#!/usr/bin/env python
from itertools import count
from textwrap import indent
from turtle import done, position
import matplotlib.patches as mpatches
from matplotlib.patches import Rectangle
import matplotlib.pyplot as plt
import sys
from Bio import SeqIO

bed_file = sys.argv[1]

#import bed file
kmer_status = [] #bed file tells us whether a kmer is matched between genome 1 and 2, or there's an inversion
with open(bed_file, 'r') as file:
    for line in file:
        line = line.rstrip()
        kmer_status.append(line)
    done
file.close()

#split kmer_status list into chunks of 100
chunked_list = []
chunk_size = 100

for i in range(0, len(kmer_status), chunk_size):
    chunked_list.append(kmer_status[i:i+chunk_size])
done

#count number of INVs in each 100 kmer chunk
inversion_count = []
for i in chunked_list:
    window_100_kmers = i
    window_100_kmers = ''.join(window_100_kmers)
    inversion_count.append(window_100_kmers.count("INV"))
done



#plot % of inversions in each 100kmers going from left to right across chromosome

fig = plt.figure(figsize=(10, 5))
ax = fig.add_axes([0,0,1,1])

x_axis = (range(0, len(inversion_count)))

plt.plot(x_axis, inversion_count)
plt.ticklabel_format(style='plain')
plt.xlabel("Bins of 100 31-mers")
plt.ylabel("Percentage of inverted 31-mers")
plt.show()
plt.savefig('bins_inverted_kmer_proportion.png')
