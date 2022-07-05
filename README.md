# smORF_detect

Le but de ce projet est d'analyser une séquence d'ADN afin de détecter des peptides de très petite taille qui n'ont pas été detecté jusqu'à présent.

Pour cela nous avons déja du mettre en place la séparation de fichier afin de pouvoir ouvrir un fichier et l'analyser.

## La séparation en plusieurs fichiers

Nous avons crée un code afin de diviser un fichier en plusieurs fichiers car le transcriptome humain étant important, la taille du fichier l'est aussi.

Pour cela, nous allons séparer le fichier en créant de nouveau fichiers avec chacuns contenant un chromosome différent 

Cela va donc créer un nombre n de fichiers qui correspond au nombre n de chromosomes.

## L'analyse de la séquence d'ADN

Tout d'abord pour pouvoir utiliser ce code, il faut utiliser un des fichiers créer ultérieurement grâce au code separefichier.py 

Maintenant que le fichier a été selectionné, nous devons effectuer la traduction de la séquence.

![Traduction](https://github.com/Melaniegou91/smORF_detect/blob/main/transcription.jpg)

Pour cela, il a fallu prendre en compte les 6 cadres de lectures de la séquence. Tout d'abord nous avons pris en compte que les 3 premiers cadres.
Pour prendre en compte ces 3 cadres de lecture, il fallait commencer la lecture de la séquence d'ADN à différents nucleotides. Pour le premier cadre, nous commencions le lecture de la séquence au premeir nucléotide, pour le deuxième cadre nous commencions la lecture au second nucléotide et pour le troisième nous commencions la lecture au 3 ème nucléotide.

Ensuite pour faire les 3 autres cadres de lecture, il fallait que nous prenions en compte la sequence complémentaire. 

C'est pour cela que nous avons créer la fonction complementaire. Nous avons fait en sorte de d'abord trouver les nucléotides complémentaire et ensuite d'inverser le sens de lecture.

Par la suite il a fallu éditer le dictionnaire du Code génétique afin que lorsque que l'on rencontre un codon nous sachions à quels acides aminés il corespondait.

![code génétique](https://github.com/Melaniegou91/smORF_detect/blob/main/Code%20g%C3%A9n%C3%A9tique.jpg)

Une fois cela fait, et apres avoir pris en compte les




