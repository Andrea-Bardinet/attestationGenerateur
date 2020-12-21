from PyPDF2 import PdfFileWriter, PdfFileReader
import io
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch

# 100px in python == 135px in inkscape.
#i don't know how to set up canvas size to work well
#setSizePage don't work as I except it to be.
#So i'm just using a function to apply a "convert"


def toPx(coord):
	return coord/1.35

def setNom(pdf,nom):
	packet = io.BytesIO()
	can = canvas.Canvas(packet)
	can.drawString(toPx(37), toPx(814), "blabla1")
	can.save()
	packet.seek(0)
	new_pdf = PdfFileReader(packet)
	pdf.mergePage(new_pdf.getPage(0))


def setPrenom(pdf,prenom):
	packet = io.BytesIO()
	can = canvas.Canvas(packet)
	can.drawString(toPx(37), toPx(814), "blabla1")
	can.save()
	packet.seek(0)
	new_pdf = PdfFileReader(packet)
	pdf.mergePage(new_pdf.getPage(0))

def setDate(pdf,jour,numero,mois,annee):
	packet = io.BytesIO()
	can = canvas.Canvas(packet)
	can.drawString(toPx(37), toPx(814), "blabla1")
	can.save()
	packet.seek(0)
	new_pdf = PdfFileReader(packet)
	pdf.mergePage(new_pdf.getPage(0))

def setHeure(pdf,heure,minute):
	packet = io.BytesIO()
	can = canvas.Canvas(packet)
	can.drawString(toPx(37), toPx(814), "blabla1")
	can.save()
	packet.seek(0)
	new_pdf = PdfFileReader(packet)
	pdf.mergePage(new_pdf.getPage(0))



pdfVide = PdfFileReader(open("attest.pdf", "rb"))
output = PdfFileWriter()


page = pdfVide.getPage(0)

setNom(page,"")


output.addPage(page)
# finally, write "output" to a real file
outputStream = open("newAttest.pdf", "wb")
output.write(outputStream)
outputStream.close()