#!/usr/bin/env bash

#This is a script that implements multi-threading to the inversion-id script.
#This should increase running speed significantly.


#With this script, $1 is the fasta files with chromosome sequence, $2 is the chromosome name, and $3 is the number of threads/parallel processes to run.
#memory allocations could be added inside the for loop after "do".


#split 100k list into chunks with as many jobs as you can submit/threads you have
let chunk_size=100000/$3
split -l $chunk_size sampled_sequence1_unique_kmer sampled_sequence1_unique_kmer_segment

#for loop to submit job
for file in sampled_sequence1_unique_kmer_segment*; do ./inversion-id.py $file $1 $2 &
done
