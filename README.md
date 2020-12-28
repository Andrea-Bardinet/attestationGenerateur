
# attestationGenerateur
Générateur d'attestation pour Bordeaux. 

## Disclaimer
Ce projet n'a pas pour but d'inciter à outre passer le couvre-feu/confinement.
Il s'agit surtout d'un petit projet en python pour s'entrainer.
Respectez les règles.

## Principe de base
On génère billet de train allant à Bordeaux. Il sert d'attestation valide.
J'ai modifié ce billet pour supprimer les champs à modifier.
Le programme se contente simplement d'écrire du texte aux endroits adéquats.
Ainsi, le QRcode ou le code du billet originel restent inchangés.

## Utiliser

Utilisez ce format de commande pour créer votre billet (dans le répertoire créé par git):

```bash
python3 src/generer.py nom prenom jour/mois/année heure:minute nomDuFichier
```

**nom**: Votre nom
**prénom**: Votre prénom
**jour/mois/année**: La date ou commence l'attestation
**heure:minute**: L'heure a laquelle commence l’attestation
**nomFichier**: Nom du fichier en sortie

Le fichier créé est ensuite placé dans le répertoire courant (vous pouvez rentrer un chemin a la place du nom)

## Exemple
```bash
python3 src/generer.py Dupont Bernar 10/08/2020 21:30 monAttestation
```

## Organisation

Si vous souhaitez modifier le projet voici son organisation:

* pdf
	* **model.pdf**: Billet de train vide qui sera modifié
* src
	* **generer**: Lit les arguments et appel les fonctions pour créer le billet.
	* **data**: Contient toutes les données pour créer le billet. Coordonnées du texte, les couleurs, les fonts ect..
	* **setValeur**: Permet de préparer la création des canvas en recueillant les données et en formatant le texte en entrée.
	* **pdfEdit**: Contient toutes les fonctions servant à lire, créer, modifier les PDF.



