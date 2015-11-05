#!/bin/bash

for ip in `cat hosts`
do
    ping -c 1 -w 1 -i 0.2 $ip &> /dev/null
    if [ $? -eq 0 ];then
		echo -e "\033[32m $ip is up\e[0m"
    else
		echo -e "\033[31m $ip is down\033[0m"
    fi
done
