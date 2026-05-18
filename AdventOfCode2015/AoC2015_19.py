with open("AoC2015_19_data.txt", "r") as file:
    data = file.read()
replacements,molecule = data.split('\n\n')
replacements = replacements.split('\n')

ans = [0,0]

new_molecules = set()
reverse_replacements = []


for rep in replacements:
    inp,out = rep.split(' => ')
    reverse_replacements.append((out, inp))
    # Find all start indices of occurrences
    indices = []
    start = 0
    while True:
        idx = molecule.find(inp, start)
        if idx == -1:
            break
        indices.append(idx)
        start = idx + 1
    
    # Generate all strings with just one replacement
    for idx in indices:
        new_molecule = molecule[:idx] + out + molecule[idx + len(inp):]
        new_molecules.add(new_molecule)


steps = 0
while molecule != 'e':
    for out, inp in reverse_replacements:
        if out in molecule:
            molecule = molecule.replace(out, inp, 1)  # replace only first occurrence
            steps += 1
            break

ans[1]=steps


ans[0]=len(new_molecules)
print(ans)