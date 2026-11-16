szamok = [6, 3, -5, 11]
print(szamok[1])

nev = "Takács László"
# az ötödik karakter kiírása
print(nev[4])

# az utolsó két karakter kiírása
print(nev[-2:])

# harmadik karaktertől a nyolcadik karakterig kiírás
print(nev[2:8])

# a szöveg kibővítése a végén (append helyett +=)
nev += " István"
print(nev)

#minden harmadik karakter kiírása
print(nev[0 : : 3])

n = len(nev)
for i in range(0, n, 3):
    print( nev[i] )

#tükrözés listán
szamok.reverse()
print(szamok)

#tükrözés szövegen
tukrozott = nev[ : : -1]
print(tukrozott)

#kisbetűs, nagybetűs és nagy kezdőbetűs kiírás
kisbetus = nev.lower()
nagybetus = nev.upper()
nagy_kezdobetus = nev.capitalize()

print(kisbetus)
print(nagybetus)
print(nagy_kezdobetus)