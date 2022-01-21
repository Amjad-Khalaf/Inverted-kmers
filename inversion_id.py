#!/usr/bin/env python
from itertools import count
from textwrap import indent
from turtle import done, position
import matplotlib.patches as mpatches
from matplotlib.patches import Rectangle
import matplotlib.pyplot as plt
import sys

firstarg=sys.argv[1]

def inversions (alignment):
    #read sequence 1 from alignment (on line 2) from split maf file
    maf_file = open(alignment, "r").readlines()
    line1 = maf_file[-3].split() #Gets the third last value from the list and split on whitespace
    sequence1 = line1[6]
    sequence1 = sequence1.upper()
    starting_position_sequence1 = line1[2]

    #read sequence 2 from alignment (on line 3) from split maf file
    line2 = maf_file[-2].split() #Gets the second last value from the list and split on whitespace
    sequence2 = line2[6]
    sequence2 = sequence2.upper()
    starting_position_sequence2 = line2[2]

    #read alignment score (this is recorded as a XXXX on line 1 in the file)
    alignment_line = maf_file[-4].split()
    alignment_score = alignment_line[1]

    #generate list of kmers (31 in this case, but you can add smth to modify it)
    kmer_list_sequence1 = []
    for i in range(0, len(sequence1)-31):
            kmer = sequence1[i:i+31] 
            kmer_list_sequence1.append(kmer)

    kmer_list_sequence2 = []
    for i in range(0, len(sequence2)-31):
            kmer = sequence2[i:i+31] 
            kmer_list_sequence2.append(kmer)

    #generate list of unique kmers (using dictionary indexed by original index)
    unique_kmers_sequence1 = list(dict.fromkeys(kmer_list_sequence1))
    unique_kmers_sequence2 = list(dict.fromkeys(kmer_list_sequence2))

    #Identify inversions, and append their index to inversion_log
    inversion_log = []
    for i in range(0, len(kmer_list_sequence1)):
        a = kmer_list_sequence1[i]
        a = a[::-1]

        if a == kmer_list_sequence2[i]:
            inversion_log.append(i)
        done
    done

    #Create output file with the following information:
    #alignment score, number of inversions identified, and positions of inversions in seq 1 and 2
    #my bash script should have a touch command to produce this file

    f = open('inversion_output.txt', 'a')
    f.write("alignment score:\t")
    f.write(alignment_score)
    f.write("\n")
    f.write("inversion number:\t")

    inversion_number = len(inversion_log)
    f.write(str(inversion_number))
    f.write("\n")

    inversion_positions_sequence1 = []
    inversion_positions_sequence2 = []
    for i in inversion_log:
        place = int(starting_position_sequence1) + i
        inversion_positions_sequence1.append(str(place))

        place2 = int(starting_position_sequence2) + i
        inversion_positions_sequence2.append(str(place2))
    done

    f. write("kmer starting positions in sequence 1:\t")
    for i in inversion_positions_sequence1:
        f.write(i)
        f.write("\t")
    done
    f.write("\n")

    f. write("kmer starting positions in sequence 2:\t")
    for i in inversion_positions_sequence2:
        f.write(i)
        f.write("\t")
    done

    f.write("\n")

    f.close

    #produce plot (this is technically a bar graph, but the format works for my needs)

    #produce values on axes (these will be the starting positions of each kmer, given in bp)
    #to do this, I just need to add to each kmer id the starting position of the relevant sequence
    xaxis_sequence1 = []
    xaxis_sequence2 = []
    for i in range(0, len(kmer_list_sequence1)-1):
        
        position_sequence1 = i + int(starting_position_sequence1)
        xaxis_sequence1.append(position_sequence1)

        position_sequence2 = i + int(starting_position_sequence2)
        xaxis_sequence2.append(position_sequence2)
    done

    #Draw figure (the longitudinal size is helpful - maybe modify it based on how output turns out)
    fig = plt.figure(figsize=(60,3))
    ax = fig.add_subplot()

    #I'm drawing a bar graph, but I want all the bars to have the same height.
    height = []
    for i in xaxis_sequence1:
        height.append(1)
    done

    #Determine the colour of the bargraphs (to do this, I'll just use a list of colours)
    colors = []
    for i in range(0, len(kmer_list_sequence1)-1):
        if i in inversion_log:
            colors.append('r')
        else:
            colors.append('b') #this code just looks at the presence of inversions, NOT if they are unique..
            #I will test the code first then impelemnt a second if loop asking if they are unique.
    done

    #Disable y axes
    ax.get_yaxis().set_visible(False)

    #Create second x axis (for sequence 2)
    ax2 = ax.twiny()
    

    #plot bar graph
    ax.bar(xaxis_sequence1, width = 1, height = height,  color= colors)
    ax2.bar(xaxis_sequence2, width =1, height = 0)
    ax.set_xlabel("Sequence 1", fontsize=18)
    ax2.set_xlabel("Sequence 2", fontsize=18)

    #show plot
    plt.show()
    
    plt.savefig(str(alignment) + 'plot.png')

inversions(firstarg)
