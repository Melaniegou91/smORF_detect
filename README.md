# smORF_detect

Le but de ce projet est d'analyser une séquence d'ADN afin de détecter des peptides de très petite taille qui n'ont pas été detecté jusqu'à présent.

Pour cela nous avons déja du mettre en place la séparation de fichier afin de pouvoir ouvrir un fichier et l'analyser.

## La séparation en plusieurs fichiers 

Dans ce code, nous cherchons à diviser un fichier en plusieurs fichiers car le transcriptome humain étant important, la taille du fichier l'est aussi.

Pour cela, nous allons séparer le fichier en créant de nouveau fichiers avec chacun contenant un chromosome différent 



```{r}
with open ('human_g1k_v37.fasta', 'r')  as genome: 
  compteur = 0
  chromosome = "chromosome37h"
  strcompteur=str(compteur)
  filehandler = open(chromosome+strcompteur+'.fasta','a+')
  for ligne in genome :
    if ligne.startswith('>'):
      compteur=compteur+1
      strcompteur=str(compteur)
      filehandler.close()
      filehandler=open(chromosome+strcompteur+'.fasta','a+')
      filehandler.write(ligne)
    else :
      filehandler.write(ligne)
```

Cela va donc créer un nombre n de fichiers qui correspond au nombre n de chromosomes.

## L'analyse de la séquence d'ADN

Tout d'abord pour pouvoir utiliser ce code, nous utilisons un des fichiers créer ultérieurement grâce au code separefichier.py 

Maintenant que nous avons sélectionner notre fichier, nous devons effectuer la traduction de la séquence.

![Cover](https://github.com/Melaniegou91/smORF_detect/blob/main/transcription.jpg)

Pour cela, il a fallu prendre en compte les 6 cadres de lectures de la séquence. Tout d'abord nous avons pris en compte que les 3 premiers.

Ce qui nous ont menés au code suivant :

```{r}
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

```


