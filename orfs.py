# Import the sequence and alphabet toolboxes from the Biopython library
from Bio.Seq import Seq
import warnings
warnings.filterwarnings("ignore")

# Import the sequence of a bacterial DNA genome (called a plasmid) as a Seq object.
plasmodium_dna = "C:\\Users\\GrzegorzChuchra\\Documents\\GitHubSrc\\Brilliant\\Data\plasmodium.txt"
plasmid = open(plasmodium_dna).readlines()[0]
table = 1
seq = Seq(plasmid)

# Define an ORF finding function
def orf_finder(seq):
    output = []
    # The function can search the RNA sequence offset by 0, 1 or 2
    for frame in range(3): 
        # From the first frame on, the sequence is translated using the translate() method
        for pro in seq[frame:].translate(table).split("*"): 
            # If the protein is longer than 100 amino acids, and it starts with the starting codon M, record it.
            if len(pro) > 100 and pro[0] == "M": 
                output.append("%s...%s Amino Acids: %i, Frame offset: %i" \
                % (pro[:30], pro[-3:], len(pro), frame))
    return output

orfs = orf_finder(seq)

for i in range(25):
    print("ORF ",i+1, " ",orfs[i])