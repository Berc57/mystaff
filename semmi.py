#file megnyitása
file = open('orvosi_nobeldijak.txt', 'r',encoding='utf-8')

# lista létrehozása a sorok számára
lista = []


# első sor beolvasása (fejléc, nem csinálunk vele semmit)
file.readline()

#fájl sirainak bejárása 

for sor in file:
     #listához hozzáfűzöm a listává szétdarabolt sort
    lista.append(sor.strip().split(";"))
print(lista)
print(lista[1][3])   


#1. feladat hány angol nobeldíjas van 
print("--- 1. Feladat: ---")
db = 0

for sor in lista:
    if sor[3] == "GB":
        db = db +1
        
print(db)    

# 2. Feladat kik azok akik 1905 előtt kaptak nobeldíjat
print("--- 2. Feladat: ---")
for sor in lista:
    if int(sor[0])<1905:
        print(sor[1])
        
#3. Feladat irasd ki azokat az embereket akikek A-val kezdődik a neve
print("--- 3. Feladat: ---")
for sor in lista:
    if sor[1][0] == "A":
        print(sor[1])
        
#4. Feladat: kik élnek még és hány évesek
print("--- 4. Feladat: ---")
for sor in lista:
    if len(sor[2]) == 5:
        szulev = int(sor[2][1:4])
        print(sor[1],2022 - szulev)