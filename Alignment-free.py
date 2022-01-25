#!/usr/bin/env python
from itertools import count
from textwrap import indent
from turtle import done, position
import matplotlib.patches as mpatches
from matplotlib.patches import Rectangle
import matplotlib.pyplot as plt
import sys
from Bio import SeqIO

sequence1 = []
with open('/lustre/scratch123/tol/projects/badass/users/ak37/pangenome/gambiae-SV1/3RL/idAnoGambDA_150_04_1_3RL.fa', 'r') as file:
    for line in file:
        line = line.rstrip()
        sequence1.append(line)
    done
file.close
sequence1 = ''.join(sequence1)


sequence2 = []
with open('/lustre/scratch123/tol/projects/badass/users/ak37/pangenome/gambiae-SV1/3RL/idAnoGambDA_407_04_1_3RL.fa', 'r') as file:
    for line in file:
        line = line.rstrip()
        sequence2.append(line)
    done
file.close
sequence2 = ''.join(sequence2)


kmer_list_sequence1 = []
for i in range(0, len(sequence1)-31):
    kmer = sequence1[i:i+31] 
    kmer_list_sequence1.append(kmer)
done

print(kmer_list_sequence1[0])


kmer_list_sequence2 = []
for i in range(0, len(sequence2)-31):
    kmer = sequence2[i:i+31] 
    kmer_list_sequence2.append(kmer)
done

unique_kmers_sequence1 = list(dict.fromkeys(kmer_list_sequence1))
unique_kmers_sequence2 = list(dict.fromkeys(kmer_list_sequence2))


#Identify inversions, and append their index to inversion_log
inversion_log = []
for i in kmer_list_sequence2:
    if i in unique_kmers_sequence2:
        inverted_kmer = i[::-1]

        if inverted_kmer in unique_kmers_sequence1:
            inversion_log.append(kmer_list_sequence2.index[i])
        done
    done
done

print(len(inversion_log))

f = open('alignment.free.unique.invs', 'a')
for i in inversion_log:
    f.write(str(i))
    f.write("\n")
done
f.close()
