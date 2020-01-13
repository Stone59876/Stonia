import time
import random
start_time = time.time()

def remplacer(l1:list,i:int,l2:list)->list:
    a=0
    for j in range (i,i+len(l2)):
        l1[j]=l2[a]
        a+=1
    return (l1)
 
 
def fusionner(liste:list,deb:int,mil:int,fin:int):
    j:int
    k:int
    j,k = deb,mil+1
    tmp=[]
    while j<=mil and k<=fin:
        if liste[j]<liste[k]:
            tmp.append(liste[j])
            j+=1
        else:
            tmp.append(liste[k])
            k+=1
    while j<=mil:
        tmp.append(liste[j])
        j+=1
    while k<=fin:
        tmp.append(liste[k])
        k+=1
    l=remplacer(liste,deb,tmp)
    return l
 
def trierpartition(liste:list,deb:int,fin:int):
    if(fin-deb>0):
        if(fin-deb==1) and liste[deb]>liste[fin]:
            liste[deb],liste[fin] = liste[fin],liste[deb]
        else:
            mid = (deb+fin) // 2
            liste=trierpartition(liste,deb,mid)
            liste=trierpartition(liste,mid+1,fin)
            liste=fusionner(liste,deb,mid,fin)
    return liste
 
def trifusion(liste:list):
    trierpartition(liste,0,len(liste)-1)
    return liste
 
def triInsertion(l):
    for n in range(1,len(l)):
        cle=l[n]
        j=n-1
        while j>=0 and l[j]>cle:
            l[j+1]=l[j]
            j=j-1
        l[j+1]=cle
    return l

    
def prog():
    liste=[]
    for k in range(1000000):
        liste.append(random.randint(0,20))
    a=trifusion(liste)
    print(a)

def prog2():
    liste=[]
    for k in range(1000):
        liste.append(random.randint(0,20))
    b=triInsertion(liste)
    print(b)
    
print(triInsertion([3,1,2,5,4,6,7,8,9]))
    
