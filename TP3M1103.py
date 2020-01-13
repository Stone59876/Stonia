def reverse(nom:str):
    nomreverse=(nom + "_reverse.pbm")
    nomlec=(nom + ".pbm")
    l:list
    l=[]
    v=[]
    with open(nomlec,"r") as image:
        for ligne in image:
            l.append(ligne)
        for i in range(0,len(l)):
            c=l[i]
            v.append([])
            for j in range(len(c)):
                v[i].append(c[j])
        for x in range(2,len(v)):
            for z in range(len(v[x])):
                if v[x][z]=="0":
                    v[x][z]="1"
                elif v[x][z]=="1":
                    v[x][z]="0"
    reverse=open(nomreverse,"w")
    for valeur in v:
         for char in valeur:
            reverse.write(char)
          

def reverse2(nom:str):
    nomreverse=(nom + "_reverse.pgm")
    nomlec=(nom + ".pgm")
    l:list
    l=[]
    v=[]
    h=[]
    with open(nomlec,"r") as image:
        for ligne in image:
            l.append(ligne)
        for i in range(0,len(l)):
            c=l[i]
            v.append([])
            for j in range(len(c)):
                v[i].append(c[j])
        print(v)
        p=0
        maxi=""
        while v[2][p]!="\n":
            maxi=(maxi + v[2][p])
            p=p+1
        maxi=int(maxi)
        print(maxi)
        for x in range(len(v)):
            for z in range(len(v[x])):
                h.append(v[x][z])
        print(h)
        q=[]
        for char in h:
            if char!=" " and char=!="\n":
                
            
    
    reverse=open(nomreverse,"w")
    for valeur in v:
         for char in valeur:
            reverse.write(char)

reverse2("image")