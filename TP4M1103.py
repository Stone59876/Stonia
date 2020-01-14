class Etudiant:
    def __init__(self):
        self.nom="nom"
        self.prenom="prenom"
        self.anne=0
        self.moyenne=0.0
        self.promo=1

def creeretu(nom,prenom,anne,moy,promo):
    etu=Etudiant()
    etu.nom=nom
    etu.prenom=prenom
    etu.anne=anne
    etu.moyenne=moy
    etu.promo=promo
    return etu

def initTableau():
    nombredetu=int(input("Choisir le nombre d'étudiants a insérer:"))
    tableau=[["Etudiants","Nom","Prénom","Année","Moyenne","Promo"]]
    for i in range(nombredetu):
        etu:list
        etu=[]
        E=Etudiant()
        E.nom=input("Nom de l'étudiant :")
        E.prenom=input("Prénom de l'étudiant :")
        E.anne=int(input("Année de naissance de l'étudiant :"))
        E.moyenne=float(input("Moyenne de l'étudiant :"))
        E.promo=int(input("Numéro de la promotion de l'étudiant :"))
        etu=[i,E.nom,E.prenom,E.anne,E.moyenne,E.promo]
        tableau.append(etu)
    return tableau
        
def affichageTableau(tableau:list):
    for ligne in tableau:
        print(" ")
        for colonne in ligne:
            print(colonne,end="\t")
            
def ajoutEtu(tableau:list):
    etu=[]
    E=Etudiant()
    E.nom=input("Nom de l'étudiant :")
    E.prenom=input("Prénom de l'étudiant :")
    E.anne=int(input("Année de naissance de l'étudiant :"))
    E.moyenne=float(input("Moyenne de l'étudiant :"))
    E.promo=int(input("Numéro de la promotion de l'étudiant :"))
    etu=[i,E.nom,E.prenom,E.anne,E.moyenne,E.promo]
    tableau.append(etu)
    return tableau
    
def rechercherEtu(Etu:Etudiant(),tableau:list):
    nometu=Etu.nom
    trouve:bool
    trouve=False
    x=1
    while x<len(tableau) and not trouve:
        if tableau[x][1]==nometu:
            trouve=True
        else:
            x=x+1
    if trouve==True:
        etudiantcherche=tableau[x]
        print("\n")
        print("Voici l'étudiant recherché:")
        for valeur in etudiantcherche:
            print(valeur,end='\t')
        return etudiantcherche
    else:
        print("Etudiant non trouvé !")
        return None
    
def supprimerEtu(etu:Etudiant(),tableau:list):
    info=rechercherEtu(etu,tableau)
    indice=info[0]+1
    del tableau[indice]
    return tableau

def triEtu(tableau:list):
    l=tableau
    for n in range(2,len(l)):
        cle=l[n]
        cle2=l[n][4]
        j=n-1
        while j>=1 and l[j][4]>cle2:
            l[j+1]=l[j]
            j=j-1
        l[j+1]=cle
    return l

def majeurPromo(tableau:list):
    promo1=[["promotion une"],]
    promo2=[["promotion deux"],]
    tableau.pop(0)
    for ligne in tableau:
        if ligne[5]==1:
            promo1.append(ligne)  
        elif ligne[5]==2:
            promo2.append(ligne)
    promotri1=triEtu(promo1)
    promotri2=triEtu(promo2)
    majeur1=promotri1[-1]
    majeur2=promotri2[-1]
    print("Voici le majeur de la promotion 1:")
    for valeur in majeur1:
        print(valeur,end="\t")
    print ("\n")
    print("Voici le majeur de la promotion 2:")
    for valeur2 in majeur2:
        print(valeur2,end="\t")
    return majeur1,majeur2

classe=[['Etudiants', 'Nom', 'Prénom', 'Année', 'Moyenne', 'Promo'], [0, 'Cogo', 'Clément', 2001, 15.0, 1], [1, 'Fievez', 'Paul', 2001, 13.5, 1], [2, 'Pichon', 'Georges', 1999, 16.0, 1], [3, 'Marcaille', 'Lucas', 2000, 12.5, 2], [4, 'Wayne', 'Bruce', 1987, 14.5, 2], [5, 'Molotov', 'Dimitri', 1892, 20.0, 2]]

