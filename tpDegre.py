class degre_sexa:
    def __init__(self):
        self.degre = 0
        self.minute = 0
        self.seconde = 0
        
def ajouterval(val):
    print("Valeur des degre:")
    val.degre=int(input())
    print("Valeur des minutes:")
    val.minute=int(input())
    print("Valeur des secondes:")
    val.seconde=int(input())
    return val
        
def affichage(sexa):
    print("Valeur des degre:",sexa.degre)
    print("Minutes:",sexa.minute)
    print("Secondes:",sexa.seconde)
        
def sexa_vers_dec(s):
    return (s.degre+(s.minute/60)+(s.seconde/3600))

def dec_vers_sexa(d:float):
    c=str(d)
    s=degre_sexa
    s.degre=int(c.split('.')[0])
    v=d-s.degre
    v2=v*60
    v3=str(v2)
    s.minute=int(v3.split('.')[0])
    s.seconde=int((float(v2)-s.minute)*60)
    return s
    
def suivante(s:degre_sexa):
    s.seconde=s.seconde+1
    if s.seconde>59:
        s.seconde=0
        s.minute=s.minute+1
    if s.minute>59:
        s.minute=0
        s.degre=s.degre+1
    return s

def Prog():
    latitude=degre_sexa
    latitude.degre=int(input("Insérer les degrées:"))
    latitude.minute=int(input("Insérer les minutes:"))
    latitude.seconde=int(input("Insérer les secondes:"))
    print(latitude.degre,'"',latitude.minute,"'",latitude.seconde,'"')
    latitudedec=sexa_vers_dec(latitude)
    print(latitudedec,'deg')
    latitude2=suivante(latitude)
    print("latitude suivante:")
    print(latitude2.degre,'"',latitude2.minute,"'",latitude2.seconde,'"')
    latitude2dec=sexa_vers_dec(latitude)
    print(latitude2dec,'deg')
    
Prog()
    
    




        