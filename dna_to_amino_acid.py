dna = "TCGGTGAATCTGTTTGAT"

mrna = ""

transcribe = { 
    'A' : 'U',
    'T' : 'A',
    'C' : 'G',
    'G' : 'C'
}

for base in dna : 
    mrna += transcribe[base]

amino_acid = ""

translate = {
    "UUU": 'F', "UUC": 'F',
    "UUA": 'L', "UUG": 'L',
    "UCU": 'S', "UCC": 'S', "UCA": 'S', "UCG": 'S',
    "UAU": 'Y', "UAC": 'Y',
    "UAA": ' ', "UAG": ' ',
    "UGU": 'C', "UGC": 'C',
    "UGA": ' ', "UGG": 'W',
    "CUU": 'L', "CUC": 'L', "CUA": 'L', "CUG": 'L',
    "CCU": 'P', "CCC": 'P', "CCA": 'P', "CCG": 'P',
    "CAU": 'H', "CAC": 'H',
    "CAA": 'Q', "CAG": 'Q',
    "CGU": 'R', "CGC": 'R', "CGA": 'R', "CGG": 'R',
    "AUU": 'I', "AUC": 'I', "AUA": 'I',
    "AUG": 'M',
    "ACU": 'T', "ACC": 'T', "ACA": 'T', "ACG": 'T',
    "AAU": 'N', "AAC": 'N',
    "AAA": 'K', "AAG": 'K',
    "AGU": 'S', "AGC": 'S',
    "AGA": 'R', "AGG": 'R',
    "GUU": 'V', "GUC": 'V', "GUA": 'V', "GUG": 'V',
    "GCU": 'A', "GCC": 'A', "GCA": 'A', "GCG": 'A',
    "GAU": 'D', "GAC": 'D',
    "GAA": 'E', "GAG": 'E',
    "GGU": 'G', "GGC": 'G', "GGA": 'G', "GGG": 'G'
}

len_mrna = len(mrna)
idx = 0

while(idx<=len_mrna-1) :
    if idx+2<=len_mrna-1 : 
        amino_acid += translate[mrna[idx:idx+3]]
    idx += 3

print("DNA : ", dna)
print("mRNA : ", mrna)
print("Amino Acid : ", amino_acid)

