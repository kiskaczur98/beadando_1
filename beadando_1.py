
def elso_feladat(szam):
    hatvany=0
    binaris=list(str(bin(szam)[2:]))
    kitevok=[]
    for i in range(len(binaris)-1,-1,-1):
        if binaris[i]=='1':
            kitevok.append(hatvany)
        hatvany=hatvany+1
    return kitevok
while True:
    try:
        n=int(input('Adj meg egy számot!'))
        print(elso_feladat(n))
        break
    except ValueError:
        print("Nem megfelelő a megadott érték!")