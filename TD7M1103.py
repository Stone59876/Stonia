class pere:
    def __init__(self):
        self.valeur=0
        self.filsdroit=None
        self.filsgauche=None
        
class noeud:
    def __init__(self,val):
        self.valeur=val
        self.filsdroit=None
        self.filsgauche=None
        
class arbre:
    def __init__(self,pere):
        self.pere=pere
        
def arbrebinaire():
    papa=pere()
    valeur=input("Valeur du père :")
    papa.valeur=valeur
    valeur1=input("Valeur des fils :")
    valeur2=input()
    if valeur1>valeur2:
        fils1=noeud(valeur1)
        fils2=noeud(valeur2)
    elif valeur2>valeur1:
        fils1=noeud(valeur2)
        fils2=noeud(valeur1)
    else:
        fils1=noeud(valeur1)
        fils2=noeud(valeur2)
    papa.filsdroit=fils1
    papa.filsgauche=fils2
    arbre=arbre(papa)
    return arbre

def ajouter(arbre):
    noeud=arbre.pere
    if noeud.filsdroit!=None or noeud.filsgauche!=None:
        
        
    
    
        
        