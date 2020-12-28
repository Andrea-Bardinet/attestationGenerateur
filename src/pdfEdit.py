""" operations sur les pdf """

from PyPDF2 import PdfFileWriter, PdfFileReader
import io
from reportlab.pdfgen import canvas

def getPage(chemin):
	return PdfFileReader(open(chemin, "rb")).getPage(0)

def newCanvas():
	packet = io.BytesIO()
	can = canvas.Canvas(packet)
	return [packet,can]

def setCanvas(can, dat, string):
	can.setFont(dat["font"], dat["size"])
	can.setFillColorRGB(dat["rgb"][0],dat["rgb"][1],dat["rgb"][2])
	can.drawString(dat["pos"][0], dat["pos"][1], string)

def addToPDF(pdf,can):
	can[1].save()
	can[0].seek(0)
	new_pdf = PdfFileReader(can[0])
	pdf.mergePage(new_pdf.getPage(0))

def creerPDF(chemin, page):
	output = PdfFileWriter()
	output.addPage(page)
	outputStream = open(chemin, "wb")
	output.write(outputStream)
	outputStream.close()

	