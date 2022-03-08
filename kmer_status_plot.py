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
contig_bed_file = sys.argv[2]

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


#Convert x axis from number of bins to coordinates
coordinate_x_axis = []
for i in chunked_list:
    window_100_kmers = i
    window_100_kmers = ''.join(window_100_kmers)
    coordinate_list = ([int(s) for s in window_100_kmers.split() if s.isdigit()])
    print(str(coordinate_list[0]) + " , " + str(coordinate_list[len(coordinate_list)-1]))
    coordinate_x_axis.append(coordinate_list[0])
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


#add contig data
#to prepare this, I looked for gaps of 100 Ns and marked them as a point (see contig_count.py)

#import contig bed file
contig_status = [] 
with open(contig_bed_file, 'r') as file:
    for line in file:
        line = line.rstrip()
        contig_status.append(line)
    done
file.close()

#Convert x axis from number of bins to coordinates

contig_breaks = []
for i in contig_status:
    coordinate_list = ([int(s) for s in i.split() if s.isdigit()])
    for i in range(coordinate_list[0], coordinate_list[len(coordinate_list)-1]):
        contig_breaks.append(i)
done


#plot % of inversions in each 100kmers going from left to right across chromosome WITH CONTIGS

fig = plt.figure(figsize=(10, 5))
ax = fig.add_axes([0,0,1,1])

x_axis = (range(0, len(inversion_count)))

plt.plot(coordinate_x_axis, inversion_count)

for i in contig_breaks:
    plt.axvline(x = i, color = "grey", linestyle = "--", ymin=0.90, ymax=0.95)
done


plt.ticklabel_format(style='plain')
plt.xlabel("Chromosome Coordinates")
plt.ylabel("Percentage of inverted 31-mers")
plt.title("Bins of 100 31-mers across DA150 X chromosome coordinates")
plt.show()
plt.savefig('bins_inverted_kmer_proportion_contigs.png')
