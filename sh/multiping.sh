#!/bin/bash

cat hosts | xargs -i -P 20 sh -c 'ping -c 1 -w 1 -i 0.2 {} &> /dev/null && echo -e "\033[32m {} is up\e[0m" || echo -e "\033[31m {} is down\033[0m"' ;