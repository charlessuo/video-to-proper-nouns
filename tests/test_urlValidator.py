#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Chao Suo"

import unittest
from urlValidator import url_validator

class urlValidatorTestCase(unittest.TestCase):
	'''
	Tests for urlValidator.py
	'''

	def test_validate_url_with_no_scheme(self):
		'''
		Is //www.youtube.com/watch?v=BJ1EGdt2Xp successfully validated as invalid url?
		'''
		self.assertFalse(url_validator.validate("//www.youtube.com/watch?v=BJ1EGdt2Xp"))

	def test_validate_url_with_no_netloc(self):
		'''
		Is https:///watch?v=BJ1EGdt2Xp successfully validated as invalid url?
		'''
		self.assertFalse(url_validator.validate('https:///watch?v=BJ1EGdt2Xp'))

	def test_validate_url_valid_but_does_not_exist(self):
		'''
		Is https://github.com/oauthjs/node-oauth2-server/blob/master/examples/password successfully validated as 
		website does not exist? 
		'''
		self.assertFalse(url_validator.validate("https://github.com/oauthjs/node-oauth2-server/blob/master/examples/password"))

	def test_validate_url_valid_and_exists(self):
		'''
		Is https://www.youtube.com/watch?v=BJ1EGdt2Xp successfully validated as
		valid url and website exists?
		'''
		self.assertTrue(url_validator.validate("https://www.youtube.com/watch?v=BJ1EGdt2Xp"))


if __name__ == '__main__':
	unittest.main()