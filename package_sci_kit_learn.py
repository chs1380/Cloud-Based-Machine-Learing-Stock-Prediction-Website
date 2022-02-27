from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from dateutil.relativedelta import relativedelta
import joblib
import pandas as pd
from sklearn.neural_network import  MLPRegressor
import pandas_ta

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
    model_10days=joblib.load('LR_model_10_Days')
    model_60_days=joblib.load('LR_model_60_Days')
    model_365_days=joblib.load('LR_model_365_Days')

    prediction = df_today[features_to_fit]

    future_price_10_days= model_10days.predict(prediction)
    future_price_60_days= model_60_days.predict(prediction)
    future_price_365_days= model_365_days.predict(prediction)

    return future_price_10_days,future_price_60_days,future_price_365_days


def prediction_fucnction_mlp(df):
    # number of days need to forecast in the future
    forecast_day = int(365)
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

    prediction = df_today[features_to_fit]

    model = joblib.load('MLP_model')
    future_price=model.predict(prediction)
    df['NextClose'] = df['Close'].shift(-forecast_day)
    return future_price

result=prediction_fucnction('AAPL.csv')
print(result)



# def prediction_fucnction(df):
#     # number of days need to forecast in the future
#     forecast_day = int(365)
#     df = pd.read_csv(df)
#     # modify data drop all columns except the closing price
#
#     # set date as index and data type as date time
#     df['Date'] = pd.to_datetime(df.Date)
#     df.index = df['Date']
#     df.dropna()
#
#     # drop all column except the closing price axis=1 mean colmun
#     df.drop(['Open', 'High', 'Low', 'Adj Close', 'Volume'], axis=1, inplace=True)
#
#     # use panda ta library to generate exponential moving average in range of 10 days
#     df.ta.ema(close='Close', length=10, append=True)
#
#     # Price after n days, shift mean make the last -forecast_day data as NAN
#     df_today = df.iloc[-1:, :].copy()  # get last row  [ 0:3( 1 - 4 row),0:3( 1-4 column)]
#
#     # make forecast day row is 0 to train,for example last
#     df['NextClose'] = df['Close'].shift(-forecast_day)
#
#     # independent variable
#     features_to_fit = ['Close', 'EMA_10']
#
#     df.fillna(0, inplace=True)
#
#     # this is for sci kit learn trianing
#     X = df[features_to_fit]
#     Y = df['NextClose']
#
#     # train the model
#     # split data for training, 70% for traing and 30 % for training
#     X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3)
#
#     # Traning, testing to plot graphs
#     model = LinearRegression()
#
#     model.fit(X_train, Y_train)
#
#     joblib.dump(model,"LR_model_365_Days")
#     prediction = df_today[features_to_fit]
#
#     future_price = model.predict(prediction)
#     df['NextClose'] = df['Close'].shift(-forecast_day)
#
#     # the actual data
#
#     return future_price
# print(prediction_fucnction('AAPL.csv'))
#
# # def prediction_fucnction_mlp(df):
#     # number of days need to forecast in the future
#     forecast_day = int(365)
#     df = pd.read_csv(df)
#     # modify data drop all columns except the closing price
#
#     # set date as index and data type as date time
#     df['Date'] = pd.to_datetime(df.Date)
#     df.index = df['Date']
#     df.dropna()
#
#     # drop all column except the closing price axis=1 mean colmun
#     df.drop(['Open', 'High', 'Low', 'Adj Close', 'Volume'], axis=1, inplace=True)
#
#     # use panda ta library to generate exponential moving average in range of 10 days
#     df.ta.ema(close='Close', length=10, append=True)
#
#     # Price after n days, shift mean make the last -forecast_day data as NAN
#     df_today = df.iloc[-1:, :].copy()  # get last row  [ 0:3( 1 - 4 row),0:3( 1-4 column)]
#
#     # make forecast day row is 0 to train,for example last
#     df['NextClose'] = df['Close'].shift(-forecast_day)
#
#     # independent variable
#     features_to_fit = ['Close', 'EMA_10']
#
#     df.fillna(0, inplace=True)
#
#     # this is for sci kit learn trianing
#     X = df[features_to_fit]
#     Y = df['NextClose']
#
#     # train the model
#     # split data for training, 70% for traing and 30 % for training
#     X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3)
#
#     # Traning, testing to plot graphs
#     mlp = MLPRegressor()
#     mlp.fit(X_train, Y_train)
#     joblib.dump(mlp,"MLP_model_365_Days")
#
#     prediction = df_today[features_to_fit]
#
#     future_price = mlp.predict(prediction)
#     df['NextClose'] = df['Close'].shift(-forecast_day)
#
#     # the actual data
#
#     return future_price
#
# print(prediction_fucnction_mlp('AAPL.csv'))
