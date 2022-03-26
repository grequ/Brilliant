
nucleobases_code_to_name = {'A' : 'Adenine', 'C' : 'Cytosine', 'G' : 'Guanine', 'T' : 'Thymine', 'U' : 'Uracil'}

# A python dictionary data structure to translate.
t_dna_to_protein = {'ATG': 'M', 'GCG': 'A', 'TCA': 'S', 'GAA': 'E', 'GGG': 'G', 'GGT': 'G', 'AAA': 'K', 'GAG': 'E', 'AAT': 'N', 'CTA': 'L', 
                'CAT': 'H', 'TCG': 'S', 'TAG': 'STOP', 'GTG': 'V', 'TAT': 'Y', 'CCT': 'P', 'ACT': 'T', 'TCC': 's', 'CAG': 'Q', 'CCA': 'P', 
                'TAA': 'STOP', 'AGA': 'R', 'ACG': 'T', 'CAA': 'Q', 'TGT': 'C', 'GCT': 'A', 'TTC': 'F', 'AGT': 'S', 'ATA': 'I', 'TTA': 'L', 
                'CCG': 'P', 'ATC': 'I', 'TTT': 'F', 'CGT': 'R', 'TGA': 'STOP', 'GTA': 'V', 'TCT': 'S', 'CAC': 'H', 'GTT': 'V', 'GAT': 'D', 
                'CGA': 'R', 'GGA': 'G', 'GTC': 'V', 'GGC': 'G', 'TGC': 'C', 'CTG': 'L', 'CTC': 'L', 'CGC': 'R', 'CGG': 'R', 'AAC': 'N', 
                'GCC': 'A', 'ATT': 'I', 'AGG': 'R', 'GAC': 'D', 'ACC': 'T', 'AGC': 'S', 'TAC': 'Y', 'ACA': 'T', 'AAG': 'K', 'GCA': 'A', 
                'TTG': 'L', 'CCC': 'P', 'CTT': 'L', 'TGG': 'W'}
t_codne_to_protein = {'UUU': 'F', 'UUC': 'F', 'UUA': 'L', 'UUG': 'L', 'CUU': 'L', 'CUC': 'L', 'CUA': 'L', 'CUG': 'L', 'AUU': 'I', 'AUC': 'I', 
                'AUA': 'I', 'AUG': 'M', 'GUU': 'V', 'GUC': 'V', 'GUA': 'V', 'GUG': 'V', 'UCU': 'S', 'UCC': 'S', 'UCA': 'S', 'UCG': 'S', 
                'CCU': 'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P', 'ACU': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T', 'GCU': 'A', 'GCC': 'A', 
                'GCA': 'A', 'GCG': 'A', 'UAU': 'Y', 'UAC': 'Y', 'CAU': 'H', 'CAC': 'H', 'CAA': 'Q', 'CAG': 'Q', 'AAU': 'N', 'AAC': 'N', 
                'AAA': 'K', 'AAG': 'K', 'GAU': 'D', 'GAC': 'D', 'GAA': 'E', 'GAG': 'E', 'UGU': 'C', 'UGC': 'C', 'UGG': 'W', 'CGU': 'R', 
                'CGC': 'R', 'CGA': 'R', 'CGG': 'R', 'AGU': 'S', 'AGC': 'S', 'AGA': 'R', 'AGG': 'R', 'GGU': 'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G' }
