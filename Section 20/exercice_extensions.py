# 136
# Extraire les extensions

definition_extensions = (
    ("exe", "Executable"),
    ("doc", "Document Word"),
    ("txt", "Document Texte"),
    ("jpeg", "Image JPEG")
)

def tuple_in_list(tuple):
    liste = []
    for elem in tuple:
        liste.append(elem)
    return liste

def new_list_extension(list):
    new_list = []
    for elem in list:
        if "." in elem:
            a = elem.split(".")
            for ext in definition_extensions:
                if a[-1].lower() == ext[0].lower():
                    new_list.append((elem + " (" +ext[1] + ")"))
        else:
            new_list.append(elem + " (Aucune extension)")
    print(new_list)
        

fichiers = ("notepad.exe", "mon.fichier.perso.doc","notes.TXT", "vacances.jpeg", "planning", "data.dat")

fichiers_list = tuple_in_list(fichiers)


new_list_extension(fichiers_list)


