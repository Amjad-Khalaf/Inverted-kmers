#!/usr/bin/env bash

eval "$(conda shell.bash hook)" #this is to prevent the conda init error
conda activate /software/team222/ak37/miniconda3/envs/jellyfish

jellyfish count -m 31 -s 100M -t 10 -o sequence1.kmer.count $1 #31mer count for sequence 1
jellyfish count -m 31 -s 100M -t 10 -o sequence2.kmer.count $2 #31mer count for sequence 2

#make kmers readable
jellyfish dump sequence1.kmer.count > sequence1_kmer_list
jellyfish dump sequence2.kmer.count > sequence2_kmer_list 

#extract unique kmers
awk -F'>' 'NR==FNR{ids[$0]; next} NF>1{f=($2 in ids)} f' id.txt sequence1_kmer_list > sequence1_unique_kmer
awk -F'>' 'NR==FNR{ids[$0]; next} NF>1{f=($2 in ids)} f' id.txt sequence2_kmer_list > sequence2_unique_kmer

#remove fasta labels
sed -i.bak '/^>/d' sequence1_unique_kmer
sed -i.bak '/^>/d' sequence2_unique_kmer

#generate file used by python
touch structural_variation.out

#return to base environment
conda deactivate

#run python script
bsub -G team301-grp -o output.%J -e error.%J -n 18 -R"select[mem>50000] rusage[mem=50000]" -M50000 ./inversion-id.py sequence1_unique_kmer sequence2_unique_kmer $1 $2
