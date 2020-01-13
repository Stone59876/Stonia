def insererval(l:list,v:int):
    liste:list
    liste=[]
    for i in range(0,len(l)):
        if v>l[i]:
            if v<=l[i+1]:
                for j in range(i+1,len(l)):
                    liste.append(l[j])
                    l.append(0)
                for k in range(i+2,len(l)):
                    a=
                    l[k]=liste[a]
    print(l)
    
insererval([1,2,3,4,5,6,7,8,9,10,11,12,13],7)
    