def sauverTableau(tableau:list):
    fichier=input("Nom du fichier à créer:")
    fichier=(fichier + ".txt")
    with open(fichier,"w") as fichiertxt:
        for ligne in tableau:
            for colonne in ligne:
                fichiertxt.write( str(colonne) + ";")
            fichiertxt.write("\n")

        
def recupTableau():
    fichier=input("Nom du fichier à ouvrir:")
    fichier=(fichier + ".txt")
    with open(fichier,"r") as fichiertxt:
        tableau=[]
        for ligne in fichiertxt:
            s = ligne.strip("\n")
            s = s.strip("\r")
            v = s.split(";")
            tableau.append(v)        
    return tableau
        
def modifFichier():
    fichier=input("Nom du fichier à modifier:")
    fichier=(fichier + ".txt")
    nometu=input("Nom de l'étudiant dont les informations doivent être modifiées:")
    with open(fichier,"r") as fichiertxt:
        tableau=[]
        for ligne in fichiertxt:
            s = ligne.strip("\n")
            s = s.strip("\r")
            v = s.split(";")
            tableau.append(v)
    trouve=False
    x=1
    while x<len(tableau) and not trouve:
        if tableau[x][1]==nometu:
            trouve=True
        else:
            x=x+1
    if trouve==True:
        etudiantamodif=tableau[x]
        print("L'étudiant à modifié est dans le tableau")
    else:
        print("L'étudiant n'est pas dans le tableau !")
        return None
    choix=input("Quelle valeur souhaitez vous modifiez ? (Nom,Prénom,Année de naissance,Moyenne,Promo)")
    if choix=='Nom':
        pos=1
    elif choix=='Prénom':
        pos=2
    elif choix=='Année de naissance':
        pos=3
    elif choix=='Moyenne':
        pos=4
    elif choix=='Promo':
        pos=5
    else:
        print("Choix incorrect !")
        print("Veuillez entrez les valeurs suivantes :")
        print("Nom","\n","Prénom","\n","Année de naissance","\n","Moyenne","\n","Promo")
        choix=input("Entrez votre choix:")
        if choix=='Nom':
            pos=1
        elif choix=='Prénom':
            pos=2
        elif choix=='Année de naissance':
            pos=3
        elif choix=='Moyenne':
            pos=4
        elif choix=='Promo':
            pos=5
        else:
            pass
    valactuel=etudiantamodif[pos]
    print("Voici la valeur actuelle pour ",choix,valactuel)
    new=input("Entrez la valeur que vous souhaitez mettre a la place:")
    tableau[x][pos]=new
    with open(fichier,"w") as fichiertxt:
        for ligne in tableau:
            for colonne in ligne:
                fichiertxt.write( str(colonne) + ";")
            fichiertxt.write("\n")
        

def supEtuFich():
    tableau=recupTableau()
    print(tableau)
    nomEtu=input("Nom de l'étudiant à supprimer du tableau:")
    trouve=False
    x=1
    while x<len(tableau) and not trouve:
        if tableau[x][1]==nomEtu:
            trouve=True
        else:
            x=x+1
    if trouve==True:
        etudi=tableau[x]
    else:
        print("Etudiant non trouvé !")
        return None   
    pos=int(etudi[0])+1
    del tableau[pos]
    fichier=input("Nom du fichier contenant le tableau avec étudiant supprimé:")
    fichier=(fichier + ".txt")
    with open(fichier,"w") as fichiertxt:
        for ligne in tableau:
            for colonne in ligne:
                fichiertxt.write( str(colonne) + ";")
            fichiertxt.write("\n")
    
def affichageFich():
    fichier=input("Nom du fichier à lire:")
    fichier=(fichier + ".txt")
    with open(fichier,"r") as fichiertxt:
        for ligne in fichiertxt:
            print("\n")
            s = ligne.strip("\n")
            s = s.strip("\r")
            v = s.split(";")
            for val in v:
                print(val,end="\t")
                
        
    
        
affichageFich()
        


