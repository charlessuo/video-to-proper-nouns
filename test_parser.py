#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Chao Suo"

import unittest
import os
import shutil
import errno
from parser import video_parser

class ParserTestCase(unittest.TestCase):
	'''
	Tests for parser.py
	'''

	def setUp(self):
		'''
		set up by creating temp dir, downloading audio and converting to wav
		'''
		_, self.temp_dir = video_parser._create_temp_dir()
		self.audio_file_path = video_parser._download_audio("https://www.youtube.com/watch?v=ekZZZPRxWtI", self.temp_dir)
		self.output_wav_path = video_parser._convert_to_wav(self.temp_dir, self.audio_file_path)

	def tearDown(self):
		'''
		Clean up temp dir
		'''
		try:
			shutil.rmtree(self.temp_dir) # delete temp directory
		except OSError as exc:
			if exc.errno != errno.ENOENT: # ENOENT - no such file or directory
				raise  # re-raise exception

	def test_parser_create_temp_dir(self):
		'''
		Check whether temporary directory is successfully created.
		'''
		self.assertTrue(os.path.isdir(self.temp_dir))

	def test_parser_download_audio(self):
		'''
		Test whether audio is downloaded to the correct temp path
		'''
		self.assertTrue(os.path.exists(self.audio_file_path))

	def test_parser_convert_to_wav(self):
		'''
		Test whether wav is converted and saved to the correct temp path
		'''
		self.assertTrue(os.path.exists(self.output_wav_path))


if __name__ == '__main__':
	unittest.main()



