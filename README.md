# Identifying large inversions between two sequences (INV-ID)
<br />
This code is written to identify inversions between two submitted chromosomes. It receives chromosome 1 and uses Jellyfish2 to extract all unique 31-mers from it. Then, it checks for the presence of these unique 31-mers in the submitted chromosome 2 as matches or as inverted 31-mers. It records all of the results in a bed file which can be viewed using IGV. It also provides the option of investigating the detailed structure of any identified inversion. 
<br />
This method has the potential to outcompete alignment-based methods and other inversion-id methods available, which are less efficient, error-prone, and generally do not provide additional insight into the structure of the inversion (see last section in README.md document), but take around the same time to run.


<br />
<br />

### Identify inverted 31-mers between two genomic assemblies

Run Jellyfish on chromosome 1 to identify unique kmers:
<br />
<br />

```
jellyfish count -m 31 -s 100M -t 10 -o chromosome1.kmer.count chromosome1.fa ##-m determines kmer size, and -o determines name of output file
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

Although in theory, the script could take all the unique kmers from the chromosome 1 and test them, taking only 100k appears to be sufficient to identify large inversions.

```
shuf -n 100000 sequence1_unique_kmer > sampled_sequence1_unique_kmer
```

<br />

Then, generate the output file `touch structural_variation.out` and run the python script to identify inversions as follows:

```
./inversion-id.py sampled_sequence1_unique_kmer chromosome2.fasta chromosome_name
```

<br />

Ultimately, instead of running these steps separately, running the shell script `kmer_count.sh` will do all of this for you. By this script, the output bed file is called `structural_variation.out`

```
./kmer_count.sh chromosome1.fasta 
./inversion-id.py sampled_sequence1_unique_kmer chromosome2.fasta chromosome_name
```

<br />

In order to speed up the running process, running `./speedrun.sh` was impelemented with the option of multi-threading. The `speedrun.sh` will split the 100k kmers into smaller chunks (based on how many threads are chosen), and run `inversion-id.py` on each of them in parallel. This is slightly messy, and will require a cleanup script to be run afterwards. You may modify memory allocation or add a cluster job submission command inside `./speedrun.sh`.




```
./kmer_count.sh chromosome1.fasta
./speedrun.sh chromosome2.fasta chromosome_name thread_number
./cleanup.sh
```

<br />

### View inversion positions in IGV

If you ran `./speedrun.sh` followed by `./cleanup.sh` , you could access `inversion_list.bed` and `syn_list.bed` with the `chromosome2.fasta` file in IGV to view the positions of inverted 31-mers. A large inversion will appear as a long stretch of inverted 31-mers, with a gap in the track from `syn_list.bed` which symbolise the matching 31-mers.

<br />

If you did not run `./speedrun.sh` , and just ran `./inversion-id.py sampled_sequence1_unique_kmer chromosome2.fasta outputfile.bed chromosome_name` . From the output file, you need to separate inversions and matching 31 mers, sort each of these files respectively, and then you can view them as tracks in IGV. This can be done as follows: 

```
grep "INV" outputfile.bed  | sort -k 2n > inversion_list.bed
grep "SYN" outputfile.bed  | sort -k 2n > syn_list.bed
```


<br />

This is a sample image from IGV for what an inversion would look like. Please note, you might have to zoom in a bit for gaps in the syn track to appear. The inv track is displayed in blue, whilst the syn in red.

<img width="1165" alt="Screenshot 2022-03-01 at 09 54 19" src="https://user-images.githubusercontent.com/92156267/156146772-f78902e7-b12d-4a30-ab6d-9daf512be4d7.png">

<br />
<br />

### Observe more detailed structure of inversions identified
<br />

This method also provides additional insight into the structure of the variation, which is missed by whole-genome alignment approaches. To do this, the `kmer_status_plot.py` will receive the output file from `inversion-id.py` and go through the 31-mers from the beginning of the chromosome to its end. For each 100 31-mers, it will calculate the proportion of inverted 31-mers, and will plot this as a line graph. This approach clearly shows a large inversion if present, but it also identifies if the inversion has some non-inverted sequences like repeats (or otherwise) that are usually missed out by genome alignment approaches.

<br />

Here is an example of an inversion displayed by this plot. Smaller inversions not usually picked up by genome alignment methods are also identified.

![output](https://user-images.githubusercontent.com/92156267/156162889-7cbad62d-027c-4b05-9035-ea29c4bbf5fb.png)
 



