#!/bin/bash
eval "$(conda shell.bash hook)" #this is to prevent the conda init error

conda activate /software/team222/ak37/miniconda3/envs/minimap2 #activate minimap environment

#produce maf alignment from 2 input sequences
/software/team222/ak37/minimap2/minimap2 --cs=long $1 $2 | /software/team222/ak37/paftools/k8 /software/team222/ak37/paftools/paftools.js view -f maf - > maf_alignment

#remove header
awk 'NR > 2' maf_alignment > adjusted_maf_alignment

#the maf alignment is organised with each small alignment in 4 line blocks
#this will split it into single files, each file with its own alignment
split -l 4 adjusted_maf_alignment split_maf/maf_a_0
