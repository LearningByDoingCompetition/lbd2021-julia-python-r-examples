FROM docker.io/ubuntu:20.04

ARG DEBIAN_FRONTEND=noninteractive
ENV TZ=Europe/London

RUN apt-get update && \
    apt-get install -y \
    busybox julia \
    && apt-get clean && \
    rm -rf /var/cache/apt/lists/*

RUN useradd -u 12345 -ms /bin/bash user
USER user
WORKDIR /home/user

RUN julia -e 'using Pkg; Pkg.add.(["ZMQ", "JSON"]); Pkg.precompile()'
