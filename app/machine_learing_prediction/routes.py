from flask import Flask, request, render_template, flash, redirect, url_for
from app.machine_learing_prediction import bp
from flask_login import login_required, current_user
import fileinput
from config import Config
from model import Result
from app.machine_learing_prediction.form import ml_form
from flask_login import login_required
import pandas as pd
import pandas_ta
from app import db
from model import Result, Model
from datetime import date, datetime
import yfinance as yf
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from dateutil.relativedelta import relativedelta
from matplotlib import pyplot as plt
import os
from sklearn.neural_network import MLPClassifier, MLPRegressor
import joblib



def get_history_price(stockCode):
    end_date = datetime.now()
    start_date = datetime.now() - relativedelta(years=10)
    price = yf.download(stockCode, start=start_date, end=end_date)
    # set it to panda dataframe for better manipulation and save to CSV
    df = pd.DataFrame(data=price)
    df.to_csv(stockCode + '.csv')
    return "csv saved"


def prediction_fucnction(df):
    df = pd.read_csv(df)
    # modify data drop all columns except the closing price
    # set date as index and data type as date time
    df['Date'] = pd.to_datetime(df.Date)
    df.index = df['Date']
    df.dropna()

    # drop all column except the closing price axis=1 mean colmun
    df.drop(['Open', 'High', 'Low', 'Adj Close', 'Volume'], axis=1, inplace=True)

    # use panda ta library to generate exponential moving average in range of 10 days
    df.ta.ema(close='Close', length=10, append=True)

    # Price after n days, shift mean make the last -forecast_day data as NAN
    df_today = df.iloc[-1:, :].copy()  # get last row  [ 0:3( 1 - 4 row),0:3( 1-4 column)]

    # independent variable
    features_to_fit = ['Close', 'EMA_10']

    df.fillna(0, inplace=True)

    # Traning, testing to plot graphs
    model_10days=joblib.load('app/machine_learing_prediction/LR_model_10_Days')
    model_60_days=joblib.load('app/machine_learing_prediction/LR_model_60_Days')
    model_365_days=joblib.load('app/machine_learing_prediction/LR_model_365_Days')

    prediction = df_today[features_to_fit]

    future_price_10_days= model_10days.predict(prediction)
    future_price_60_days= model_60_days.predict(prediction)
    future_price_365_days= model_365_days.predict(prediction)

    return future_price_10_days,future_price_60_days,future_price_365_days

def prediction_fucnction_mlp(df):
    df = pd.read_csv(df)
    # modify data drop all columns except the closing price

    # set date as index and data type as date time
    df['Date'] = pd.to_datetime(df.Date)
    df.index = df['Date']
    df.dropna()

    # drop all column except the closing price axis=1 mean colmun
    df.drop(['Open', 'High', 'Low', 'Adj Close', 'Volume'], axis=1, inplace=True)

    # use panda ta library to generate rsi in range of 10 days
    df['RSI']=df.ta.rsi(close='Close', length=10, append=True)

    # Price after n days, shift mean make the last -forecast_day data as NAN
    df_today = df.iloc[-1:, :].copy()  # get last row  [ 0:3( 1 - 4 row),0:3( 1-4 column)]

    # independent variable
    features_to_fit = ['Close', 'RSI']

    df.fillna(0, inplace=True)



    # Use model to predict the stock price
    model_10days = joblib.load('app/machine_learing_prediction/MLP_model_10_Days')
    model_60_days = joblib.load('app/machine_learing_prediction/MLP_model_60_Days')
    model_365_days = joblib.load('app/machine_learing_prediction/MLP_model_365_Days')

    prediction = df_today[features_to_fit]

    future_price_10_days = model_10days.predict(prediction)
    future_price_60_days = model_60_days.predict(prediction)
    future_price_365_days = model_365_days.predict(prediction)
    return future_price_10_days, future_price_60_days, future_price_365_days

@login_required
@bp.route('/ml_predict', methods=['GET', 'POST'])
def prediction():
    form = ml_form(csrf_enabled=False)
    form.ml_model.choices = [(model.Model_id, model.Model_name) for model in Model.query.all()]
    prediction_histroy=[]
    if current_user.is_authenticated:
        prediction_histroy = Result.query.filter_by(user_id=current_user.User_id)  # query all the history prediction
        if request.method == 'POST' and form.validate_on_submit():
            stock_code = form.stock_code.data
            get_model_name = Model.query.filter_by(
                Model_id=form.ml_model.data).first()
            if get_model_name.Model_name == "linear regression":
                # first get stock csv first
                get_history_price(stock_code)
                # train and predict price of stock
                # today_price
                today_price = yf.Ticker(form.stock_code.data)
                price = today_price.info['regularMarketPrice']
                # prediction with prediction and mark to database
                future_price = prediction_fucnction(stock_code + '.csv')
                prediction_record = Result(Stock_code=stock_code, Old_price=price,
                                           price_after_10=round(int(future_price[0]), 3),
                                           price_after_60=round(int(future_price[1]), 3),
                                           price_after_360=round(int(future_price[2]), 3),Model="linear regression",Model_id=form.ml_model.data,user_id=current_user.User_id,
                                           Date_that_init_predict=datetime.now())
                # user_id=current_user.User_id)
                db.session.add(prediction_record)
                db.session.commit()
                os.remove(stock_code + '.csv')
                flash('Success predict stock ' + str(stock_code) + ' price after 10 days will be $' + str(
                    round(int(future_price[0]), 3)), category='success')
                return redirect('/ml_predict')
            #
            elif get_model_name.Model_name == "MLP prediction":
                # first get stock csv first
                get_history_price(stock_code)
                # train and predict price of stock
                # today_price
                today_price = yf.Ticker(form.stock_code.data)
                price = today_price.info['regularMarketPrice']
                # prediction with prediction and mark to database
                future_price = prediction_fucnction_mlp(stock_code + '.csv')
                prediction_record = Result(Stock_code=stock_code, Old_price=price,
                                           price_after_10=round(int(future_price[0]), 3),
                                           price_after_60=round(int(future_price[1]), 3),
                                           price_after_360=round(int(future_price[2]), 3), Model="MLP prediction",
                                           Date_that_init_predict=datetime.now(),Model_id=form.ml_model.data,
                                           user_id=current_user.User_id)
                db.session.add(prediction_record)
                db.session.commit()
                os.remove(stock_code + '.csv')
                flash('Success predict stock ' + str(stock_code) + ' price after 10 days will be $' + str(
                    round(int(future_price[0]), 3)),
                      category='success')
                return redirect('/ml_predict')
    else:
        flash('Please register an account to use prediction!',category='danger')
        return redirect(url_for('Home_Page.home'))
    return render_template('machine_learning_prediction/prediction.html',
                           prediction_histroy=prediction_histroy, form=form)