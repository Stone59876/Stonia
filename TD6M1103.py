from random import *
from pileObjet import *

Coul = ["Coeur","Carreau","Pique","Treffle"]
Val = {"2":1,"3":2,"4":3,"5":4,"6":5,"7":6,"8":7,"9":8,"10":9,"Valet":10,"Dame":11,"Roi":12,"As":13}

class Carte:
    def __init__(self,val,coul):
        self.couleur=coul
        self.valeur=val
        
class Joueur:
    def __init__(self,name):
        self.nom=name
        self.cartes=Pile(52)
        self.plis=[]

class Partie:
    def __init__(self,name1,name2):
        self.P1=Joueur(name1)
        self.P2=Joueur(name2)
        self.tas= []
    
def creerJdC()->list:
    JdC=[]
    for C in Coul:
        for V in Val:
            carte=Carte(V,C)
            JdC.append(carte)
    return JdC

def melanger(j):
    l=[]
    while len(j)>0:
        c=randint(0,len(j)-1)
        l.append(j[c])
        j.pop(c)
    return l

def distribuer(p,j):
    p1=p[0]
    p2=p[1]
    cartej1=Pile(26)
    cartej2=Pile(26)
    for i in range(26):
        carte1=j.pop()
        empiler(cartej1,carte1)
        carte2=j.pop()
        empiler(cartej2,carte2)
    p1.tas=cartej1
    p2.tas=cartej2
    p=((p1,p2))
    return p
    
popo=creerJdC()
print(popo)
ccc=melanger(popo)
a=0
print(ccc)
for carte in ccc:
    a=a+1
    print("Valeur:",carte.valeur,"Couleur:",carte.couleur)
print(a)

clement=Joueur("clement")
lucas=Joueur("lucas")
joueur=((clement,lucas))
joueurpret=distribuer(joueur,ccc)
print(joueurpret[0].nom,joueurpret[0].tas,joueurpret[1].nom,joueurpret[1].tas)
carteclem=joueurpret[0].tas
cartelucas=joueurpret[1].tas
for i in range(26):
    carte=depiler(carteclem)
    print("Valeur:",carte.valeur,"Couleur:",carte.couleur)
print("carte de lucas")
for i in range(26):
    carte=depiler(cartelucas)
    print("Valeur:",carte.valeur,"Couleur:",carte.couleur)