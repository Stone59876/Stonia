from math import *

class Point:
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y
        
def ValPoint():
    x=int(input("Abscisse du point :"))
    y=int(input("Ordonnée du point :"))
    return Point(x,y)

def Distance(a,b):
    return sqrt(pow(a.x-b.x,2)+pow(a.y-b.y,2))
    
def Polygone()->list:
    l=[]
    nb=int(input("Combien de points comporte ce polygone :"))
    c=0
    while c<nb:
        p=ValPoint()
        l.append(p)
        c=c+1
    return l

def perimetrePoly(p:list):
    peri=0
    for i in range(0,len(p)):
        if i!=(len(p)-1):
            peri=peri+Distance(p[i],p[i+1])
        else:
            peri=peri+Distance(p[i],p[0])
    return peri
        
def sauverPoly(poly:list):
    nom=input("Nom du fichier:")
    nom=nom + ".txt"
    with open(nom,"w") as f:
        for point in poly:
            x=str(point.x)
            y=str(point.y)
            f.write(x)
            f.write(",")
            f.write(y)
            f.write("\n")
        
def recupPoly():
    nom=input("Nom du fichier:")
    nom=nom + ".txt"
    poly=[]
    with open(nom,"r") as f:
        for ligne in f:
            a=ligne.split(",")
            x=int(a[0])
            y=int(a[1])
            p=Point(x,y)
            poly.append(p)
    return poly

def Prog():
    a=ValPoint()
    b=ValPoint()
    d=Distance(a,b)
    print("La distance entre ces deux points est:",d)
    choix=input("Souhaitez vous sauvegarder ou récuperer un Polygone ?")
    if choix=="sauvegarder":
        p=Polygone()
        sauverPoly(p)
    elif choix=="récuperer":
        p=recupPoly()
        peri=perimetrePoly(p)
        print("Le périmètre du Polygone est:",peri)
    else:
        print("Choix incorrect,entrez sauvegarder ou récuperer")
        
Prog()
        


    
    
