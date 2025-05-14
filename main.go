package main

import (
	"Inverted_Kmers/fasta"
	"Inverted_Kmers/kmers"
	"fmt"
	"os"
	"strconv"
)

func printHelp() {
	fmt.Println(`Usage: program <Fasta1> <Fasta2> <k>
	Arguments:
	<Fasta1>   Path to the first FASTA file.
	<Fasta2>   Path to the second FASTA file.
	<k>        Length of k-mers.

	Example:
	Inverted_Kmers genome1.fasta genome2.fasta 21`)
}

func main() {

	if len(os.Args) == 2 && (os.Args[1] == "-h" || os.Args[1] == "--help") {
		printHelp()
		os.Exit(0)
	}

	if len(os.Args) != 4 {
		fmt.Println("Error: Incorrect number of arguments.")
		printHelp()
		os.Exit(1)
	}

	Fasta1 := os.Args[1]
	Fasta2 := os.Args[2]
	k_string := os.Args[3]

	// string to int
	k, err := strconv.Atoi(k_string)
	if err != nil || k < 0 {
		fmt.Println("Error: k must be a positive integer.")
		os.Exit(1)
	}

	// Check file existence
	if _, err := os.Stat(Fasta1); os.IsNotExist(err) {
		fmt.Printf("Error: File not found: %s\n", Fasta1)
		os.Exit(1)
	}
	if _, err := os.Stat(Fasta2); os.IsNotExist(err) {
		fmt.Printf("Error: File not found: %s\n", Fasta2)
		os.Exit(1)
	}

	Fasta1_kmer_map := make(map[string]kmers.Kmer)

	records := fasta.Read(Fasta1)
	for _, value := range records {
		Fasta1_kmer_map = kmers.KmeriseNonCanonically(value.Sequence, value.Header, k, Fasta1_kmer_map)
	}

	Fasta2_kmer_map := make(map[string]kmers.Kmer)
	records = fasta.Read(Fasta2)
	for _, value := range records {
		Fasta2_kmer_map = kmers.KmeriseNonCanonically(value.Sequence, value.Header, k, Fasta2_kmer_map)
	}

	Fasta1_unique_kmer_map := kmers.GetUniqueKmersMap(Fasta1_kmer_map)

	kmers.MapKmersBetweenSequences(Fasta1_unique_kmer_map, Fasta2_kmer_map)
}
