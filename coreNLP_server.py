#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Chao Suo"

from misc import *
import subprocess

'''
Module: coreNLP_server.py
Function: Start the coreNLP server by calling subprocess, and provide function
to shut down the server
Input: None
Output: None
'''

class CoreNLPServer:
	def __init__(self):
		# cmd line arguments to be called in subprocess
		self.arguments = ['java','-mx4g','-cp','*','edu.stanford.nlp.pipeline.StanfordCoreNLPServer','-port','8999','-timeout','20000']

	def run(self): # Start server
		mlog("Server started...")
		sp = subprocess.Popen(self.arguments, cwd="./stanford-corenlp-full-2017-06-09")
		return sp

	def stop(self, sp): # Terminate server
		sp.kill()
		mlog("Server is now shut down.")

corenlp_server = CoreNLPServer()

if __name__ == '__main__':
	server = CoreNLPServer()
	curt_process = server.run()
	server.stop(curt_process)