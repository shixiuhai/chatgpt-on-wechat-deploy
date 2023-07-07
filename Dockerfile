
# FROM python:3

# RUN mkdir /data
# WORKDIR /data
# ADD requirements.txt /data/

# RUN pip install --no-cache-dir -r requirements.txt -i https://pypi.douban.com/simple

# docker build -t chatgpt/wechat/env:latest  .
FROM python:3.10-slim
RUN mkdir /data
WORKDIR /data
RUN sed -i 's/deb.debian.org/mirrors.tuna.tsinghua.edu.cn/g' /etc/apt/sources.list
ADD chatgpt-on-wechat/requirements-optional.txt /data/
ADD chatgpt-on-wechat/requirements.txt /data/
ARG TZ='Asia/Shanghai'
RUN apt-get update \
    &&apt-get install -y --no-install-recommends bash ffmpeg espeak libavcodec-extra\
    && /usr/local/bin/python -m pip install --no-cache --upgrade pip \
    && pip install --no-cache -r requirements.txt \
    && pip install --no-cache -r requirements-optional.txt \
    && pip install azure-cognitiveservices-speech

