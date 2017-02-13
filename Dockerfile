# use base python image with python 4.4
FROM python:3.4

# create app directory
RUN mkdir /app

# set working directory to /app/
WORKDIR /app/


# add requirements.txt to the image
ADD requirements.txt /app/requirements.txt

# install python dependencies
CMD pip install -r requirements.txt

# ??
ADD . /app/
# TODO do we need this?
# # create unprivileged user
# RUN adduser --disabled-password --gecos '' entrayn