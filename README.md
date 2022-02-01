# Identifying inversions between two sequences
<br />
The premise of the code is to identify unique 31-mers in each of the two submitted sequences. Then, for each 31-mer in sequence one, the inverted 31-mer is searched for in sequence 2 (both types of inversions: reverse, and reverse complement). If the inverted 31-mer is identified, its coordinates in sequence 2 are recorded against the coordinates in sequence 1.
<br />
<br />
The output file is designed to have the following columns:
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
This is necessary, as I need a BEDPE format for plotting. As such, I also need to identify **syntenic regions**. Since I'm not interested in these actual regions, and these are used only for the plotting software to work, I've used the following relaxed approach: if a unique 31-mer is found in both sequence 1 and 2, it is labelled as syntenic. 
<br />
<br />
Problems with the code: it is very slow. I tried to optimise it using set operations, but it's still very slow.
