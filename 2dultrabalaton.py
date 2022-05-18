file = open("ub2017egyeni.txt","r",encoding="utf-8")
lista = []
file.readline()

for sor in file:
    egyadat = sor.strip().split(";")
    lista.append(egyadat)

count0 = 0

for i in lista:
    if i[1] == "1":
        count0 += 1
        
print(count0)
























file.close()