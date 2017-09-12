#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Chao Suo"

from pocketsphinx.pocketsphinx import *
from sphinxbase.sphinxbase import *
from misc import *
import os

'''
Module: speechRecognizer.py
Function: Taking in a path of wav file, run speech recognition engine to generate
string of transcript
Input: path-to-wav-file, type=str
Output: transcript, type=str
'''

class SpeechRecognizer:
	def __init__(self):
		MODELDIR = "./pocketsphinx/model"
		DATADIR = "./pocketsphinx/test/data"

		# Create a decoder with certain model
		config = Decoder.default_config()
		config.set_string('-hmm', os.path.join(MODELDIR, 'en-us/en-us'))
		config.set_string('-lm', os.path.join(MODELDIR, 'en-us/en-us.lm.bin'))
		config.set_string('-dict', os.path.join(MODELDIR, 'en-us/cmudict-en-us.dict'))

		# Create decoder object for streaming data
		self.decoder = Decoder(config)

	def decode_speech(self, wav_file):
		'''
		Decode wav file to generate detected words list and generate best hypothesis
		as transcript to output
		'''
		mlog("Start speech recognition...")
		self.decoder.start_utt()
		stream = open(wav_file, "rb")
		while True:
			buf = stream.read(1024)
			if buf:
				self.decoder.process_raw(buf, False, False)
			else:
				break
		self.decoder.end_utt()
		words = []
		[words.append(seg.word) for seg in self.decoder.seg()] # save detected words
		hypothesis = self.decoder.hyp() # get best transcript
		mlog("Transcript recognized as below:")
		print 'Best hypothesis: ', hypothesis.best_score, hypothesis.hypstr
		# print 'Best hypothesis segments: ', [seg.word for seg in self.decoder.seg()]
		mlog("Speech Recognition finished")
		return hypothesis.hypstr, words

speech_recognizer = SpeechRecognizer()

if __name__ == "__main__":
	filename = "sample.wav"
	sr = SpeechRecognizer()
	transcript, _ = sr.decode_speech(filename)
	print "Transcript detected as: ", transcript