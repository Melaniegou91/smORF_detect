import re
with open('chromosome1.fasta', 'r')  as sequence_adn:

	seqCOMPLEMENTAIRE=''
	
	
	
	Code_genetique = {"ATA":"I", "ATC":"I", "ATT":"I", "ATG":"M",
                    	  'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
                    	  'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
                    	  'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',                
                    	  'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
                    	  'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
                    	  'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
                    	  'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
                    	  'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
                    	  'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
                    	  'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
                   	  'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
                   	  'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
                   	  'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
                   	  'TAC':'Y', 'TAT':'Y', 'TAA':'*', 'TAG':'*',
                   	  'TGC':'C', 'TGT':'C', 'TGA':'*', 'TGG':'W',
                     
                   	 }
                   	 

   
	def translate(sequence_adn, x):
		
		codon=""	#Initialise le codon à  un string vide
		aa=""		#initialise le sequence de protéine à un string vide
		counter=0	#Initialise le codon à 0
		for line in sequence_adn:	#Parcours chaque lignes une à une du fichier
			counter+=1		#On ajoute 1 au compteur à chaque fois qu'on a parcouru une ligne
			if counter == 2:	#Si le compteur = 2 on applique la condition suivante :
				line = line[x:] #la ligne change et commence à l'indice x et termine à la fin de la ligne
				
      				
			if line.startswith('>') : #Si la ligne ne commence pas par un > on rentre dans la boucle suivante
				aa+='\n'
				for caracteres in line:	# On parcours chaque caractere d'une ligne
					
					aa+=caracteres
					
					
			else :
				for caracteres in line:
					if(len(codon)<2):	# Si la longueur du codon est < à 2 on applique :
						codon = codon + caracteres	#On ajoute au codon le caractere parcouru
					else:	#Si la longueur du codon est > à 2 on applique les lignes suivantes :
						codon+=caracteres	#On ajoute au codon le caractere parcouru
						if codon in Code_genetique:	#si le codon fait partis du code génétique :
							aa=aa+Code_genetique[codon]#On ajoute à la sequence protéique le codon
							codon="" #Le codon redevient vide
						
						else:	#Si le codon n'est pas dans le code genetique :
							aa+='X'	#On ajoute à la sequence proteique le caractère 'X'
							codon=""	#Le codon redevient vide
			
			
		return(aa)	#La fonction renvoie la sequence protéique
	
	
	cadre1 = translate(sequence_adn,0)
	fichier = open("M38_cadre1.fasta","a+")
	fichier.write(cadre1)
	fichier.close()
	sequence_adn.seek(0)
	cadre2 = translate(sequence_adn,1)
	fichier2 = open("M38_cadre2.fasta","a+")
	fichier2.write(cadre2)
	fichier2.close()
	sequence_adn.seek(0)
	cadre3 = translate(sequence_adn,2)
	fichier3 = open("M38_cadre3.fasta","a+")
	fichier3.write(cadre3)
	fichier3.close()
	sequence_adn.seek(0)
	
	def complementaire(sequence_adn) :
		seq_compl = ""
		for line in sequence_adn:
			if line.startswith('>'):
				seq_compl = seq_compl+'\n' 
				for caractere in line:
					caractere=caractere.lower()
					seq_compl+=caractere
				seq_compl = seq_compl+'\n' 
			else :
				for caractere in line:
					if caractere == 'A':
					 	caractere = 'T'
					 	seq_compl+=caractere
					elif caractere == "T":
					 	caractere = "A"
					 	seq_compl+=caractere
					elif caractere == 'C':
					 	caractere="G"
					 	seq_compl+=caractere
					elif caractere == 'G':
					 	caractere = 'C'
					 	seq_compl+=caractere
					else:
					 	caractere=caractere
					 	seq_compl+=caractere
				seq_compl = seq_compl+'\n' 
		seq_compl=seq_compl[::-1]
		return (seq_compl)
		
		
	compl=complementaire(sequence_adn)
	
	def translatecompl(sequence_adn, x):
		
		codon=""	#Initialise le codon à  un string vide
		aa=""		#initialise le sequence de protéine à un string vide
		counter=0	#Initialise le codon à 0
		for line in sequence_adn:	#Parcours chaque lignes une à une du fichier
			counter+=1		#On ajoute 1 au compteur à chaque fois qu'on a parcouru une ligne
			if counter == 2:	#Si le compteur = 2 on applique la condition suivante :
				line = line[x:] #la ligne change et commence à l'indice x et termine à la fin de la ligne
				
      				
			if line.startswith('>') : #Si la ligne ne commence pas par un > on rentre dans la boucle suivante
				
				for caracteres in line:	# On parcours chaque caractere d'une ligne
					
					aa+=caracteres
				aa+='\n'
					
					
			else :
				for caracteres in line:
					if(len(codon)<2):	# Si la longueur du codon est < à 2 on applique :
						codon = codon + caracteres	#On ajoute au codon le caractere parcouru
					else:	#Si la longueur du codon est > à 2 on applique les lignes suivantes :
						codon+=caracteres	#On ajoute au codon le caractere parcouru
						if codon in Code_genetique:	#si le codon fait partis du code génétique :
							aa=aa+Code_genetique[codon]#On ajoute à la sequence protéique le codon
							codon="" #Le codon redevient vide
						
						else:	#Si le codon n'est pas dans le code genetique :
							aa+='X'	#On ajoute à la sequence proteique le caractère 'X'
							codon=""	#Le codon redevient vide
			
			
		return(aa)
	
	
	cadre4 = translatecompl(compl,0)
	fichier4 = open("M38_cadre4.fasta","a+")
	fichier4.write(cadre4)
	fichier4.close()
	cadre5 = translatecompl(compl,1)
	fichier5 = open("M38_cadre5.fasta","a+")
	fichier5.write(cadre5)
	fichier5.close()
	cadre6 = translatecompl(compl,2)
	fichier6 = open("M38_cadre6.fasta","a+")
	fichier6.write(cadre6)
	fichier6.close()
	
	
	#smORF_detects
	
 			
