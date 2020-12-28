""" --- Liste des differents valeurs --- """

import conversion as conv

""" init """
nom = {} 
prenom = {} 
date = {} 
arr = {} 
dep = {}

""" position """
nom["pos"] = conv.toPx([467,1004])  #arial bold 10px mAJ rgb 62 61 64
prenom["pos"] = conv.toPx([487,985]) #arial bold 10px
date["pos"] = conv.toPx([37,912]) #arial bold MAJ 13 px rgb 0 117 161
arr["pos"] = conv.toPx([45,814]) #arial bold 10px 155 39 67
dep["pos"] = conv.toPx([45,892])

""" rgb """
nom["rgb"] = prenom["rgb"] = conv.toRgb([62,61,64])
date["rgb"] = conv.toRgb([0,117,161])
arr["rgb"] = dep["rgb"] = conv.toRgb([155,39,67])

""" font """
nom["font"] = prenom["font"] = date["font"] = 'Helvetica'
arr["font"] = dep["font"] = 'Helvetica-Bold'

""" size """
nom["size"] = prenom["size"] = dep["size"] = arr["size"] = 10
date["size"] = 15

""" autre """
jours = ["lundi","mardi","mercredi","jeudi","vendredi","samedi","dimanche"]
mois = ["janvier","février","mars","avril","mai","juin","juillet","août","septembre","octobre","novembre","décembre"]

	
