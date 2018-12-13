# Spling data from Cultivar Name and Description

import csv # convert
import itertools #function for a efficient looping
import codecs

with codecs.open('Abiutxt.txt', 'r', 'UTF-8') as in_file:
    x = in_file.read().splitlines()
    x = [line.split('. ', 1) for line in x if line]
with codecs.open('logtestAbiutxt.csv', "w", 'UTF-8') as output:
    writer = csv.writer(output, lineterminator='\n')
    writer.writerows(x)