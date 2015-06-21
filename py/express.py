#!/bin/python
#-*- coding:utf-8 -*-


import sys
import requests
import json
import re
import argparse

def main():
	reload(sys)
	sys.setdefaultencoding('utf8')
	parser = argparse.ArgumentParser(usage='python express.py -t SF -n 532951504202',description="Express assistant")
	parser.add_argument("-n","--number",type=int,help="input your order number")
	parser.add_argument("-t","--type",help="your express company(SF,STO,ZTO,YD,YTO,TT)")
	args = parser.parse_args()
	if args.type == None or args.number == None:
		parser.print_help()
		exit()

	if type(args.type) != type('str') or type(args.number) != type(1):
		print "error parameters"
		exit()

	d = {'SF':sf,'YTO':yto,'STO':sto}
	return d.get(args.type.upper())(args.number)

def zto(order_number):
	pass

def sto(order_number):
	pass

def yto(order_number):
	pass

def yd(order_number):
	pass

def sf(order_number):
	sf_url_head = "http://www.sf-express.com/sf-service-web/service/bills/"
	sf_url_tail = "/routes?app=bill&lang=sc&region=cn&translate="

	url = sf_url_head + str(order_number) + sf_url_tail
	print "正在处理查询结果，请稍后"
	r = requests.get(url)
	if r.text == '[]':
			print "查询失败，请确认清单号以及快递公司准确性"
			exit()

	print "-" * 20
	data = json.dumps(r.json(),ensure_ascii=False)
	temp = data.decode("utf-8")
	newdata = json.loads(data,encoding="utf-8")

	print "查询订单号:"+str(newdata[0]['id'])
	print "始发地:"+newdata[0]['origin']
	print "目的地:"+newdata[0]['destination']
	print "订单状态:"
	print "=" * 20
	print '\033[1;34m',"运单状态修改时间\t状态",'\033[0m'
	for i in newdata[0]['routes']:
			print '\033[1;32m' + i['scanDateTime'] + "\t" + re.sub('<[^>]+>','',i['remark']) + '\033[0m'

if __name__ == '__main__':
	main()