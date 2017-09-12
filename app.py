#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Chao Suo"

from flask import Flask, request, render_template
from parser import video_parser
from speechRecognizer import speech_recognizer
from coreNLP_server import corenlp_server
from nerTagger import ner_tagger
from urlValidator import url_validator
from misc import *
import shutil
import errno
import json

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html')

@app.route('/res', methods=['GET'])
def fill_in():
	return render_template('home.html')

@app.route('/res', methods=['POST'])
def get_result():
	video_url = request.form['video_url']
	if url_validator.validate(video_url): # Validate the url
		# start coreNLP server
		curt_process = corenlp_server.run()
		# take in a video link, download audio and convert it to wav file, saved in temp dir
		pwd, tmp_dir, output_file_path = video_parser.parse_to_wav(video_url)
		# run speech recognition engine to generate transcript of the wav file
		transcript, _ = speech_recognizer.decode_speech(output_file_path)
		# run coreNLP NER engine to tagger proper nouns in the transcript
		result_json = ner_tagger.annotate(transcript)

		corenlp_server.stop(curt_process) # Shut down the coreNLP server

		# Remove temp file directory created in video_parser
		try:
			shutil.rmtree(tmp_dir)
		except OSError as exc:
			if exc.errno != errno.ENOENT: # ENOENT - no such file or directory
				raise  # re-raise exception
		mlog("Temp dir is removed")
		return render_template('result.html', response=json.dumps(result_json, sort_keys = True, indent = 2))
	return render_template('home.html', message='Invalid url, please enter again', video_url=video_url)

if __name__ == '__main__':
	mlog("Start Processing!")
	app.run(debug=True)

