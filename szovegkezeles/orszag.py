# bemenet azonnali nagy kezdőbetűre alakítása
orszag = input("Adjon meg egy országot: ").capitalize()

# Szlov-val kezdődik-e
if orszag.startswith("Szlov"):
    print("Az ország Szlov-val kezdődik.")

# ia-ra végződik-e
if orszag.endswith("ia"):
    print("Az ország ia-ra végződik.")

# az ország nevében van-e é betű
if "é" in orszag:
    print("Az ország nevében benne van az é betű.")