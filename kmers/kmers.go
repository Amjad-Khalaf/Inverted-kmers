package kmers

import "fmt"

type Kmer struct {
	Count     int
	Positions []int
	Locations []string //names of the sequences this kmer appears in
}

func ReverseComplement(sequence string) string {
	complement := map[rune]rune{'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}
	reverse_complement_sequence := make([]rune, len(sequence))
	for i, base := range sequence {
		reverse_complement_sequence[len(sequence)-1-i] = complement[base]
	}
	return string(reverse_complement_sequence)
}

func KmeriseNonCanonically(sequence string, sequence_name string, k int, kmer_map map[string]Kmer) map[string]Kmer {
	var i int
	for i <= len(sequence)-k {
		kmer := sequence[i : i+k]
		info := kmer_map[kmer]
		info.Count++
		info.Positions = append(info.Positions, i)
		info.Locations = append(info.Locations, sequence_name)
		kmer_map[kmer] = info
		i += 1
	}
	return kmer_map
}

func GetUniqueKmersMap(kmer_map map[string]Kmer) map[string]Kmer {
	unique_kmer_map := make(map[string]Kmer)
	for key, value := range kmer_map {
		if value.Count == 1 {
			info := unique_kmer_map[key]
			info.Count = 1
			info.Positions = append(info.Positions, value.Positions[0])
			info.Locations = append(info.Locations, value.Locations[0])
			unique_kmer_map[key] = info
		}
	}
	return unique_kmer_map
}

func MapKmersBetweenSequences(sequence1_kmer_map map[string]Kmer, sequence2_kmer_map map[string]Kmer) {
	for kmer, _ := range sequence1_kmer_map {
		for index, position := range sequence2_kmer_map[kmer].Positions {
			fmt.Printf("%s\t%d\t%d\t%s\t%s\n", sequence2_kmer_map[kmer].Locations[index], position, position+len(kmer), "SYNTENIC", kmer)
		}
		rckmer := ReverseComplement(kmer)
		for index, position := range sequence2_kmer_map[rckmer].Positions {
			fmt.Printf("%s\t%d\t%d\t%s\t%s\n", sequence2_kmer_map[rckmer].Locations[index], position, position+len(rckmer), "INVERTED", kmer)
		}
	}
}
