#!/usr/bin/env python3

import string as st
import secrets as sc
import random as rnm

while True:
	tt = st.ascii_lowercase + st.ascii_uppercase + st.digits + st.punctuation
	print('\n')
	taille = int(input('chooose the size of your password : > ')) 
	print()
	choice = input('do you whant to generate a secure password >> press 1 	 or 	a ULTRA secure password >> press 2 > ')
	print()
	
	if choice == '2':
		print('[+] Generating your ULTRA secure password (option 2)...')
		print()
		gen = ''.join(sc.choice(tt) for i in range(1000000))
		r1 = ''.join(sc.choice(gen) for u in range(1000000))
		r2 = ''.join(sc.choice(r1) for o in range(10000))
		r3 = ''.join(rnm.choice(r2) for x in range(1000))
		rlast = ''.join(sc.choice(r3) for y in range(100))
		final = ''.join(sc.choice(rlast) for z in range(taille))
		print('[*] Your ULTRA secure password is > ' + final)
		
	elif choice == '1':
		print('[+] Generating your secure password (option 1)...')
		print()
		gen_ez = ''.join(sc.choice(tt) for e in range(taille))
		print('[*] Your secure password is > ' + gen_ez)
		print()
			
	else:
		print('RETRY')
	retry = input('Do you whant to generate another password ? (y/n)  > ')
	if retry.lower() == 'n':
		print('\n')
		print('Exiting...')
		break
