#pull a python image
FROM python:3.7-alpine3.14

#Setup working directory
WORKDIR /app

#add all files from current directory
ADD . /app

##create a interpeter for cffi
RUN apk add --no-cache --virtual .pynacl_deps build-base python3-dev libffi-dev

#update tools
RUN apk -U upgrade
RUN pip install --upgrade setuptools
RUN apk add --no-cache libffi-dev openssl-dev

#CD to app
RUN cd app
#install dependency
RUN pip install --trusted-host pypi.python.org -r requirments.txt
#expose port to 80 and 8000
EXPOSE 8000
#run gunicorn command
CMD [ "python", "./test.py"]
CMD gunicorn -w 1 -b 0.0.0.0:8000 run:app