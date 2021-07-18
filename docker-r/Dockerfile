FROM docker.io/ubuntu:20.04

ARG DEBIAN_FRONTEND=noninteractive
ENV TZ=Europe/London

RUN apt-get update && \
    apt-get install -y \
    r-base libzmq3-dev \
    && apt-get clean && \
    rm -rf /var/cache/apt/lists/*

RUN R -e "install.packages(c('rzmq', 'jsonlite'), repos='http://cran.rstudio.com/')"

RUN useradd -u 12345 -ms /bin/bash user
USER user
WORKDIR /home/user
