#!/bin/bash
# 20150617 v 0.0.1

if [ $# -ne 2 ];then
		echo -e "\tusage:"
		echo -e "\t ./rename_host.sh <new hostname>"
		exit
fi

sudo hostname $1
if [ $? -eq 0 ];then
		echo "modify hostname success"
fi

ip=$(ifconfig | grep "inet addr" | grep -v "127.0.0.1" | cut -d: -f2| awk '{print $2}')

sed -i '$d' /etc/hosts
sudo echo -e $ip"    "$1 >> /etc/hosts

if [ $? -eq 0 ];then
		echo "modify /etv/hosts success"
fi

sed -i '$d' /etc/sysconfig/network
sudo echo "HOSTNAME=\""$1"\"" >> /etc/sysconfig/network
if [ $? -eq 0 ];then
		echo "modify /etv/sysconfig/network success"
fi



