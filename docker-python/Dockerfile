FROM docker.io/ubuntu:20.04

ARG DEBIAN_FRONTEND=noninteractive
ENV TZ=Europe/London

RUN apt-get update && \
    apt-get install -y \
    python3-pip \
    && apt-get clean && \
    rm -rf /var/cache/apt/lists/*

RUN pip install \
    pyzmq \
    --no-cache-dir

RUN useradd -u 12345 -ms /bin/bash user
USER user
WORKDIR /home/user
