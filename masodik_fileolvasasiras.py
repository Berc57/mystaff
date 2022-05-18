class nobeldijak:
    ev: int
    nev: str
    szuletesHalalozas: str
    orszagkod: str
    
    def __init__(self, sor:str) -> None:
        adatok =sor.split(";")
        self.ev = int(adatok[0])
        self.nev = adatok[1]
        self.szuletesHalalozas = adatok[2]
        self.orszagkod = adatok[3]

f = open("orvosi_nobeldijak.txt","r",encoding="utf-8")
    
# 1. Hány Nobel díjas van??

szamlalo = 0

f.readline()

for sor in f:
    print(sor)
    szamlalo += 1
print("Ennyi Nobel díjas van:", szamlalo)

# 2. Hány magyar Nobel díjas van??

f.seek(0)
f.readline()
szamlalo = 0


for sor in f:
    magyar = nobeldijak(sor.strip())
    if magyar.orszagkod == "H":
        szamlalo +=1
print("Ennyi magyar Nobel dijas van:", szamlalo)

# 3. Mikor kapták az első Nobel díjat??
f.seek(0)
f.readline()

ev = 2022
for sor in f:
    elso = nobeldijak(sor.strip())
    if elso.ev < ev:
        ev = elso.ev
print(ev)

# 4. Szerepel e Archibald nevű ember a listában??

f.seek(0)
f.readline()
szamlalo = 0

for sor in f:
    neve = nobeldijak(sor.strip())
    if "Otto" in neve.nev:
        szamlalo += 1
print("Ennyi Otto nevű ember kapott Nobel díjat:", szamlalo)

# 5. Soronként irasd ki soronként, hogy hány éves korában halt meg a díjazott
f.seek(0)
f.readline()
szamlalo = 0

for sor in f:
    ember = nobeldijak(sor.strip())
    evek = ember.szuletesHalalozas.split("-")
    if (evek[1] != ""):
        print(ember.nev,": ", int(evek[1])-int(evek[0]))

f.close()