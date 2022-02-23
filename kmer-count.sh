#!/usr/bin/env bash
#This script extracts unique kmers from a reference chromosome submitted using Jellyfish2

eval "$(conda shell.bash hook)" #this is to prevent the conda init error
conda activate /software/team222/ak37/miniconda3/envs/jellyfish

jellyfish count -m 31 -s 100M -t 10 -o sequence1.kmer.count $1 #31mer count for sequence 1

#make kmers readable
jellyfish dump sequence1.kmer.count > sequence1_kmer_list

#extract unique kmers
awk -F'>' 'NR==FNR{ids[$0]; next} NF>1{f=($2 in ids)} f' id.txt sequence1_kmer_list > sequence1_unique_kmer

#remove fasta labels
sed -i.bak '/^>/d' sequence1_unique_kmer

#generate file used by python
touch structural_variation.out

#sample 100k 31-mers from sequence 1
shuf -n 100000 sequence1_unique_kmer > sampled_sequence1_unique_kmer
