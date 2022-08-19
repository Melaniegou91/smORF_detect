import sys
import os
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
os.remove("chromosome0.fasta")



# Ancienne version
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
   
    
        
         
         
         
         
         
         
         
         
         
         
         
         
         