codon_to_AA = {'AUG': 'M', 'GCG': 'A', 'UCA': 'S', 'GAA': 'E', 'GGG': 'G', 'GGU': 'G', 'AAA': 'K', 'GAG': 'E', 'AAU': 'N', 'CUA': 'L',
                'CAU': 'H', 'UCG': 'S', 'UAG': 'STOP', 'GUG': 'V', 'UAU': 'Y', 'CCU': 'P', 'ACU': 'T', 'UCC': 's', 'CAG': 'Q', 'CCA': 'P',
                 'UAA': 'STOP', 'AGA': 'R', 'ACG': 'T', 'CAA': 'Q', 'UGU': 'C', 'GCU': 'A', 'UUC': 'F', 'AGU': 'S', 'AUA': 'I', 'UUA': 'L', 
                 'CCG': 'P', 'AUC': 'I', 'UUU': 'F', 'CGU': 'R', 'UGA': 'STOP', 'GUA': 'V', 'UCU': 'S', 'CAC': 'H', 'GUU': 'V', 'GAU': 'D', 
                 'CGA': 'R', 'GGA': 'G', 'GUC': 'V', 'GGC': 'G', 'UGC': 'C', 'CUG': 'L', 'CUC': 'L', 'CGC': 'R', 'CGG': 'R', 'AAC': 'N', 
                 'GCC': 'A', 'AUU': 'I', 'AGG': 'R', 'GAC': 'D', 'ACC': 'T', 'AGC': 'S', 'UAC': 'Y', 'ACA': 'T', 'AAG': 'K', 'GCA': 'A', 
                 'UUG': 'L', 'CCC': 'P', 'CUU': 'L', 'UGG': 'W'}

map = {'AUG': 'M', 'GCG': 'A', 'UCA': 'S', 'GAA': 'E', 'GGG': 'G', 'GGU': 'G', 'AAA': 'K', 'GAG': 'E', 'AAU': 'N', 'CUA': 'L', 'CAU': 'H', 'UCG': 'S', 'UAG': 'STOP', 'GUG': 'V', 'UAU': 'Y', 'CCU': 'P', 'ACU': 'T', 'UCC': 's', 'CAG': 'Q', 'CCA': 'P', 'UAA': 'STOP', 'AGA': 'R', 'ACG': 'T', 'CAA': 'Q', 'UGU': 'C', 'GCU': 'A', 'UUC': 'F', 'AGU': 'S', 'AUA': 'I', 'UUA': 'L', 'CCG': 'P', 'AUC': 'I', 'UUU': 'F', 'CGU': 'R', 'UGA': 'STOP', 'GUA': 'V', 'UCU': 'S', 'CAC': 'H', 'GUU': 'V', 'GAU': 'D', 'CGA': 'R', 'GGA': 'G', 'GUC': 'V', 'GGC': 'G', 'UGC': 'C', 'CUG': 'L', 'CUC': 'L', 'CGC': 'R', 'CGG': 'R', 'AAC': 'N', 'GCC': 'A', 'AUU': 'I', 'AGG': 'R', 'GAC': 'D', 'ACC': 'T', 'AGC': 'S', 'UAC': 'Y', 'ACA': 'T', 'AAG': 'K', 'GCA': 'A', 'UUG': 'L', 'CCC': 'P', 'CUU': 'L', 'UGG': 'W'}


t_dna_links = {'A': 'T', 'T':'A', 
            'G': 'C', 'C' : 'G'}

t_mRNA_to_dna_link = {'A': 'U', 'T':'A', 
            'G': 'C', 'C' : 'G', 'U' : 'A'}

# 1. Generate a complementary DNA sequence just in case the gene is encoded on the complementary strand
# https://brilliant.org/practice/introduction-transcription-and-translation/?p=7
def complement(seq):
    comp_seq=""
    # Find complement sequence.
    for nucleobase in seq:
        comp_seq += t_dna_links[nucleobase]
     
    return comp_seq;

# 2. Reverse the direction
# https://brilliant.org/practice/introduction-transcription-and-translation/?p=7
def reverse_complement(seq):
    return seq[::-1]

# 3. Find which strand has a TATA box promoter (the coding strand).
# https://brilliant.org/practice/introduction-transcription-and-translation/?p=7
def is5to3Strand(seq) :
    if (seq.find("TATAAAA") == -1) :
        return 0
    else:
        return 1

# 4. Perform a T > U substitution
# https://brilliant.org/practice/introduction-transcription-and-translation/?p=7
def DNA_to_mRNA (dna):
    l_mRNA = ""

    for nucleobase in dna:
        l_mRNA += t_mRNA_to_dna_link[nucleobase]
 
    return l_mRNA

