#!/usr/bin/env python
from itertools import count
from textwrap import indent
from turtle import done, position
import matplotlib.patches as mpatches
from matplotlib.patches import Rectangle
import matplotlib.pyplot as plt
import sys
from Bio import SeqIO

unique_kmers_sequence_1 = sys.argv[1]
sequence2_inputfile = sys.argv[2]
output_file = sys.argv[3]
chromosome = sys.argv[4]


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

#import sequence 1 unique kmers (produced by jellyfish)
unique_kmer_list_sequence1 = []
with open(unique_kmers_sequence_1, 'r') as file:
    for line in file:
        line = line.rstrip()
        unique_kmer_list_sequence1.append(line)
    done
file.close()

#find inverted kmers in sequence 2


for i in unique_kmer_list_sequence1:

    if i in sequence2:
        f = open('structural_variation.out', 'a')
        f.write(str(chromosome) + "\t" + str(sequence2.index(i) + 1) + "\t" + str(sequence2.index(i) + 32) + "\t" + "SYN" + str(unique_kmer_list_sequence1.index(i)) + "\n")
        f.close()
    done

    kmer = str(i)
    reverse_complement_kmer = kmer[::-1]
    reverse_complement_kmer = reverse_complement_kmer.replace("C", "g")
    reverse_complement_kmer = reverse_complement_kmer.replace("G", "c")
    reverse_complement_kmer = reverse_complement_kmer.replace("A", "t")
    reverse_complement_kmer = reverse_complement_kmer.replace("T", "a")
    reverse_complement_kmer = reverse_complement_kmer.upper()

    if reverse_complement_kmer in sequence2:
        f = open(output_file, 'a')
        f.write(str(chromosome) + "\t" + str(sequence2.index(reverse_complement_kmer) + 1) + "\t" + str(sequence2.index(reverse_complement_kmer) + 32) + "\t" + "INV" + str(unique_kmer_list_sequence1.index(i)) + "\n")
        f.close()
    done
done
