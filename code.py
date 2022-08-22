import random

prix = random.randint(1, 10)
score = 100
tentatives = 0


print("Devinez le juste prix. Le prix est un nombre compris  entre 1 et 10.")

while true:
	nombre=int(input())
	tentatives +=1
	if nombre > prix:
		print(" Le juste prix est plus bas ")
	if nombre < prix:
		print(" Le juste prix est plus haut ")
	if nombre == prix:
		print("Félicitation !!! Vous avez trouvé le bon prix {} en essayant {}. Votre score est {} ".format(prix, tentatives, int(score/tentatives)))
		break
print("Partie terminée")		