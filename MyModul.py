#kasutaja=["Valeria","Dasha","Marina","Masha","Sasha"]
def registreerimine(k,p):
    """
    """
    r=input("Tahad registreerida? Jah, Ei ")
    if r=="Jah":
        while True :
            kasutaja=input("Sisesta kasutajanimi : ")
            if kasutaja not in k :
                k.append(kasutaja)
                break
            else :
                print("Viga!") 
        while True :
            paroolid=input("Sisesta parooli : ")
            if paroolid not in p :
                p.append(paroolid)
                print("Te olete registreerunud! ")
                break
    if r=="Ei":
          print("Head aega!") 
    return(k,p)

def autoriseerimine(k,p):
    """
    """
    a=input("Tahad autoriseerimine? Jah, Ei ")
    if a=="Jah":
        while True :
            kasutaja=input("Sisesta kasutajanimi : ")
            if kasutaja not in k :
                k.append(kasutaja)
                break
            else :
                print("Viga!") 
        while True :
            paroolid=input("Sisesta parooli : ")
            if paroolid not in p :
                p.append(paroolid)
                break
            print("Te olete autoriseeritud!")
            break
    if a=="Ei":
        print("Head aega!")

def nime_või_parooli_muutmine(k,p):
    """
    """
    nvpm=input("Tahad kasutajanime või parooli muutmine? Jah, Ei ")
    if nvpm=="Jah":
        kasutaja=input("Sisesta kasutajanimi : ")
        if kasutaja in k: 
            indeks=k.index(kasutaja) 
        nimi_muutumine=input("Mida sa tahad muuta? 1-kasutajanime 2-parooli : ")
    if nimi_muutumine=="1":
        while True:
            kasutaja=input("Sisesta kasutajanimi : ")
            uus_kasutaja=input("Sisesta uus kasutajanimi : ")
            k[indeks]=uus_kasutaja
            print("Sinu uus nimi", uus_kasutaja)
            break
    if nimi_muutumine=="2":
        while True:
            parooli=input("Sisesta parooli : ")
            uus_parooli=input("Sisesta uus parooli : ")
            p[indeks]=uus_parooli
            print("parooli",parooli,"uus parooli",uus_parooli)
            break
