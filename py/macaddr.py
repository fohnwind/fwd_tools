#!/usr/bin/env python
# -*- coding:utf-8 -*-
# fohnwind 20160111

import uuid

def mac():
	mac = uuid.UUID(int = uuid.getnode()).hex[-12:]
	return ':'.join([mac[i:i+2] for i in xrange(0,11,2)])

if __name__ == '__main__':
	print mac()
