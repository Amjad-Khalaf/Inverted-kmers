# Identifying large inversions between two sequences

<div align="justify">
 
I've rewritten this tool in `Go` to identify inversions between two fasta files. It receives two genomes, kmerises them non-canonically, identifies the unique kmers in genome 1, and generates a bed file with the location of those kmers and whether they're syntenic or inverted in genome 2. The premise is identical to v1.0, but now doesn't rely on Jellyfish, and the process is more streamlined with fewer steps. A `python` script is also supplied, which visualises inverted kmer density in each sequence/contig/chromosome in genome 2.

## Installation

<div align="justify">
  
Installation is simple. Clone this repository, `cd` into it, and run `go build`. You need Go installed to do this -- see https://go.dev/doc/install.

For running the `Python` script, you need a virtual environment with `Python3` and the following installed.


```
sys
numpy
matplotlib
```

## Quick! How do I use it?!

<div align="justify">

```
Usage: Inverted_Kmers Fasta1 Fasta2 k > OutputBedFile
       Arguments:
      	<Fasta1>   Path to the first FASTA file.
      	<Fasta2>   Path to the second FASTA file.
      	<k>        Length of k-mers.

	Example:
	Inverted_Kmers genome1.fasta genome2.fasta 21
```

Here's a snippet of an output bed file:

```
X       25546615   25546646   INVERTED   GTCTACTAGCACTCTGGAAGTTTGTACCATT
X       7473502    7473533    SYNTENIC   AAGAGCTCAATTCAAGCACTGATTACGATGC
X       4559038    4559069    SYNTENIC   GTTAAAGTCAGTGAAGAATAAAAAAAGAACA
```

Once you have an `OutputBedFile`, you can run the plotting script as follows. As in the previous version, it sorts kmers identified by their position along each sequence/contig/chromosome, generates bins of 100 kmers, and plots inverted kmer density. A plot will be generated for each sequence/contig/chromosome, with the name `{sequence}.png`.

```
Usage: python PlotKmerDensity.py OutputBedFile [chunk_size] [window_size]
       Arguments:
       <bed_file>: Path to BED file containing kmer match status
       [chunk_size]: (Optional) Number of kmers per bin (default: 100)
       [window_size]: (Optional) Smoothing window size (default: 70)
```

![X](https://github.com/user-attachments/assets/ae3b0fc4-cd67-4b86-a9ad-58d2fe423b36)


You may be able to still use the bed file to have a look with IGV (although you may need to tweak this a bit -- I haven't tested the latest version). This is a sample image from IGV for what an inversion would look like. Please note, you might have to zoom in a bit for gaps in the syntenic kmer track to appear. The inverted kmer track is displayed in blue, whilst the syntenic kmer in red.

<img width="1165" alt="Screenshot 2022-03-01 at 09 54 19" src="https://user-images.githubusercontent.com/92156267/156146772-f78902e7-b12d-4a30-ab6d-9daf512be4d7.png">

</div>
