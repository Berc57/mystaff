from xmlrpc.client import boolean


class Haromszog:
    a: int
    b: int
    c: int
    
    # konstruktor
    def __init__(self, sorom) -> None:
        self.a = int(sorom[0])
        self.b = int(sorom[1])
        self.c = int(sorom[2])    
        
    # osztály metódusa: szöveggel visszatérve megmondja, hogy a számok háromszöget alkotnak-e    
    def haromszoge(self) -> str:
        if self.a<self.b+self.c and self.b<self.a+self.c and self.c<self.a+self.b:
            return "Háromszöget alkotnak"
        else:
            return "Nem alkotnak háromszöget."
    
    # osztály metódusa: egész számként visszaadja a háromszög kerületét
    def kerulet(self)-> int:
        return self.a + self.b + self.c
    
    def derekszoge(self) -> boolean:
        return self.a*self.a+self.b*self.b == self.c*self.c

file = open("haromszog.txt", "r", encoding="utf-8")
file.readline()
lista = []

for sor in file:
    egyadat = sor.strip().split("*")
    lista.append(egyadat)
    
print(lista)

for item in lista:
    print(item)
    EgyHaromszog = Haromszog(item)
    
bekertSzamok = []
x = int(input("A szám szerepel e:"))

for i in range(3):
    szam:int = int(input("Add meg a háromszög oldalát:"))
    bekertSzamok.append(szam)
    if szam == x:
        print("Szerepel a számok közt", x)
    else:
        print("Nem szerepel a számok közt", x)
    
egyHaromszog = Haromszog(bekertSzamok)

print(egyHaromszog.derekszoge())
