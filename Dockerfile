FROM ubuntu:16.04

# Base
RUN apt-get update && apt-get install -y \
      curl \
      build-essential \
      software-properties-common

# Python3
RUN add-apt-repository ppa:jonathonf/python-3.6
RUN apt-get update && apt-get install -y \
      python3.6 \
      python3-dev

# and pip
RUN curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
RUN python3 get-pip.py

# Bluetooth and audio
RUN apt-get update && apt-get install -y \
      bluez \
      bluez-tools \
      pulseaudio \
      pkg-config \
      # libboost-python-dev \
      # libboost-thread-dev \
      libbluetooth-dev
      # libglib2.0-dev \

RUN pip install pybluez
