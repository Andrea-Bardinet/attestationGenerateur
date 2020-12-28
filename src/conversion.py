""" fonction de conversion des données """

""" valeur 0-255 vers 0-1 """
def toRgb(rgb):
	return [val/255 for val in rgb]

""" convertit valeur en pixel trouvé sur inkscape vers celle en python
je n'ai pas trouvé comment bien regler le canvas,
 donc j'utilise ca en attendant"""
def toPx(coord):
	return [val/1.35 for val in coord]