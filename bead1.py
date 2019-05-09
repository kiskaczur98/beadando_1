# Minden pozitív szám felírható kettő pozitív (plusz nulla) hatványainak összegeként.
# Írjon függvényt, amely egy adott n szám esetén egy rendezett listában visszaad a
# számokat, amelyekre kell kettőt emelni és a hatványok összege n.

while True:
    try:
        def elso_feladat(szam):
            hatvany=0
            binaris=list(str(bin(szam)[2:]))
            kitevok=[]
            for i in range(len(binaris)-1,-1,-1):
                if binaris[i]=='1':
                    kitevok.append(hatvany)
                print(binaris[i],"2^",hatvany)
                hatvany=hatvany+1
            return kitevok

        n=int(input('Adj meg egy számot!'))
        print(elso_feladat(n))
    except ValueError:
        print("Nem megfelelő a megadott érték!")