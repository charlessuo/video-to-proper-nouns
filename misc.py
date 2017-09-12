#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Chao Suo"

'''
Module: misc.py
Function: Used as a tool to generate simple system log
Input: text to print in log, type=str
Output: [APP LOG] log
'''

def mlog(str, level="APP LOG"):
	print "[%s] %s" % (level, str)