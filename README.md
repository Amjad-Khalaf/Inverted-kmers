# Identifying large inversions between two sequences (INV-ID)
<br />
This code receives a reference chromosome, and uses Jellyfish2 to extract all unique kmers from it. Then, it checks for the presence of these unique kmers in a submitted query chromosome as matches or as inverted kmers. It records all of the results in a bed file which can be viewed using IGV.
<br />
<br />
Run Jellyfish on reference chromosome to identify unique kmers:
<br />
<br />

```
jellyfish count -m 31 -s 100M -t 10 -o reference.kmer.count reference_chromosome.fa ##-m determines kmer size, and -o determines name of output file
jellyfish dump sequence1.kmer.count > sequence1_kmer_list ##this command makes the output file human-readable
```
<br />
<br />

From the kmer list, to extract unique kmers `vi` a text file called ` id.txt ` with `1` as its only content. Then carry out the following commands:

```
awk -F'>' 'NR==FNR{ids[$0]; next} NF>1{f=($2 in ids)} f' id.txt sequence1_kmer_list > sequence1_unique_kmer
sed -i.bak '/^>/d' sequence1_unique_kmer #remove fasta labels from kmer list
```

<br />

Although in theory, the script could take all the unique kmers from the reference and test them, taking only 100k appears to be sufficient to identify large inversions.

```
shuf -n 100000 sequence1_unique_kmer > sampled_sequence1_unique_kmer
```

<br />

Then, generate the output file `touch structural_variation.out` and run the python script to identify inversions as follows:

```
./inversion-id.py sampled_sequence1_unique_kmer query_chromosome.fasta outputfile.bed chromosome_name
```

<br />

Ultimately, instead of running these steps separately, running the shell script `kmer_count.sh` will do all of this for you. By this script, the output bed file is called `structural_variation.out`

```
./kmer_count.sh reference.fasta 
./inversion-id.py sampled_sequence1_unique_kmer query_chromosome.fasta structural_variation.out chromosome_name
```

<br />
I generated a script to speed up the process temporarily, as I work on on optimising the python approach itself. The `speedrun.sh` will split the 100k kmers into chunks of 5kmers, and run `inversion-id.py` on each of them in parallel. This is slightly messy, and will require a cleanup script to be run afterwards.

<br />



```
./kmer_count.sh reference.fasta
./speedrun.sh query_chromosome.fasta chromosome_name
./cleanup.sh
```