def mRNA_to_tRNA (mRNA) :
    l_tRNA = ""
    
    for nucleobase in mRNA :
        l_tRNA += t_mRNA_to_dna_link[nucleobase]
    
    return l_tRNA

def codone_from_mRNA (mRNA) :
    return ""


# A function that translates DNA into a protein sequence.
def DNA_to_Protein(a_dna):
    l_protein = []
    l_start = 0
    # Step through the DNA sequence and translate.
    while l_start + 2 < len(a_dna):
        codon = a_dna[l_start:l_start + 3]
        l_protein.append(t_dna_to_protein[codon])
        l_start += 3
    return ''.join(l_protein)


# A function that translates mRNA into a protein sequence.
def mRNA_to_Protein(a_mRNA):
    l_protein = []
    l_start = 0

    while l_start + 2 < len(a_mRNA):
        codon = a_mRNA[l_start:l_start + 3]         ## G: i don't think that here we have codon? Probobly anycodoe as the codon is in the faction above 
        l_protein.append(t_codne_to_protein[codon])   
        l_start += 3
    return ''.join(l_protein)

def translate(rna):
    # Modify the function here.
    # Read the RNA sequence codon-by-codon and write the string "protein" according to the genetic code dict.
    protein=[]
    
    l_start = 0

    while l_start + 2 < len(rna):
        codon = rna[l_start:l_start + 3]         ## G: i don't think that here we have codon? Probobly anycodoe as the codon is in the faction above 
        currentProtein = codon_to_AA[codon]
        if currentProtein == "STOP":
            return ''.join(protein)
        else :
            protein.append(currentProtein)   
        l_start += 3
    return ''.join(protein)

def translate1(RNA):
    protein = []
    ## Find the start codon in the RNA sequence.
    start = RNA.find('AUG')
    ## Proceed forwards in the sequence until the end.
    while start+2 < len(RNA):
        ## Read in the next codon.
        codon = RNA[start:start+3]
        ## Break if the codon is a stop codon.
        if map[codon]=="STOP": 
            print("STOPPED!")
            break
        ## Add the translated codon to the end of the protein string.
        protein.append(map[codon])
        start+=3
    return ''.join(protein)

