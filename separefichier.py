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
      
  #chromosome2=open('chromosome2.fasta','r')
  #print(chromosome2.read())
   
   
   
'''   
   uvrir le fichier en lecture
   utiliser boucle
   a chaque qu'une ligne commence par > ca declence 'ouverture en ecriture en fichier en append
   ca ecrit le ligne en cours dans ce fichier qui vient d'etre ouvert
   initialiser une variable compteur =0
   des que le cdition de tomber sur le signe sera rencontrer 
   chromosome+compteur+'fasta'
         
'''         
         
         
         
         
         
         
         
         
         
         
         
         
         
