from MyModul import *
kasutaja=["Valeria","Dasha","Marina","Masha","Sasha"]
paroolid=["va123leria","dasha543","marina.o777","masha.0908","sasha#333"]
while True :
    vastus=int(input("1-registreerimine/n2-autoriseerimine/n3-nime või parooli muutmine/n4-unustanud parooli taastamine/n5-lõpetamine./n")) #4-nime või parooli muutmine/n5-unustanud parooli taastamine/n
    if vastus==1:
        registreerimine(kasutaja,paroolid)
    if vastus==2:
        autoriseerimine(kasutaja,paroolid)
    if vastus==3 :
        print(kasutaja,paroolid)
        nime_või_parooli_muutmine(kasutaja,paroolid)
    #    print("Head aega!")
    #if vastus==4 :
    #    nvpm=input("Mida sa tahad muutumine?/nN-nime/nP-parooli")
    #    print()
    #if vastus=="N" 
