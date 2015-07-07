#!/bin/python
# -*- coding:utf-8 -*-

import requests
import json

#r = requests.get("https://api.weibo.com/oauth2/authorize?client_id=4181570995&redirect_uri=http://neuibm.club")

#暂时还不能自动登录获得getAuthorize

def getAuthorize():
		return ""

def getToken(AppKey,AppSecret,code,redirect_uri):
		data = {'client_id':AppKey,'client_secret':AppSecret,'grant_type':'authorization_code','code':code,'redirect_uri':redirect_uri}
		r = requests.post("https://api.weibo.com/oauth2/access_token",data=data)
		#data = json.loads(r.json())
		data = r.json()
		print data

if __name__ == '__main__':
    test()
