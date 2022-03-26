
# Input sequence
test_sequence = "ACAACATACAAAGGGCCACAGATACATCAAAAAATGCTCAACATCACTATTTGTCAGGGAAGTACTAATTAAAACCAAAATGAGATGTCCCCTCAAACCTGTTAGAATGGCTATTATCAAAAAGATGAAAGATAGCAACTATCAGAGAGGATGATAGAAAAGGGAACCCTTGCATCATGTACAAATTAAAAATAGAACTATCACATGATCCAAGAATCCTACTTCTGGGTATATAGCCAAAGGAATTGAAATCAATATGTCAAAGGGATATCTGCACTCCTATGTTATTGCAGCATGTTCACAATGGCCAAGATATAGAATCAACCTAACTGTTCATAGACAGATGAATGGATAAATGAAATGTGATATGGAAAATTATTCAGCCTTAAAAACAGTAGGAAATTCTGTCATTTGAGACAACGTGGATGAACCTAGAGGACATTAAGCTAAGTGAAATAAGCTAGACACAGAAAGACAAATATTGCATGATCTCACTTAGAATCTAAAAAATCTGAACTCATAGAAGCAGAGAATAGTATGATGGTTACTAGGGTTATCTGGCAGGGAGAGGATGAGGAAATGGGACATTGTTAATAAAAGGAAAAAAATTCAATTAGTAGG"

def nucleotides_counter_from_table(sequence):
    adenosines = 0
    guanines = 0
    thymines = 0
    cytosines = 0

    for base in sequence:
        for nucleotide in base:
            if nucleotide == "A":
                adenosines = adenosines + 1
            elif nucleotide == "G":
                guanines = guanines + 1
            elif nucleotide == "T":
                thymines = thymines + 1
            elif nucleotide == "C":
                cytosines = cytosines + 1

    return {"adenosine" : adenosines, "thymine" : thymines,
            "cytosine" : cytosines, "guanine" : guanines}

def nucleotides_counter(sequence):
    adenosines = 0
    guanines = 0
    thymines = 0
    cytosines = 0

    for nucleotide in sequence:
        if nucleotide == "A":
            adenosines = adenosines + 1
        elif nucleotide == "G":
            guanines = guanines + 1
        elif nucleotide == "T":
            thymines = thymines + 1
        elif nucleotide == "C":
            cytosines = cytosines + 1

    return {"adenosine" : adenosines, "thymine" : thymines,
            "cytosine" : cytosines, "guanine" : guanines}

# Print your result.
human_dna = "C:\\Users\\GrzegorzChuchra\\Documents\\GitHubSrc\\Brilliant\\Data\human.txt"
mosquito_dna = "C:\\Users\\GrzegorzChuchra\\Documents\\GitHubSrc\\Brilliant\\Data\mosquito.txt"
plasmodium_dna = "C:\\Users\\GrzegorzChuchra\\Documents\\GitHubSrc\\Brilliant\\Data\plasmodium.txt"

print("human genmom: ")
print(nucleotides_counter_from_table(open(human_dna).readlines()))
print("\n mosquito genmom: ")
print(nucleotides_counter_from_table(open(mosquito_dna).readlines()))
print("\n plasmodium genmom: ")
print(nucleotides_counter_from_table(open(plasmodium_dna).readlines()))
# print(nucleotides_counter(test_sequence))


