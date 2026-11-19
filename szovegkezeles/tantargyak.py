tantargyak = ["matematika", "magyar", "történelem", "angol", "testnevelés"]

#soronként kiírás
for tantargy in tantargyak:
    print(tantargy)

uj_tantargy = input("Adjon meg egy tantárgyat, ami még nem szerepel a listában: ")
while len(uj_tantargy) > 0:
    if uj_tantargy in tantargyak:
        print("A tantárgy már szerepel a listában.")
    else:
        tantargyak.append(uj_tantargy)
    uj_tantargy = input("Adjon meg egy tantárgyat, ami még nem szerepel a listában: ")

#írjuk ki az összes tantárgy utolsóelőtti betűjét soronként
for tantargy in tantargyak:
    print(tantargy[-2])

#számolja ki a tantárgyak hány százaléka kezdődik "m" betűvel
megfelelt = 0
osszes = len(tantargyak)
for tantargy in tantargyak:
    if tantargy.startswith("m"):
        megfelelt += 1

szazalek = round(100 * megfelelt / osszes, 2)
print(f"A tantárgyak {szazalek} %-a kezdődik m betűvel.")