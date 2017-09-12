#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Chao Suo"

from pycorenlp import StanfordCoreNLP
from misc import *

'''
Module: nerTagger.py
Function: Taking in transcript in string format, run coreNLP annotators to annotate
proper nouns in the transcript
Input: transcript, type=str
Output: tagging dict, type=json/conll
'''

class NERTagger:
	def __init__(self):
		self.tagger = StanfordCoreNLP('http://localhost:8999')
		self.truecase_props = {'annotators': 'truecase',
								'outputFormat': 'json',
								'timeout': 10000}
		self.ner_props = {'annotators': 'tokenize,ssplit,pos,lemma,ner',
						'outputFormat': 'json',
						'timeout': 10000}

	def _truecase_annotate(self, raw_input_str):
		'''
		lowercase to proper capitalized
		e.g. kobe bryant is a lakers player -> Kobe Bryant is a Lakers player
		'''
		return self.tagger.annotate(raw_input_str, properties=self.truecase_props)

	def _ner_annotate(self, caped_input):
		'''
		tag proper nouns in a input sentence as string
		e.g. Kobe Bryant is a Lakers player
		->   Kobe: PERSON, Bryant: PERSON, Lakers: ORGANIZATION
		'''
		return self.tagger.annotate(caped_input, properties=self.ner_props)

	def _format_output(self, result):
		'''
		Take in original json output from coreNLP annotators and extract words
		with certain named entity tags and summarize them into a new json
		e.g.: Kobe: PERSON, Bryant: PERSON, Lakers: ORGANIZATION ->
		->    {PERSON: ['Kobe Bryant'], 
			   ORGANIZATION: ['Lakers']}
		'''
		token_dict = result["sentences"][0]["tokens"]
		categories = ["PERSON", "LOCATION", "ORGANIZATION", "MISC", \
					  "MONEY", "NUMBER", "ORDINAL", "PERCENT", \
					  "DATE", "TIME", "DURATION", "SET"]
		# Summarize the words with certain tags as categories
		# Generate final output from tagging output from coreNLP library
		output_dict = {}
		temp_str = token_dict[0]["lemma"]
		prev_category = token_dict[0]["ner"]
		for i in range(1, len(token_dict)):
			old_item = token_dict[i - 1]
			item = token_dict[i]
			curt_cat = item["ner"]
			if curt_cat in categories and curt_cat == old_item["ner"]:
				temp_str += " " + item["lemma"]
			elif curt_cat in categories and curt_cat != old_item["ner"]:
				if prev_category in output_dict and temp_str not in output_dict[prev_category]:
					output_dict[prev_category].append(temp_str)
				elif prev_category not in output_dict and prev_category != "O":
					entity_list = []
					entity_list.append(temp_str)
					output_dict[prev_category] = entity_list
				prev_category = curt_cat
				temp_str = item["lemma"]

		return output_dict

	def annotate(self, raw_input_str):
		mlog("Start truecase annotating...")
		# Step 1. Use truecase annotator to turn lowercase transcipt into proper capitalized tokens
		caped = self._truecase_annotate(raw_input_str)

		# Step 2. Append all truecase annotated tokens together to form a new transcipt
		caped_text = ""
		for item in caped["sentences"][0]["tokens"]:
			caped_text += " " + item["truecaseText"]
		caped_text = caped_text.encode('utf-8')

		# Step 3. Run NER annotator to tag proper nouns in the transcipt
		mlog("Start tagging named entities...")
		tagging_result = self._ner_annotate(caped_text)
		# print tagging_result

		# Step 4. Extract certain tagging info to generate final output
		output_json = self._format_output(tagging_result)
		mlog("Tagging result below:")
		print output_json
		mlog("NER tagging finished")
		return output_json

ner_tagger = NERTagger()

if __name__ == '__main__':
	import time
	from coreNLP_server import corenlp_server
	curt_process = corenlp_server.run()
	time.sleep(5)
	tagger = NERTagger()
	tagger.annotate('lonzo ball talked about kobe bryant after the lakers game.')
	corenlp_server.stop(curt_process)