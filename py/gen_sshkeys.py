#!/usr/bin/env python
# -*- coding:utf-8 -*-
 
# by fohnwind

from os import chmod
from Crypto.PublicKey import RSA

key = RSA.generate(2048)
private_key = "/tmp/temp.key"
public_key = "/tmo/temp.key.pub"

with open(private_key, 'w') as f:
	chmod(private_key, 0600)
	f.write(key.exportKey("PEM"))

pkey = key.publickey()

with open(public_key, 'w') as f:
	f.write(pkey.exportKey('OpenSSH'))