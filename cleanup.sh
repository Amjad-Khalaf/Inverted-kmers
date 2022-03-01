#!/usr/bin/env bash

#This is a cleanup script to tidy up the results from the speedrun.sh script

#put all results together in one file
touch total_structural_variation.out

awk '{print $0"A"}' structural_variation1.out >> total_structural_variation.out
awk '{print $0"B"}' structural_variation2.out >> total_structural_variation.out
awk '{print $0"C"}' structural_variation3.out >> total_structural_variation.out
awk '{print $0"D"}' structural_variation4.out >> total_structural_variation.out
awk '{print $0"E"}' structural_variation5.out >> total_structural_variation.out
awk '{print $0"F"}' structural_variation6.out >> total_structural_variation.out
awk '{print $0"G"}' structural_variation7.out >> total_structural_variation.out
awk '{print $0"H"}' structural_variation8.out >> total_structural_variation.out
awk '{print $0"I"}' structural_variation9.out >> total_structural_variation.out
awk '{print $0"J"}' structural_variation10.out >> total_structural_variation.out
awk '{print $0"K"}' structural_variation11.out >> total_structural_variation.out
awk '{print $0"L"}' structural_variation12.out >> total_structural_variation.out
awk '{print $0"M"}' structural_variation13.out >> total_structural_variation.out
awk '{print $0"N"}' structural_variation14.out >> total_structural_variation.out
awk '{print $0"O"}' structural_variation15.out >> total_structural_variation.out
awk '{print $0"P"}' structural_variation16.out >> total_structural_variation.out
awk '{print $0"Q"}' structural_variation17.out >> total_structural_variation.out
awk '{print $0"R"}' structural_variation18.out >> total_structural_variation.out
awk '{print $0"S"}' structural_variation19.out >> total_structural_variation.out
awk '{print $0"T"}' structural_variation14.out >> total_structural_variation.out

#clean up directory
rm structural_variation*
rm sampled_sequence1_unique_kmer_segment*
rm error*
rm output*

#sort total_structural_variation.out
sort -k 2n total_structural_variation.out > sorted_total_structural_variation.out
rm total_structural_variation.out

#extract inversions and matching kmers in separate files
grep "INV" total_structural_variation.out | sort -k 2n > inversion_list.bed
grep "SYN" total_structural_variation.out | sort -k 2n > syn_list.bed
