#!/bin/bash
# for baidu interview 2015.8

SUM=1 #factor 1 = 1

for i in $(seq 1 100)
do
	j=$(factor $i | awk '{if (NF==2) print $2}')
	(( SUM=SUM+j ))
done

echo $SUM
