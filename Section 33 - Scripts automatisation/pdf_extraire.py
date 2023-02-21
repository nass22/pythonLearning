# 233
# Fichiers PDF: Extraire le texte

from PyPDF2 import PdfFileReader, PdfFileWriter

f = open("recap.pdf", "rb")

reader = PdfFileReader(f)
page0 = reader.getPage(1)
texte = page0.extractText()
texte = texte.replace("Ò","\"").replace("‘", "è").replace("”", "é").replace("’","ê")

f.close()

print(texte)