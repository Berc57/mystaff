class Merkozes:
    fordulo: int
    hazaigol: int
    vendeggol: int
    hazaifelidogol: int
    vendegfelidogol: int
    hazaicsapat: str
    vendegcsapat: str
    
    def __init__(self, sor:str) -> None:
        adatok = sor.split(" ")
        self.fordulo = int(adatok[0])
        self.hazaigol = int(adatok[1])
        self.vendeggol = int(adatok[2])
        self.hazaifelidogol = int(adatok[3])
        self.vendegfelidogol = int(adatok[4])
        self.hazaicsapat = (adatok[5])
        self.vendegcsapat = (adatok[6])
        
file = open("meccs.txt","r",encoding="utf-8")

file.seek(0)
file.readline()

lista = []

for i in file:
    egyeredmeny = Merkozes(i.strip())
    lista.append(egyeredmeny)
print("Összesen ennyi meccs volt", len(lista))

forudlohanyadik = int(input("Add meg egy forduló számát"))

for egyadat in lista:
    if forudlohanyadik == egyadat.fordulo:
        print(egyadat.hazaicsapat)
        
csapatnev = str(input("Add meg a csapat nevét"))
count = 0

for i in lista:
    if csapatnev == i.hazaicsapat or csapatnev == i.vendegcsapat:
        count += 1

if count != 0:
    print("Van", csapatnev, "nevű csapat")
else:
    print("Nincs", csapatnev, "nevű csapat")
    
hazaifel = 0
vendegfel = 0
hazai = 0
vendeg = 0

for i in lista:
    if i.hazaifelidogol > i.vendegfelidogol:
        hazaifel += 1
    elif i.hazaifelidogol < i.vendegfelidogol:
        vendegfel += 1
    for i in lista:
        if i.hazaigol > i.vendeggol:
            hazai += 1
        elif i.hazaigol < i.vendeggol:
            vendeg += 1
if 2 > 3 and 1 < 4:
    print("Sikerült megforditani a meccs eredményét")

gol = 0

for i in lista:
    if i.vendegcsapat == "Nyulak":
        gol = gol + i.vendeggol
        
print("Ennyi gólt lőttek a nyulak vendégként:", gol)































file.close()