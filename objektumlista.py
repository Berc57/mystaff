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

# üres objektumlista létrehozása amiben nobeldijak tipusu változó van

osszesnobeldijas: list[nobeldijak] = []

f.readline()
for sor in f:
    ember = nobeldijak(sor.strip())
    osszesnobeldijas.append(ember)
print(len(osszesnobeldijas))

print(osszesnobeldijas[10].nev)

for egy in osszesnobeldijas:
    print(egy.ev)
    
for i in range(osszesnobeldijas):
    print(i)