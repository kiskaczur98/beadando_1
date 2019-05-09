# Minden pozitív szám felírható kettő pozitív (plusz nulla) hatványainak összegeként.
# Írjon függvényt, amely egy adott n szám esetén egy rendezett listában visszaad a
# számokat, amelyekre kell kettőt emelni és a hatványok összege n.

while True:
    def elso_feladat(szam):
        hatvany=0
        binaris=list(str(bin(szam)[2:]))
        kitevok=[]
        for i in range(len(binaris)-1,-1,-1):
            if binaris[i]=='1':
                kitevok.append(hatvany)
            hatvany=hatvany+1
        return kitevok
    try:
        n=int(input('Adj meg egy számot!'))
        print(elso_feladat(n))
        break
    except ValueError:
        print("Nem megfelelő a megadott érték!")