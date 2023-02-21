# 129
# Swapper 2 éléments

noms = ["Sabrina", "Camélia", "Naya", "Samir"]

# noms[0] = noms[3]
# Output: ['Samir', 'Camélia', 'Naya', 'Samir']

noms[0], noms[3] = noms[3], noms[0]
# Output: ['Samir', 'Camélia', 'Naya', 'Sabrina']

print(noms)