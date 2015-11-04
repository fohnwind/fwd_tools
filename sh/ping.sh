#!/bin/bash
for ip in `cat hosts`
do
	ping -c 2 -i 0.5 $ip > /dev/null 2>&1
	if [ $? -eq 0 ];then
		echo -e "\033[32m $ip is up.\033[0m"
	else
		echo -e "\033[31m $ip is down. \033[0m"
	fi
done
