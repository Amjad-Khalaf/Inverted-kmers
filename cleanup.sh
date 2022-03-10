#!/usr/bin/env bash

#This is a cleanup script to tidy up the results from the speedrun.sh script

#put all results together in one file
touch total_list.out

#for loop

for file in *_structural_variation.out; do cat $file >> total_list.out
done


#clean up directory
rm *structural_variation.out
rm sampled_sequence1_unique_kmer_segment*
rm error*
rm output*

#sort total_structural_variation.out
sort -k 2n total_list.out > sorted_total_structural_variation.out
rm total_list.out

#extract inversions and matching kmers in separate files
grep "INV" sorted_total_structural_variation.out | sort -k 2n > inversion_list.bed
grep "SYN" sorted_total_structural_variation.out | sort -k 2n > syn_list.bed
