class Instant:
    def __init__(self):
        self.heure = 0
        self.minute = 0
        self.seconde = 0
        
def read_Instant():
    instant=Instant()
    print("Entre le nombre d'heure")
    heure=int(input())
    instant.heure=heure
    print("Entrez le nombre de minute")
    minute=int(input())
    instant.minute=minute
    print("Entrez le nombre de seconde")
    seconde=int(input())
    instant.seconde=seconde
    return instant
    
def print_Instant(t:Instant):
    print(t.heure,":",t.minute,":",t.seconde)

def estInstantValide(t:Instant)->bool:
    vrai=True
    if t.heure>24 or t.heure<0:
        vrai=False
    elif t.minute>59 or t.minute<0:
        vrai=False
    elif t.seconde>59 or t.seconde<0:
        vrai=False
    return vrai

def suivant(t:Instant):
    t.seconde=t.seconde+1
    if t.seconde>59:
        t.seconde=0
        t.minute=t.minute+1
    if t.minute>59:
        t.minute=0
        t.heure=t.heure+1
    if t.heure>24:
        t.heure=t.heure-24
    return t

def estPlusRecent(t1:Instant,t2:Instant)->bool:
    recent:bool
    recent=True
    if t1.heure<t2.heure:
        recent=False
    elif t1.heure==t2.heure:
        if t1.minute<t2.minute:
            recent=False
    elif t1.heure==t2.heure and t1.minute==t2.minute:
        if t1.seconde<t2.seconde:
            recent=False
    return recent    

def duree(debut:Instant,fin:Instant)->Instant:
    duree=Instant
    if estPlusRecent(debut,fin):
        raise Exception("Temps final plus récent que temps début")
        print("Temps final plus récent que temps début")
        return None
    else:
        sommedebut=debut.seconde+debut.minute*60+debut.heure*3600
        sommefin=fin.seconde+fin.minute*60+fin.heure*3600
        total=sommefin-sommedebut
        duree.heure=total//3600
        total=total%3600
        duree.minute=total//60
        total=total%60
        duree.seconde=total
        return duree
    



        

        

        
        
    