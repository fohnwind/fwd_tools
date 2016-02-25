#!/bin/bash
# 20151103 V0.0.2 stable

set -e

if [ $# -ne 1 ];then
    echo -e "\tusage:"
    echo -e "\t ./rename_host.sh <new hostname>"
    exit
fi

echo "> hostname will become --> "$1
sudo hostname $1

if [ $? -eq 0 ];then
    echo "modify hostname success"
fi

ip=$(ifconfig | grep "inet addr" | grep -v "127.0.0.1" | cut -d: -f2| awk '{print $1}')
echo "> host ip is --> "$ip
#可以先做一个备份 然后对比blablabla
#cp /etc/hosts  ~/hosts.bak
sed -i '$d' /etc/hosts
sudo echo -e $ip"    "$1 >> /etc/hosts

if [ $? -eq 0 ];then
    echo "modify /etc/hosts success"
fi

#cp /etc/sysconfig/network ~/network.bak
sed -i '$d' /etc/sysconfig/network
sudo echo "HOSTNAME=\""$1"\"" >> /etc/sysconfig/network

if [ $? -eq 0 ];then
    echo "modify /etc/sysconfig/network success"
fi