gene = "TCAGACTGGTGCCGTGGTGCTCTCGCCCGATGTGACGTCGACCGCCAGCGGCGCGATGACGCCGAGGATTTCCGTGATCGTTTCGGAGGGCACGCCGGCTGCGGTCAGCGCGTCGGCCAAGTGTCCGGCGACCAGGCTGAAGTGGTGCATGGTAATTCCGCGCCCCTGATGGACTTGCTTCATCGGCGCACCGGTATAGGGCTCGGGCCCGCCAAGCGCGGCCGCGAAAAACTCCACCTGCTTGCCCTTGAGGCGGCTCATGTTCGTACCGCTGAAGAAGGCCGATAGTTGGTCATCGGCAAGCACACGAACATAGAAGTCCTCGACGACGACTTCGATGGCCTCATGCCCGCCGATCTTGTCGTAGATGCTGATCGGCTCACGTTTGCGCAAGCGTGACAGTAGTCCCATTTTTATA"
gdh = 'AUGGAUCAGACAUAUUCUCUGGAGUCAUUCCUCAACCAUGUCCAAAAGCGCGACCCGAAUCAAACCGAGUUCGCGCAAGCCGUUCGUGAAGUAAUGACCACACUCUGGCCUUUUCUUGAACAAAAUCCAAAAUAUCGCCAGAUGUCAUUACUGGAGCGUCUGGUUGAACCGGAGCGCGUGAUCCAGUUUCGCGUGGUAUGGGUUGAUGAUCGCAACCAGAUACAGGUCAACCGUGCAUGGCGUGUGCAGUUCAGCUCUGCCAUCGGCCCGUACAAAGGCGGUAUGCGCUUCCAUCCGUCAGUUAACCUUUCCAUUCUCAAAUUCCUCGGCUUUGAACAAACCUUCAAAAAUGCCCUGACUACUCUGCCGAUGGGCGGUGGUAAAGGCGGCAGCGAUUUCGAUCCGAAAGGAAAAAGCGAAGGUGAAGUGAUGCGUUUUUGCCAGGCGCUGAUGACUGAACUGUAUCGCCACCUGGGCGCGGAUACCGACGUUCCGGCAGGUGAUAUCGGGGUUGGUGGUCGUGAAGUCGGCUUUAUGGCGGGGAUGAUGAAAAAGCUCUCCAACAAUACCGCCUGCGUCUUCACCGGUAAGGGCCUUUCAUUUGGCGGCAGUCUUAUUCGCCCGGAAGCUACCGGCUACGGUCUGGUUUAUUUCACAGAAGCAAUGCUAAAACGCCACGGUAUGGGUUUUGAAGGGAUGCGCGUUUCCGUUUCUGGCUCCGGCAACGUCGCCCAGUACGCUAUCGAAAAAGCGAUGGAAUUUGGUGCUCGUGUGAUCACUGCGUCAGACUCCAGCGGCACUGUAGUUGAUGAAAGCGGAUUCACGAAAGAGAAACUGGCACGUCUUAUCGAAAUCAAAGCCAGCCGCGAUGGUCGAGUGGCAGAUUACGCCAAAGAAUUUGGUCUGGUCUAUCUCGAAGGCCAACAGCCGUGGUCUCUACCGGUUGAUAUCGCCCUGCCUUGCGCCACCCAGAAUGAACUGGAUGUUGACGCCGCGCAUCAGCUUAUCGCUAAUGGCGUUAAAGCCGUCGCCGAAGGGGCAAAUAUGCCGACCACCAUCGAAGCGACUGAACUGUUCCAGCAGGCAGGCGUACUAUUUGCACCGGGUAAAGCGGCUAAUGCUGGUGGCGUCGCUACAUCGGGCCUGGAAAUGGCACAAAACGCUGCGCGCCUGGGCUGGAAAGCCGAGAAAGUUGACGCACGUUUGCAUCACAUCAUGCUGGAUAUCCACCAUGCCUGUGUUGAGCAUGGUGGUGAAGGUGAGCAAACCAACUACGUGCAGGGCGCGAACAUUGCCGGUUUUGUGAAGGUUGCCGAUGCGAUGCUGGCGCAGGGUGUGAUUUAA'

print (translate(gdh))
print (translate1(gdh))
com_gene = complement(gene)
# print(com_gene)
# print(is5to3Strand(com_gene))
rev_gene = reverse_complement(com_gene)
print(rev_gene)
print(is5to3Strand(rev_gene))
mRNA = DNA_to_mRNA(rev_gene)
print ('The DNA:  ' + rev_gene + ' has following mRNA: ' + mRNA)


# DNA = 'TACGGAGATCAT'
# mRNA = DNA_to_mRNA(DNA)
# tRNA = mRNA_to_tRNA(mRNA)
# protein_from_DNA = DNA_to_Protein(DNA)
# protein_from_mRNA = mRNA_to_Protein(mRNA)
# print ('The DNA:  ' + DNA + ' has following mRNA: ' + mRNA)
# print ('The DNA:  ' + DNA + ' has following protein: ' + protein_from_DNA)
# print ('The mRNA:  ' + mRNA + ' has following tRNA: ' + tRNA)
# print ('The mRNA:  ' + mRNA + ' has following protein: ' + protein_from_mRNA)

# seq1 = DNA_to_mRNA('AAACTTGAATAAACGTAACGACGGTTGCTAACGCGTTAGTGCCGCGCCCTCAGCTATAATGACATG')
# seq2 = mRNA_to_Protein(seq1)
# print (seq1)
# print (seq2)


# print ('The mRNA: ' + DNA_to_mRNA(DNA) + ' has following tRNA: ' + tDNA_from_mRNA(DNA_to_mRNA(DNA)))