#!/bin/bash

docker network create -d bridge \
--attachable \
--opt com.docker.network.bridge.name=egg0 \
--opt com.docker.network.bridge.enable_ip_masquerade=true \
--opt com.docker.network.bridge.enable_icc=true \
--opt com.docker.network.bridge.host_binding_ipv4=0.0.0.0 \
eggnet