# 133
# Any, all

noms = ["Sabrina", "Camélia", "Naya", "Samir"]

a = [True, True, True, False]
# print(any(a))
# any return true si au moins un élément est True
# Output: True

# print(all(a))
# all return False car il faut que tous les éléments soient True
# Output: False

# noms_avec_un_s = [True if "s" in nom.lower() else False for nom in noms]
# print(noms_avec_un_s)
# Output: [True, False, False, True]

# noms_avec_un_s_any = any([True if "s" in nom.lower() else False for nom in noms])
# print(noms_avec_un_s_any)
# Output: True
# Return True car au moins un nom dans la liste possède un "s"

# noms_avec_un_s_all = all([True if "s" in nom.lower() else False for nom in noms])
# print(noms_avec_un_s_all)
# Output: False
# Return False car "s" n'est pas présent dans tous les noms de la liste


