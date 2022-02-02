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
unique_kmers_sequence_2 = sys.argv[2]
sequence1_inputfile = sys.argv[3]
sequence2_inputfile = sys.argv[4]

#import sequence 1
sequence1 = []
with open(sequence1_inputfile, 'r') as file:
    for line in file:
        line = line.rstrip()
        sequence1.append(line)
    done
file.close()
sequence1 = ''.join(sequence1)
sequence1 = sequence1.upper()

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
done



#import sequence 2 unique kmers (produced by jellyfish)
unique_kmer_list_sequence2 = []
with open(unique_kmers_sequence_2, 'r') as file:
    for line in file:
        line = line.rstrip()
        unique_kmer_list_sequence2.append(line)
    done
    file.close()
done


#invert each unique kmer in sequence 1, and find its potential equivalent in sequence 2
#inversions are reverse complements!

results = []
reverse_complement_unique_kmers_sequence1 = []

for i in unique_kmer_list_sequence1:
    kmer = str(i)
    reverse_complement_kmer = kmer[::-1]
    reverse_complement_kmer = reverse_complement_kmer.replace("C", "g")
    reverse_complement_kmer = reverse_complement_kmer.replace("G", "c")
    reverse_complement_kmer = reverse_complement_kmer.replace("A", "t")
    reverse_complement_kmer = reverse_complement_kmer.replace("T", "a")
    reverse_complement_kmer = reverse_complement_kmer.upper()

    if reverse_complement_kmer in unique_kmer_list_sequence2:
        index_sequence1 = sequence1.index(kmer)
        index_sequence2 = sequence2.index(reverse_complement_kmer)
        f = open('structural_variation.out', 'a')
        f.write("2RL\t" + str(index_sequence1) + "\t" + str(index_sequence1+30) + "\t2RL\t" + str(index_sequence2) + "\t" + str(index_sequence2+30) +"\t" + "INV" + "\n")
        f.close()
    done
done
