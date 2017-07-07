#!/usr/bin/python
from __future__ import unicode_literals

import os
import sys
import subprocess
# Youtube-dl
import youtube_dl
# Music player
import pygame

# Depends on ffmpeg, youtube-dl and pygame
# If youtube-dl is outdated or libs are missing - upgrade with: sudo -H pip install --upgrade youtube-dl pygame

# Script accepts exactly one argument
if len(sys.argv) != 2:
    print ("Please supply only one sound name/case")
    sys.exit()

case = str.lower(sys.argv[1])

cases = {
    'leeroy': {'vid': 'mLyOj_QD4a4', 'trim': ['-t', '00:00:04.500', '-ss', '00:01:25.500']},
    'kotka' : {'vid': 'plahwm0vfys', 'trim': None},
    'ujas'  : {'vid': 'Wp3pmqBDzQ8', 'trim': ['-t', '00:00:07.000', '-ss', '00:00:00.500']}
}

if case in cases:
    fname = os.path.dirname(os.path.realpath(__file__)) + "/" + case + ".wav"
else:
    print ("Unknown case")
    sys.exit()

# Download and convert sound file if it doesn't exist
if not os.path.exists(fname):
    ydl_opts = {
    'format': 'bestaudio/best',
    'outtmpl': case + '.%(ext)s',
    'postprocessors': [{'key': 'FFmpegExtractAudio', 'preferredcodec': 'wav', 'preferredquality': '5', 'nopostoverwrites': False}],
#    'postprocessor_args': cases[case]['trim'],
    'quiet': True
    }
    if cases[case]['trim'] != None:
        ydl_opts['postprocessor_args'] = cases[case]['trim']

#    print (ydl_opts)

    # Setup youtube-dl object
    ydl = youtube_dl.YoutubeDL(ydl_opts)
    # Perform download and postprocessing
    ydl.download ([cases[case]['vid']])

pygame.mixer.init()
pygame.mixer.music.load(fname)
pygame.mixer.music.play()
while pygame.mixer.music.get_busy() == True:
    continue
