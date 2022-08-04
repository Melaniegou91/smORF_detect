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
   
import sys
nom_fichier_aseparer=sys.argv[1]
with open (nom_fichier_aseparer, 'r')  as genome: 
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
   
    
        
         
         
         
         
         
         
         
         
         
         
         
         
         
