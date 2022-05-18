class Helyjegy:
    ulesszam: int
    kmmettol: int
    kmmeddig: int
    
    def __init__(self, sor: str) -> None:
        adatok = sor.split(" ")
        self.ulesszam = int(adatok[0])
        self.kmmettol = int(adatok[1])
        self.kmmeddig = int(adatok[2])
        
file = open("eladott.txt", "r", encoding="utf-8")
file.readline()

lista = []

for sor in file:
    egyadat = Helyjegy(sor.strip())
    lista.append(egyadat)
    
file.close()

print(len(lista))