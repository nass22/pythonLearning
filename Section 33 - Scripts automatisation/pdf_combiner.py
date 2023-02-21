# 232
# Fichiers PDF: Combiner des page

# Lire des PDF, extraire du texte
# Ecrire des PDF 
# - Combiner
# - Rotation, superposer
# - Ne peut pas rajouter du texte ou des images

""" 
from PyPDF2 import PdfFileWriter, PdfFileReader

contenu_sortie = PdfFileWriter() #création d'un pdf vide

fichier_pdf_presentation = open("presentation.pdf", "rb") #on a ajouté le b car le fichier est au format binaire
fichier_pdf_recap = open("recap.pdf", "rb")

reader_presentation = PdfFileReader(fichier_pdf_presentation)
reader_recap = PdfFileReader(fichier_pdf_recap)

print("Nombre de page du PDF: "+ str(reader_recap.getNumPages()))

contenu_sortie.addPage(reader_presentation.getPage(0))

for i in range(reader_recap.getNumPages()):
    contenu_sortie.addPage(reader_recap.getPage(i))

fichier_sortie = open("fichier_sortie.pdf", "wb")
contenu_sortie.write(fichier_sortie)

fichier_pdf_presentation.close()
fichier_pdf_recap.close()
"""

#####################################################################################

# Faire une rotation:

from PyPDF2 import PdfFileWriter, PdfFileReader

contenu_sortie = PdfFileWriter() #création d'un pdf vide

fichier_pdf_presentation = open("presentation.pdf", "rb") #on a ajouté le b car le fichier est au format binaire
fichier_pdf_recap = open("recap.pdf", "rb")

reader_presentation = PdfFileReader(fichier_pdf_presentation)
reader_recap = PdfFileReader(fichier_pdf_recap)

print("Nombre de page du PDF: "+ str(reader_recap.getNumPages()))

contenu_sortie.addPage(reader_presentation.getPage(0).rotateClockwise(90))

for i in range(reader_recap.getNumPages()):
    contenu_sortie.addPage(reader_recap.getPage(i))

fichier_sortie = open("fichier_sortie.pdf", "wb")
contenu_sortie.write(fichier_sortie)

fichier_pdf_presentation.close()
fichier_pdf_recap.close()