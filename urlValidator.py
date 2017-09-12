#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Chao Suo"

'''
Module: urlValidator.py
Function: Check whether an url is in valid format and whether exists
However, it cannot check whether an url is a correct link to a video 
for the app to consume
Input: url, type=str
Output: boolean
'''

import urllib2
from urlparse import urlparse
from misc import *

class URLValidator:
	def validate(self, url):
		res = urlparse(url)
		if res.scheme == 'http' or res.scheme == 'https' and res.netloc != '':
			try:
				ret = urllib2.urlopen(url)
				if ret.code == 200:
					return True
				else:
					mlog("Successful requests but till something wrong, Error code:")
					mlog(ret.code)
					return False
			except urllib2.HTTPError, err:
				if err.code == 404:
					mlog("Page not found!")
					return False
				elif err.code == 403:
					mlog("Access denied!")
					return False
				else:
					mlog("Something wrong! HTTP Error code:") 
					mlog(err.code)
					return False
			except urllib2.URLError, err:
				mlog("Some URL Error happened, Error:")
				mlog(err.reason)
				return False

		mlog("Invalid URL, check scheme or netloc")
		return False

url_validator = URLValidator()

if __name__ == '__main__':
	validator = URLValidator()
	print validator.validate('https://www.youtube.com/watch?v=BJ1EGdt2Xp')