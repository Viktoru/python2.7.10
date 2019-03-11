#!/usr/bin/env python
# -*- coding: utf-8 -*-
#by Victor Unda

# Learning python:
# https://www.python.org/

import csv          # Lib/csv.py ...file
import itertools    #function for an efficient looping
import codecs
import string

with open("Apple.txt", "r") as in_file:

    linee = str(in_file.read())
    cropline = str.replace(linee, 'Origin:', '<b>Origin:</b>')
    cropline2 = str.replace(cropline, 'Fruit:', '<b>Fruit:</b>')
    cropline3 = str.replace(cropline2, 'Tree:', '<b>Tree:</b>')

    lines = cropline3.splitlines()     #returns a list with all the lines in string, including the line breaks

    stripped = [line.split('. ', 1)for line in lines ] #split, first ". "

    grouped = itertools.izip(*[stripped]*1) #Functions creating iterators for efficient (izip) looping

    with open('Apple01.csv', 'w') as out_file: # this is my output file

        nrsp10_w = csv.writer(out_file) # return object responsible for converting nrsp10 data into delimited strings.
        nrsp10_w.writerow(('Crop', 'Description')) # write the row paremeter to the writer's nrsp10 data file object.

        for group in grouped: # loop
            nrsp10_w.writerows(group)
