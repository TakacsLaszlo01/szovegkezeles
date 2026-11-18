nev = input("Adja meg a nevét: ")
#szóközönként széttagolja egy listába a stringet
reszek = nev.split(" ")

for resz in reszek:
    print(resz)

# második elem első karaktere
print(reszek[1][0])
#"Takács László István" -> ["Takács", "László", "István"]

#monogram építése = minden elem első karakteréből
monogram = ""
for resz in reszek:
    monogram += resz[0].upper()
print(monogram)