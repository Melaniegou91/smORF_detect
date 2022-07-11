# SmORF detect

## Etape 1

Tout d'abord afin de pouvoir utiliser ce programme, il faut installer python 3 sur un système d'exploitation du type UNIX.

## Etape 2

Il faut que vous ayez en votre possession le fichier contenant la séquence que vous souhaitez étudier.
Pour diviser ce fichier en plusieurs fichiers si il a une taille importante.
Vous devez taper la commande suivante dans votre terminal :

```

python3 separefichier.py nom_fichier_aseparer.fasta

```
Vous devez remplacer le dernier argument par le nom de votre document à séparer.

Une fois cela fait, vous devriez avoir plusieurs fichiers où chaque fichier contient un chromosome.

## Etape 3

Pour étudier le fichier que vous souhaitez étudier vous pouvez rentrer la commande suivante dans le terminal :

```

python3 traduction.py nom_fichier_entree.fasta type_sequence nom_fichier_sortie.fasta

```

Vous devez mettre en argument le nom de votre fichier à étudier puis le type de votre séquence, c'est à dire ARN si c'est une séquence d'ARN ou ADN si c'est une séquence d'ADN. Le dernier argument sera le nom du fichier de sortie du programme que vous souhaitez.

## Etape 4

Pour chercher un peptide au sein de votre fichier de sortie vous pouvez utiliser la commande suivante :

```
grep 'peptide' nom_fichier_sortie.fasta

```
Vous pouvez utiliser les options suivantes de grep :

![grep](https://github.com/Melaniegou91/smORF_detect/blob/main/grep.png)

