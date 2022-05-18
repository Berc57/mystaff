file = open("orvosi_nobeldijak.txt", "r", encoding="utf-8")
lista = []

file.readline()
for sor in file:
    egyadat = sor.strip().split(";")
    lista.append(egyadat)

count = 0
for i in range(148):
    if lista[i][3] == "GB":
        count += 1

count0 = 0
for i in range(148):
    if lista[i][0] < "1905":
        count0 += 1
        
count1 = 0
for i in range(148):
    if str(lista[i][1]).startswith("A"):
        count1 += 1
        
count2 = 0
for i in range(148):
    if str(lista[i][2]).endswith("-"):
        count2 += 1
        
for sor in lista:
    if sor[2].endswith("-"):
        print("a")


print("Enyi angol van:", count)
print("Ennyien nyertek 1905 előtt",count0)
print("Ennyinek a neve kezdődik A --val", count1)
print("Ennyen nem élnek már", count2)
file.close()