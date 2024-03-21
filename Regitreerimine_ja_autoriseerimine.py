from MyModul import *
kasutaja=["Valeria","Dasha","Marina","Masha","Sasha"]
paroolid=["va123leria","dasha543","marina.o777","masha.0908","sasha#333"]
while True :
    print("1-registreerimine\n2-autoriseerimine\n3-nime või parooli muutmine\n4-unustanud parooli taastamine\n5-lõpetamine.\n") #4-nime või parooli muutmine/n5-unustanud parooli taastamine/n
    vastus=int(input())
    if vastus==1:
        registreerimine(kasutaja,paroolid)
        loe_failist(kasutaja,paroolid)
        kirjuta_failisse(kasutaja,paroolid)
    if vastus==2:
        autoriseerimine(kasutaja,paroolid)
        loe_failist(kasutaja,paroolid)
        kirjuta_failisse(kasutaja,paroolid)
    if vastus==3 :
        print(kasutaja,paroolid)
        nime_või_parooli_muutmine(kasutaja,paroolid)
        loe_failist(kasutaja,paroolid)
        kirjuta_failisse(kasutaja,paroolid)
    if vastus==4 :
        nimi=input("Mis on sinu kasutajanimi on? ")
        if nimi in kasutaja :
            email=input("Sisesta sinu email : ")
            unustanud_parooli_taastamine(kasutaja,paroolid [kasutaja.index(nimi)])
    if vastus==5 :
        print("Head aega!")
