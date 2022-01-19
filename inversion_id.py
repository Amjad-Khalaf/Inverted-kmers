from textwrap import indent

b = open("/lustre/scratch123/tol/projects/badass/users/ak37/pangenome/gambiae/colour_inversions/fasta_split/split_maf/maf_a_0aa", "r").readlines()
line1 = b[-3].split() #Gets the second last value from the list and split on whitespace
sequence1 = line1[6]
sequence1 = sequence1.upper()

line2 = b[-2].split() #Gets the second last value from the list and split on whitespace
sequence2 = line2[6]
sequence2 = sequence2.upper()

print("You've recorded sequence 1 and 2 successfully!")

kmer_list = []

for i in range(0, len(sequence1)-31):
        kmer = sequence1[i:i+31] #here, I'm looking at kmers of 31
        kmer_list.append(kmer)
        #print(kmer)


sequence2_kmer_list = []
for i in range(0, len(sequence2)-31):
        kmer = sequence2[i:i+31] #here, I'm looking at kmers of 31
        sequence2_kmer_list.append(kmer)
        #print(kmer)

print(sequence2_kmer_list[1])
print(kmer_list[1])

inverted_kmers = []
for i in kmer_list:
    a = i[::-1]
    inverted_kmers.append(a) #this produces inverted unique kmers and appends them to the list.

for i in range(0, len(inverted_kmers)):
    if inverted_kmers[i] == sequence2_kmer_list[i]:
        print("inversion identified at index ", i)
