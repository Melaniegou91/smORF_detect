# smORF_detect

Le but de ce projet est d'analyser une séquence d'ADN afin de détecter des peptides de très petite taille qui n'ont pas été detecté jusqu'à présent.

Pour cela nous avons déja du mettre en place la séparation de fichier afin de pouvoir ouvrir un fichier et l'analyser.

## La séparation en plusieurs fichier 

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

![Cover](https://github.com/Melaniegou91/smORF_detect/blob/main/transcription.jpg)
