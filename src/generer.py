from PyPDF2 import PdfFileWriter, PdfFileReader
import datetime
import sys
import setValeur as setV
import pdfEdit


page = pdfEdit.getPage("pdf/model.pdf")

nom = sys.argv[1]
prenom = sys.argv[2]
date = sys.argv[3]
heure = sys.argv[4]
date = datetime.datetime.strptime(date+" "+heure,"%d/%m/%Y %H:%M")
outNom = sys.argv[5]


setV.setNom(page,nom)
setV.setPrenom(page,prenom)
setV.setDate(page,date)
setV.setHeure(page,date)


pdfEdit.creerPDF(outNom+".pdf",page)

