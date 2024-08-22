with open("continuous_dna.txt", "r") as file:
    dna = file.readline()

mrna = ""

transcribe = { 
    'A' : 'U',
    'T' : 'A',
    'C' : 'G',
    'G' : 'C'
}

for base in dna : 
    mrna += transcribe[base]

with open("continuous_mrna.txt", "w") as file_out :
    file_out.write(mrna)

