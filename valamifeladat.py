class eredmeny:
    nev: str
    rajtszam: int
    kategoria: str
    ido: str
    tavSzazalek: int
    
    def __init__(self, sor: str) -> None:
        adatok = sor.split(";")
        self.nev = adatok[0]
        self.rajtszam = int(adatok[1])
        self.kategoria = adatok[2]
        self.ido = adatok[3]
        self.tavSzazalek = int(adatok[4])        
        

file = open("ub2017egyeni.txt", "r", encoding="utf-8")

noidb = 0
minSzazalek =  100

file.readline()
for sor in file:
    egyAdat = eredmeny(sor)
    print("neve:", egyAdat.nev,"ideje:", egyAdat.ido)
    if egyAdat.kategoria == "Noi" and egyAdat.tavSzazalek == 100:
        noidb = noidb + 1
    if egyAdat.tavSzazalek < minSzazalek:
        minSzazalek = egyAdat.tavSzazalek
        
print("Ennyi női versenyző volt aki teljes távot teljesítette:", noidb)
print("Ennyi volt a legkevesebb százaléka a futott távnak:", minSzazalek)

file.seek(0)
file.readline()

osszeseredmeny:list[eredmeny]=[]

for sor in file:
    egyeredmeny = eredmeny(sor.strip())
    # a létrejött eredményt hozzáfűzöm a listához
    osszeseredmeny.append(egyeredmeny)
print("A listában", len(osszeseredmeny), "eredmény van")

file.seek(0)
file.readline()

# 4 es feladat

ido = osszeseredmeny[0].ido.split(":")
oraban = (int(ido[0])*3600 + int(ido[1])*60 + int(ido[2])) / 3600
print(oraban)

# 5 ös feladat

def idoOraban(idoer:str):
    return (float(ido[0])*3600 + float(ido[1])*60 + float(ido[2])) / 3600

print(idoOraban(ido))

# 6 os feladat

file.seek(0)
file.readline()
lista1 = []
count = 0
idohoz = 0

for egyAdat in osszeseredmeny:
    if egyAdat.kategoria == "Ferfi" and egyAdat.tavSzazalek == 100:
        count += 1
        idohoz += idoOraban(egyAdat.ido)
print(count)
print(ido)

# 7 es feladat

file.seek(0)
file.readline()
szamlalo = 0

for i in range(1,len(osszeseredmeny)-1):
    if osszeseredmeny[i].tavSzazalek == 100 and osszeseredmeny[i-1].tavSzazalek < 100 and osszeseredmeny[i+1].tavSzazalek < 100:
        print(osszeseredmeny[i].nev)
        szamlalo += 1
print("Ennyi találat:", szamlalo)

##################################

keresettnev = str(input("Nevet ird ide"))

bennevane = False
teljesitette = False

for egyAdat in osszeseredmeny:
    if egyAdat.nev == keresettnev:
        bennevane = True
        if egyAdat.tavSzazalek == 100:
            teljesitette = True
        
        
if bennevane and teljesitette:
    print("szerepel, 100 százalékot teljesített")
elif bennevane and teljesitette == False:
    print("szerepel de nem teljesítette")
else:
    print("nem szerepel")