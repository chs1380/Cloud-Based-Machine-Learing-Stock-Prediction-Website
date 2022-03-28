#pull a python image
FROM smizy/scikit-learn:latest

#Setup working directory
WORKDIR /app

#add all files from current directory
ADD . /app
RUN rm -rf venv

##create a interpeter for cffi
RUN apk add --no-cache --virtual .pynacl_deps build-base python3-dev libffi-dev
RUN apk update && apk add libxml2 libxslt-dev
#update tools
RUN apk -U upgrade
RUN pip install --upgrade setuptools
RUN apk add --no-cache libffi-dev openssl-dev
RUN apk add --no-cache bash

#CD to app
RUN python -m venv venv
RUN source venv/bin/activate
#install dependency
RUN pip install --trusted-host pypi.python.org -r requirements_docker.txt
#expose port to 80 and 8000
EXPOSE 8000
#run gunicorn command
CMD bash ./script.sh