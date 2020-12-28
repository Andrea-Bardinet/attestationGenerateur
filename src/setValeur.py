"""  fonctions de set """

import data
import pdfEdit
import datetime


def setNom(pdf,nom):
	dat = data.nom
	can = pdfEdit.newCanvas()
	nom = nom.upper()
	pdfEdit.setCanvas(can[1],dat,nom)
	pdfEdit.addToPDF(pdf,can)

def setPrenom(pdf,prenom):
	dat = data.prenom
	can = pdfEdit.newCanvas()
	prenom = prenom.capitalize()
	pdfEdit.setCanvas(can[1],dat,prenom)
	pdfEdit.addToPDF(pdf,can)

def setDate(pdf,date):
	dat = data.date
	can = pdfEdit.newCanvas()
	date = data.jours[date.weekday()]+" "+str(date.day)+" "+data.mois[date.month-1]+" "+str(date.year)
	date = date.upper()
	pdfEdit.setCanvas(can[1],dat,date)
	pdfEdit.addToPDF(pdf,can)

def setHeure(pdf,heure):
	datA = data.arr
	datD = data.dep
	can = pdfEdit.newCanvas()
	
	heureA = heure
	heureD = heureA - datetime.timedelta(hours = 1, minutes = 17)
	heureA = heureA.strftime("%H:%M")
	heureD = heureD.strftime("%H:%M")

	pdfEdit.setCanvas(can[1],datA,heureA)
	pdfEdit.setCanvas(can[1],datD,heureD)
	pdfEdit.addToPDF(pdf,can)



