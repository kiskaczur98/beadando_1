karakter = input("Add meg keresett karakterláncot! ")
karaktsor = input("Add meg a karaktersorozatot, amiben keresni kell!")

def keres(karakter, karaktsor):
    hossz = len(karakter)
    db = 0
    for i in range(len(karaktsor)-hossz+1):
        if karakter == karaktsor[i:(i+hossz)]:
            db += 1
    return db

print(keres(karakter, karaktsor))