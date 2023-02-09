#!/usr/bin/env python
from itertools import count
from textwrap import indent
from turtle import done, position
import matplotlib.patches as mpatches
from matplotlib.patches import Rectangle
import matplotlib.pyplot as plt
import sys
from Bio import SeqIO
import random
import re

sequence2_inputfile = sys.argv[1]
chromosome_name = sys.argv[2]

#import sequence 2
sequence2 = []
with open(sequence2_inputfile, 'r') as file:
  for line in file:
    line = line.rstrip()
    sequence2.append(line)
  done
file.close()
sequence2 = ''.join(sequence2)
sequence2 = sequence2.upper()


#count number of contigs by looking for Ns (pattern searched for has 100)
pattern = 'NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN'
f = open("contigs.bed", 'a+')
for m in re.finditer(pattern, sequence2):
    f.write(str(chromosome_name) + '\t' + str(m.start()) + '\t' + str(m.end()) + '\t' + 'N' + str(random.randint(0,10000)) + '\n')
done
f.close()
