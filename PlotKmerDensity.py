import sys
import numpy as np
import matplotlib.pyplot as plt

# Default parameters
DEFAULT_CHUNK_SIZE = 100
DEFAULT_WINDOW_SIZE = 70

# Help and argument parsing
def print_help():
    print(f"Usage: {sys.argv[0]} <bed_file> [chunk_size] [window_size]")
    print("  <bed_file>: Path to BED file containing kmer match status")
    print(f"  [chunk_size]: (Optional) Number of kmers per bin (default: {DEFAULT_CHUNK_SIZE})")
    print(f"  [window_size]: (Optional) Smoothing window size (default: {DEFAULT_WINDOW_SIZE})")

if len(sys.argv) < 2 or len(sys.argv) > 4 or sys.argv[1] in ("-h", "--help"):
    print_help()
    sys.exit(1)

bed_file = sys.argv[1]
try:
    chunk_size = int(sys.argv[2]) if len(sys.argv) >= 3 else DEFAULT_CHUNK_SIZE
    window_size = int(sys.argv[3]) if len(sys.argv) == 4 else DEFAULT_WINDOW_SIZE
except ValueError:
    print("Error: chunk_size and window_size must be integers.")
    sys.exit(1)


contig_dict = {}
with open(bed_file) as file:
    for line in file:
        line = line.rstrip("\n")
        fields = line.split("\t")
        contig = fields[0]
        start = fields[1]
        end = fields[2]
        status = fields[3]
        kmer = fields[4]
        if contig in contig_dict.keys():
            contig_dict[contig].append([start, status])
        else:
            contig_dict[contig] = [start, status]

for contig in contig_dict.keys():
    contig_dict[contig].sort(key=lambda x: x[0])
    contig_dict[contig] = [x[1] for x in contig_dict[contig]]


for contig, status_list in contig_dict.items():
    chunked = [status_list[i:i + chunk_size] for i in range(0, len(status_list), chunk_size)]
    inv_counts = [chunk.count("INVERTED") for chunk in chunked]
    x_axis = np.arange(len(inv_counts))

    # Smooth with moving average
    smoothed = np.convolve(inv_counts, np.ones(window_size)/window_size, mode='valid')

    plt.figure(figsize=(15, 4))
    plt.plot(x_axis[:len(smoothed)], smoothed, color='darkgreen')
    plt.title(f"Inverted kmer density - {contig}")
    plt.xlabel(f"Bins of {chunk_size} kmers along sequence")
    plt.ylabel("Number of inverted kmers in bin")
    plt.ylim(0, chunk_size+10)
    plt.grid(True)
    plt.tight_layout()
    output_file = contig + ".png"
    plt.savefig(output_file)