# Spling data from Cultivar Name and Description

import csv # convert
import itertools #function for a efficient looping

with open('Abiutxt.txt', 'r') as in_file:
    with open('logtestAbiutxt.csv', 'w') as out_file:
        writer = csv.writer(out_file, delimiter="\t")
        writer.writerow(('Cultivar Name', 'Description'))

        for line in in_file:
            if not line.strip():
                continue

            writer.writerow(line.strip().split(". ", 1))