#!/usr/bin/env python3

import string as st
import secrets as sc
import random as rnm

while True:
	tt = st.ascii_lowercase + st.ascii_uppercase + st.digits + st.punctuation
	print('\n')
	taille = int(input('choisie la taille de ton mots de passe : > ')) 
	print()
	choice = input('veux tu générer un mots de passe sécurisé >> press 1 	 ou 	un mots de passe ULTRA sécurisé >> press 2 > ')
	print()
	
	if choice == '2':
		print('Votre mots de passe ULTRA sécurisé se génére (option 2)...')
		print()
		gen = ''.join(sc.choice(tt) for i in range(1000000))
		r1 = ''.join(sc.choice(gen) for u in range(1000000))
		r2 = ''.join(sc.choice(r1) for o in range(10000))
		r3 = ''.join(rnm.choice(r2) for x in range(1000))
		rlast = ''.join(sc.choice(r3) for y in range(100))
		final = ''.join(sc.choice(rlast) for z in range(taille))
		print('ton mots de passe ULTRA sécurisé est le suivant > ' + final)
		
	elif choice == '1':
		print('Votre mots de passe sécurisé se génére (option 1)...')
		print()
		gen_ez = ''.join(sc.choice(tt) for e in range(taille))
		print('ton mots de passe est le suivant > ' + gen_ez)
		print()
			
	else:
		print('Choix invalide, veuiller réessayer')
	retry = input('veux tu refaire le générateur ? (oui/non)  > ')
	if retry.lower() == 'non':
		print('\n')
		print('Exiting...')
		break
