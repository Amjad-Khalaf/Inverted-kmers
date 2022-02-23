#!/usr/bin/env bash

#this is a script to speed up the python inversion-id script
#the premise is to break the 100k sampled unique kmers from the reference into lists of 5k kmers
#then run the python script on each of those sublists, finally merging the results together
#this speeds up the script around 10 times

#split 100k list into 5k chunks
split -l 5000 sampled_sequence1_unique_kmer sampled_sequence1_unique_kmer_segment

#create different output files for each python run
touch structural_variation{1..20}.out

#run python script on each segment
bsub -G team301-grp -o output.%J -e error.%J -n 30 -R"select[mem>80000] rusage[mem=80000]" -M80000 "./inversion-id.py sampled_sequence1_unique_kmer_segmentaa $1 structural_variation1.out $2" #1
bsub -G team301-grp -o output.%J -e error.%J -n 30 -R"select[mem>80000] rusage[mem=80000]" -M80000 "./inversion-id.py sampled_sequence1_unique_kmer_segmentab $1 structural_variation2.out $2" #2
bsub -G team301-grp -o output.%J -e error.%J -n 30 -R"select[mem>80000] rusage[mem=80000]" -M80000 "./inversion-id.py sampled_sequence1_unique_kmer_segmentac $1 structural_variation3.out $2" #3
bsub -G team301-grp -o output.%J -e error.%J -n 30 -R"select[mem>80000] rusage[mem=80000]" -M80000 "./inversion-id.py sampled_sequence1_unique_kmer_segmentad $1 structural_variation4.out $2" #4 
bsub -G team301-grp -o output.%J -e error.%J -n 30 -R"select[mem>80000] rusage[mem=80000]" -M80000 "./inversion-id.py sampled_sequence1_unique_kmer_segmentae $1 structural_variation5.out $2" #5
bsub -G team301-grp -o output.%J -e error.%J -n 30 -R"select[mem>80000] rusage[mem=80000]" -M80000 "./inversion-id.py sampled_sequence1_unique_kmer_segmentaf $1 structural_variation6.out $2" #6
bsub -G team301-grp -o output.%J -e error.%J -n 30 -R"select[mem>80000] rusage[mem=80000]" -M80000 "./inversion-id.py sampled_sequence1_unique_kmer_segmentag $1 structural_variation7.out $2" #7
bsub -G team301-grp -o output.%J -e error.%J -n 30 -R"select[mem>80000] rusage[mem=80000]" -M80000 "./inversion-id.py sampled_sequence1_unique_kmer_segmentah $1 structural_variation8.out $2" #8
bsub -G team301-grp -o output.%J -e error.%J -n 30 -R"select[mem>80000] rusage[mem=80000]" -M80000 "./inversion-id.py sampled_sequence1_unique_kmer_segmentai $1 structural_variation9.out $2" #9
bsub -G team301-grp -o output.%J -e error.%J -n 30 -R"select[mem>80000] rusage[mem=80000]" -M80000 "./inversion-id.py sampled_sequence1_unique_kmer_segmentaj $1 structural_variation10.out $2" #10
bsub -G team301-grp -o output.%J -e error.%J -n 30 -R"select[mem>80000] rusage[mem=80000]" -M80000 "./inversion-id.py sampled_sequence1_unique_kmer_segmentak $1 structural_variation11.out $2" #11
bsub -G team301-grp -o output.%J -e error.%J -n 30 -R"select[mem>80000] rusage[mem=80000]" -M80000 "./inversion-id.py sampled_sequence1_unique_kmer_segmental $1 structural_variation12.out $2" #12
bsub -G team301-grp -o output.%J -e error.%J -n 30 -R"select[mem>80000] rusage[mem=80000]" -M80000 "./inversion-id.py sampled_sequence1_unique_kmer_segmentam $1 structural_variation13.out $2" #13
bsub -G team301-grp -o output.%J -e error.%J -n 30 -R"select[mem>80000] rusage[mem=80000]" -M80000 "./inversion-id.py sampled_sequence1_unique_kmer_segmentan $1 structural_variation14.out $2" #14
bsub -G team301-grp -o output.%J -e error.%J -n 30 -R"select[mem>80000] rusage[mem=80000]" -M80000 "./inversion-id.py sampled_sequence1_unique_kmer_segmentao $1 structural_variation15.out $2" #15
bsub -G team301-grp -o output.%J -e error.%J -n 30 -R"select[mem>80000] rusage[mem=80000]" -M80000 "./inversion-id.py sampled_sequence1_unique_kmer_segmentap $1 structural_variation16.out $2" #16
bsub -G team301-grp -o output.%J -e error.%J -n 30 -R"select[mem>80000] rusage[mem=80000]" -M80000 "./inversion-id.py sampled_sequence1_unique_kmer_segmentaq $1 structural_variation17.out $2" #17
bsub -G team301-grp -o output.%J -e error.%J -n 30 -R"select[mem>80000] rusage[mem=80000]" -M80000 "./inversion-id.py sampled_sequence1_unique_kmer_segmentar $1 structural_variation18.out $2" #18
bsub -G team301-grp -o output.%J -e error.%J -n 30 -R"select[mem>80000] rusage[mem=80000]" -M80000 "./inversion-id.py sampled_sequence1_unique_kmer_segmentas $1 structural_variation19.out $2" #19
bsub -G team301-grp -o output.%J -e error.%J -n 30 -R"select[mem>80000] rusage[mem=80000]" -M80000 "./inversion-id.py sampled_sequence1_unique_kmer_segmentat $1 structural_variation20.out $2" #20
