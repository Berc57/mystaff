# Írasd ki az összes sort

file = open("adatok.txt", "r")
for sor in file:
    print("Sor:",sor)

# Olvasd be a fájl első sorát, amely megadja, hogy összesen hány adatsor van.

file.seek(0,0)
print("Sorok száma:", file.readline()) 

# Írasd ki egy sorokszama.txt fájlba a sorok számát.

file.seek(0,0)
file2 = open("sorokszama.txt", "w")
file2.write(file.readline())


# Írasd ki külön az adatsorokat és külön az összes sorok számát.

file.seek(0,0)
file.readline()
for sor in file:
    print("Sorok száma a 2. sortól:",sor)



# a sorokban levő 3 szám szorzatát írd ki. Csak az adatsorokkal dolgozz!

file.seek(0,0)
file.readline()

lista = []
for i in range(5):
    i = file.readline().strip().split()
    szorzat = file.readline(int(i[0])*int(i[1])*int(i[2]))
    print("Szorzat:", szorzat)
    