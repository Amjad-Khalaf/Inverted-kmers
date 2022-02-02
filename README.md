# Identifying inversions between two sequences
<br />
The premise of the code is to identify unique 31-mers in each of the two submitted sequences. Then, for each 31-mer in sequence one, the inverted 31-mer is searched for in sequence 2 (both types of inversions: reverse, and reverse complement). If the inverted 31-mer is identified, its coordinates in sequence 2 are recorded against the coordinates in sequence 1.
<br />
<br />
The output file is designed to have the following columns:
<br />
<br />

```
Reference chromosome name
Reference start position
Reference end position
Query chromosome name
Query start position
Query end position
Annotation type
```

<br />
