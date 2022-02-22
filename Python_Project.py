#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 11 08:43:27 2022

@author: secke
"""
##############la fonction des numéros ####################
def numero(x):
    """la fonction pour vérifier la validité des numéros
    """
    from string import ascii_uppercase as Majuscul
    chiffre=['0','1','3','4','5','6','7','8','9']
    if (([i for i in Majuscul  if (i in x)==True]) and ([j for j in chiffre if (j in x)==True])) and (len(x)==7):
        return True
    else:
        return False

############ la fonction des prenoms et celle des noms ################
def prenom(x):
    """la fonction pour valider les prénoms obtenus
    """
    from string import ascii_letters
    
    if ([i for i in ascii_letters  if x[0]==i]) and len(x)>=3:
        return True
    else:
        return False
def nom(x):
    """
    la fonction pour valider les noms obtenus"""
    from string import ascii_letters
    if ([i for i in ascii_letters  if x[0]==i]) and len(x)>=2:
        return True
    else:
        return False
############### la fonction des calsse ########################
def classe(x:str()):
    """la fonction pour la validité du format des classes
    """
    collez=['6em A','6em B','5em A','5em B','4em A','4em B','3em A','3em B']
    if ([clas for clas in collez if x==clas]):
        return True
    else:
        return False


############### fonctions pour les dates #####################
def formattaz(x):
    """
    la fonction de formattage des dates"""
    
    for i in x:
        if ('-'==i) or (' '==i) or ('_'==i) or (','==i) or (';'==i) or (':'==i) or ('.'==i):
            x=x.replace(i,'/') 
    return x


def ConverMois(x):
    """
    cette fonction nous permet de convertir les mois """
    
    xo=x.split("/")
    if len(xo)==3 and (xo[1] in 'janvier'):
        xo[1]='01'
    elif len(xo)==3 and (xo[1] in 'fevrier'):
        xo[1]='02'
    elif len(xo)==3 and (xo[1] in 'mars'):
        xo[1]='03'
    elif len(xo)==3 and (xo[1] in 'avril'):
        xo[1]='04'
    elif len(xo)==3 and (xo[1] in 'mai'):
        xo[1]='05'
    elif len(xo)==3 and (xo[1] in 'juin'):
        xo[1]='06'
    elif len(xo)==3 and (xo[1] in 'juillet'):
        xo[1]='07'
    elif len(xo)==3 and (xo[1] in 'aout'):
        xo[1]='08'
    elif len(xo)==3 and (xo[1] in 'septembre'):
        xo[1]='09'
    elif len(xo)==3 and (xo[1] in 'octobre'):
        xo[1]='10'
    elif len(xo)==3 and (xo[1] in 'novembre'):
        xo[1]='11'
    elif len(xo)==3 and (xo[1] in 'decembre'):
        xo[1]='12'
    return xo

def DateValid(jour,mois,an):
    """ 
    La fonction pour vérifier la validité des dates """

    if (jour.isnumeric()==True) and (an.isnumeric()==True):
        jour=int(jour)
        mois=int(mois)
        an=int(an)
        if (mois==1 or mois==3 or mois==5 or mois==7 or mois==8 or mois==10 or mois==12) and (jour<=31):
            return True
        elif (mois==4 or mois==6 or mois==9 or mois==11) and (jour<=30):
            return True
        elif (mois==2) and (an%4==0 and an%100!=0) and (jour<=29):
            return True
        elif (mois==2) and (an%4!=0 or an%100==0) and (jour<=28):
            return True
    else:
        return False

######### Programme Principal pour le traitement des données(valides vs invalides) #############
import csv
taf=open('Projet_Python.csv', 'r')
cles=["CODE","Numero","Nom","Prénom","Date de naissance","Classe","Note","Moyenne générale"]
cles_inv=["CODE","Numero","Nom","Prénom","Date de naissance","Classe","Note"]
lire=csv.DictReader(taf)
n0=0
n1=0
valide=open('fichier_valid.csv','w')
ecrire=csv.DictWriter(valide, fieldnames=cles)
ecrire.writeheader()
invalide=open('fichier_invalid.csv','w')
ecrire_inv=csv.DictWriter(invalide, fieldnames=cles_inv)
ecrire_inv.writeheader()
for l in lire:
    l['Date de naissance']=formattaz(l['Date de naissance'])
    Date_cvt=ConverMois(l["Date de naissance"])
    if (numero(l["Numero"])==True) and (DateValid(Date_cvt[0],Date_cvt[1],Date_cvt[2])==True) and (prenom(l["Prénom"])==True) and (nom(l["Nom"])==True) and (classe(l["Classe"])==True):
        
        note=str(l["Note"]).split("#")
        n_mat=0
        s_mat=0
        Note=[]
        for matiere in note:
            se=matiere.split("[")[1].split(']')[0]
            nom_mat=matiere.split("[")[0]
            se1=se.split(":")
            ntt0=se1[0].split(";")
            ntt0.append(se1[1])
            ntt=ntt0
            nouv_nt=[]
            for carac in ntt:
                for c in carac:
                    if c==',':
                        vv=carac.replace(c,'.')
                        carac=vv
                nouv_nt.append(carac)
                matiere=list(map(float,nouv_nt))
            Note.append([matiere,nom_mat])
        note=[Note[i][0] for i in range(len(Note))]
        n=0
        som=0
        for s in range(len(note)):
            n_mat=n_mat+1
            j=note[s]
            for i in range(len(j)-1):
                n=n+1
                som=som+j[i]
            moy=((som/n)+2*j[-1])/3
            s_mat=s_mat+moy
            moy_gen=s_mat/n_mat
            note.insert(note.index(j),f"{Note[s][1]}:{j} moyenne[{round(moy,2)}]")
            del note[note.index(j)]
            l["Note"]=note
        l["Moyenne générale"]=round(moy_gen,2)
        
        ecrire.writerow(l)
        n0=n0+1
    else:
        ecrire_inv.writerow(l)
        n1=n1+1
        
taf.close()
valide.close()
invalide.close()


################################## Menu ########################################

def Menu():
    
    def choice():
        """
        la fonction pour choisir l'affichage des données valides 
        ou invalides"""
        import csv
        val=open('fichier_valid.csv','r')
        lectur=csv.DictReader(val)
        inval=open('fichier_invalid.csv','r')
        lectur_inv=csv.DictReader(inval)
   
        c=str(input("Veuiller tapez $ pour les infos valides ou £ pour les infos invalides : "))
        if c=='$':
            for a in lectur:
                print(a)
        elif c=='£':
            for b in lectur_inv:
                if not (numero(b["Numero"])==True):
                    raise Exception("le format du numéro est incorrect!",b)
                elif not (prenom(b["Prénom"])==True):
                    raise Exception("le prénom est incorrect",b)
                elif not (nom(b["Prénom"])==True):
                    raise Exception("le nom est incorrect",b)
                elif not (classe(b["Classe"])==True):
                    raise Exception("le format de la classe n'est pas bon",b)
                else:
                    raise Exception("la date n'est pas valide",b)
                print(b)

    def InfoNum():
        """
        Cette fonction permet d'afficher les informations par numéro saisi au clavier """
        x=input("Veuillez entrer le numéro: ")
        import csv
        learn=open("fichier_valid.csv","r")
        lire=csv.DictReader(learn)
        for p in lire:
            if x==p["Numero"]:
                print(p)
                break

    def cinq():
        """
        la fonction pour afficher les cinqs premiers """
        import csv
        val=open('fichier_valid.csv','r')
        lectur=csv.DictReader(val)
        ordonne=[]
        for l in lectur:
            ordonne.append(l)
        from operator import itemgetter
        ordonne=sorted(ordonne, key=itemgetter('Moyenne générale'), reverse=True)
        return ordonne[1:6]
    
    print("Pour afficher les données valides ou invalides taper 1")
    print("Pour afficher les informations par numéro taper 2")
    print("Pour afficher les cinqs premiers taper 3")
    x=input("Entrer votre choix: ")
    if x=='1':
        return choice()
    elif x=='2':
        return InfoNum()
    elif x=='3':
        return cinq()
    
