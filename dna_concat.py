# Assuming the sequence is stored in a file called "sequence.fasta"
with open("sequence.fasta", "r") as file:
    lines = file.readlines()

# Skip the first line if it contains the header (e.g., >AY274119.3 ...)
sequence = "".join(line.strip() for line in lines if not line.startswith(">"))

# Print or save the continuous sequence
print(sequence)

# Optionally, save to a new file
with open("continuous_dna.txt", "w") as output_file:
    output_file.write(sequence)
