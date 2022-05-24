"""
Név;Osztály;Első nap;Utolsó nap;Mulasztott órák
Balogh Péter;6a;1;1;5
Horváth Judit;5a;1;1;5
Juhász János;6a;1;1;5
Lengyel Krisztina;6b;1;1;6
"""

class Szeptember:
    def __init__(self,sor):
        nev,osztaly,elso_nap,utolso_nap,mulasztott_orak = sor.strip().split(";")
        self.nev                = nev
        self.osztaly            = osztaly
        self.elso_nap           = elso_nap
        self.utolso_nap         = utolso_nap
        self.mulasztott_orak    = int(mulasztott_orak)

with open("szeptember.csv", encoding="UTF-8")as f:
    fejlec  = f.readline()
    lista   = [Szeptember(sor) for sor in f]

#2.feladat
mulasztas = [sor.mulasztott_orak for sor in lista]

print(f"2. feladat \n      Összes mulasztott órák száma: {sum(mulasztas)}.")

#3.feladat
print("3.feladat:")
nap     = input("Kérem adjon meg egy napot: ")
tanulo  = input("Tanuló neve: ")

#4. feladat 
print("4.feladat:")
hianyzasok = [sor.nev for sor in lista if sor.nev == tanulo]

if len(hianyzasok) != 0:
    print("A tanuló hiányzott szeptemberben")
elif len(hianyzasok) == 0:
    print("A tanuló nem hiányzott szeptemberben")

#5.feladat
hianyzott_nap = [sor for sor in lista if sor.elso_nap == nap]
print(f"5. feladat: Hiányzók 2017.09.{nap}-n:")
[print(f"               {sor.nev} {sor.osztaly}")for sor in hianyzott_nap]
