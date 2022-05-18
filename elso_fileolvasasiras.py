from re import I


file = open("haromszogek.txt", "r", encoding= "utf-8")
for sor in file:
    print(sor)

file.seek(0,0)

x = file.readline().split()
lista = x
print(lista)

print("Második sor:", file.readline())

lista2 = []
sor3 = file.readline().strip().split(" ")
lista2 = sor3
print("A 3. sor listában:", lista2)

print("A 3. sor legnagyobb száma:", max(lista2))
print("A 3. sor 2. száma:", lista2[1])

fileszam = open("ki.txt", "w")
fileszam.write(lista2[1])

file.seek(0,0)

for i in range(4):
    print(file.readline())



file.close()