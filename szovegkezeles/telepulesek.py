telepulesek = ["Budapest", "Miskolc", "Debrecen"]
for telepules in telepulesek:
    print(f"{telepules} összesen {len(telepules)} karakterből áll.")

#tetszőleges számú településsel kibővíteni
#kiválogatni a megfelelő szövegeket
#leghosszabb nevű település megállapítása

#elemek felvétele
uj_telepules = input("Adjon meg egy településnevet: ")
while len(uj_telepules) > 0:
    telepulesek.append(uj_telepules)
    uj_telepules = input("Adjon meg egy településnevet: ")

#kiírjuk az összes települést, amiben szerepel a "szent"
for telepules in telepulesek:
    if "szent" in telepules.lower():
        print(telepules)

#leghosszabb nevű település
leghosszabb = ""
for telepules in telepulesek:
    if len(telepules) > len(leghosszabb):
        leghosszabb = telepules

print(f"A leghosszabb nevű település {leghosszabb}.")