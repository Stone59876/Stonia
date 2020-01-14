from pileObjet import *

def opari(n1:float,n2:float,op:str)->float:
    if op=="+":
        return (n1+n2)
    elif op=='-':
        return (n1-n2)
    elif op=='*':
        return (n1*n2)
    elif op=='/':
        return (n1/n2)
    
def calculPile(p:Pile):
    op=depiler(p)
    v1=depiler(p)
    v2=depiler(p)
    res=opari(v1,v2,op)
    return res

def calculPile2(p:Pile):
    v1=depiler(p)
    v2=depiler(p)
    op=depiler(p)
    res=opari(v1,v2,op)
    return res

def calculatrice():
    pascal=Pile()
    print("Ecrire le calcul:")
    calc=input()
    for valeur in calc:
        if valeur!="+" and valeur!="-" and valeur!="*" and valeur!="/":
            empiler(pascal,int(valeur))
        else:
            empiler(pascal,valeur)
    afficherPile(pascal)
    while not estVide(pascal):
        print("non")
        
    
