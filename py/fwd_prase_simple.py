#!/usr/bin/python
# -*- coding:utf-8 -*-

__auther__ = 'fohnwind'
__version__ = '0.0.1 simple 20151103'
import re
import sys


def fwd_parse(target):
	#check validity
	if not target.find("[") or not target.find("]") or not target.find("-"):
		print "illegal host list"
		exit(-1)

	#parse 
	slices = re.split("\W+",target)
	start = int(slices[2])
	end = int(slices[3]) + 1
	result = []
	host_head = slices[0] + "-" + slices[1] 
	host_end = ""
	for i in slices[4:]:
		host_end += "." + i

	for i in range(start,end):
		temp = host_head + str(i) + host_end
		result.append(temp)

	#return list
	return result


if __name__ == '__main__':
	for i in sys.argv[1:]:
		print fwd_parse(i)