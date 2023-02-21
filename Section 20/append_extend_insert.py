# 125
# Append / Extend / += / Insert

noms = ["Sabrina", "Camélia"]

noms_supplementaires = ["Naya", "Samir"]

# noms.append(noms_supplementaires)
# Output: ['Sabrina', 'Camélia', ['Naya', 'Samir']]

# noms.extend(noms_supplementaires)
# Output: ['Sabrina', 'Camélia', 'Naya', 'Samir']

# noms += noms_supplementaires
# Output: ['Sabrina', 'Camélia', 'Naya', 'Samir']

# noms.insert(0, "Naya") 
# Output: ['Naya', 'Sabrina', 'Camélia']

# noms.insert(1, "Naya")
# Output: ['Sabrina', 'Naya', 'Camélia']

# noms = noms_supplementaires + noms
# Output: ['Naya', 'Samir', 'Sabrina', 'Camélia']

noms = noms + noms_supplementaires
# Output: ['Sabrina', 'Camélia', 'Naya', 'Samir']

print(noms)

