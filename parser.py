#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Chao Suo"

from misc import *
import pafy
import ffmpy
import os
import tempfile
import shutil
import errno

'''
Module: parser.py
Function: Taking in a link of online video, download its audio file and convert 
to wav format, saved in temp directory
Input: url, type=str
Output: cwd, temp_dir, output_file_path, type=str
'''

class VideoParser():
    def _create_temp_dir(self):
        return os.getcwd(), tempfile.mkdtemp()

    def _download_audio(self, url, temp_dir):
        # call pafy to extract audio file from the video and save in temp dir
        video = pafy.new(url)
        bestAudio = video.getbestaudio()
        audio_name = 'audio.opus'
        audio_file_path = os.path.join(temp_dir, audio_name)
        bestAudio.download(filepath=audio_file_path, quiet=False)
        return audio_file_path

    def _convert_to_wav(self, temp_dir, audio_file_path):
        # call ffmpy to convert audio file to wav format, save in temp dir
        output_name = 'output.wav'
        output_wav_path = os.path.join(temp_dir, output_name)
        ff = ffmpy.FFmpeg(
            inputs = {audio_file_path : None}, 
            outputs = {output_wav_path : '-ar 16000 -ac 1'}
            )
        ff.run()
        return output_wav_path

    def parse_to_wav(self, url):
        '''
        Take in a valid url of the video, call pafy to download its audio file,
        save in a temporary directory and call ffmpeg to convert the audio file 
        to wav format, also saved in the temporary directory.
        '''
        mlog("Start parsing video...")

        # set up temp dir
        cwd, temp_dir = self._create_temp_dir()
        # extract audio
        audio_file_path = self._download_audio(url, temp_dir)
        # convert audio to wav
        output_wav_path = self._convert_to_wav(temp_dir, audio_file_path)

        mlog("Parsing finished, wav file generated in temp directory")
        return cwd, temp_dir, output_wav_path

video_parser = VideoParser()

if __name__ == '__main__':
    vp = VideoParser()
    _, tmp, output_file_path = vp.parse_to_wav("https://www.youtube.com/watch?v=pJY0mBWHPw4")
    print tmp
    print output_file_path
    try:
        shutil.rmtree(tmp) # delete temp directory
    except OSError as exc:
        if exc.errno != errno.ENOENT: # ENOENT - no such file or directory
            raise  # re-raise exception
    mlog("Temp dir is removed")