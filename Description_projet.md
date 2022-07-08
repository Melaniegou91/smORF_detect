# smORF_detect

Le but de ce projet est d'analyser une séquence d'ADN afin de détecter des protéines de très petite taille qui n'ont pas été detecté jusqu'à présent.

Pour cela nous avons déja du mettre en place la séparation de fichier afin de pouvoir ouvrir un fichier et l'analyser.

## La séparation en plusieurs fichiers

Nous avons créé un code afin de diviser un fichier en plusieurs fichiers car le transcriptome humain étant important, la taille du fichier l'est aussi.

Pour cela, nous allons séparer le fichier en créant de nouveau fichiers avec chacuns contenant un chromosome différent 

Cela va donc créer un nombre n de fichiers qui correspond au nombre n de chromosomes.
```{r}

with open ('GRCh38.p13.genome.fa', 'r')  as genome: 
  compteur = 0
  chromosome = "chromosome"
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
Pour faire cela nous avons donc demandé à notre code de créer un nouveau fichier qui s'appellera chromosomen.fasta  et de fermer l'ancien fichier à chaque fois que le symbole ">" sera rencontrée dans le fichier d'origine.


## L'analyse de la séquence d'ADN

Tout d'abord pour pouvoir utiliser ce code, il faut utiliser un des fichiers créer ultérieurement grâce au code separefichier.py 

Maintenant que le fichier a été selectionné, nous devons effectuer la traduction de la séquence.

![Traduction](https://github.com/Melaniegou91/smORF_detect/blob/main/transcription.jpg)

Pour cela, il a fallu prendre en compte les 6 cadres de lectures de la séquence. Tout d'abord nous avons pris en compte que les 3 premiers cadres.
Pour prendre en compte ces 3 cadres de lecture, il fallait commencer la lecture de la séquence d'ADN à différents nucleotides. Pour le premier cadre, nous commencions le lecture de la séquence au premeir nucléotide, pour le deuxième cadre nous commencions la lecture au second nucléotide et pour le troisième nous commencions la lecture au 3 ème nucléotide.

Ensuite pour faire les 3 autres cadres de lecture, il fallait que nous prenions en compte la sequence complémentaire. 

C'est pour cela que nous avons créer la fonction complementaire. Nous avons fait en sorte de d'abord trouver les nucléotides complémentaire et ensuite d'inverser le sens de lecture.

```
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
```

Par la suite il a fallu éditer le dictionnaire du Code génétique afin que lorsque l'on rencontre un codon nous sachions à quels acides aminés il correspondait.

![code génétique](https://github.com/Melaniegou91/smORF_detect/blob/main/Code%20g%C3%A9n%C3%A9tique.jpg)

```
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
```

Une fois cela fait, et après avoir pris en compte les problèmes de mémoire, nous sommes parvenus au code transcriptome.py




