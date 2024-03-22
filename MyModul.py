import smtplib, ssl
from email.message import EmailMessage
import random 
import re

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
            else:
                print("Viga, sama nimega kasutaja on juba olemas!") 
        while True :
            valik=input("Milline parooli sa tahad? 1-autopass 2-mypass")
            if valik=="1" :
                parool=autopass()
                p.append(parool)
                print("Olete registreeritud!")
                break
            if valik=="2":
                parool=mypass(k)
                p.append(parool)
                print("Olete registreeritud!")
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
            

def unustanud_parooli_taastamine(k,p):
    """
    """
    smpt_server="smtp.gmail.com"
    port=587 #for starttls
    sender_email="daragalcenko3@gmail.com" 
    #to_email="marina.oleinik@tthk.ee"
    password=input("Type ur password and press enter :")
    context=ssl.create_default_context()
    #Create a secure SSL context
    #context= ssl.create_default_context()
    #msg="Tere tulemast!"
    msg=EmailMessage()
    msg.set_content("Tere tulemast! " +str(p))
    msg['Subject']="Kirja teema"
    msg['From']="daragalcenko3@gmail.com"
    msg['To']="allikvaleria@gmail.com"                      #"marina.oleinik@tthk.ee"

    #Try to log in to server and send email
    try:
        server= smtplib.SMTP(smpt_server,port)
        server.ehlo() #Can be omitted
        server.starttls(context=context) #Secure the connection
        server.ehlo() #Can be omitted
        server.login(sender_email,password)
        #server.sendmail(sender_email,to_email,msg)
        server.send_message(msg)
    except Exception as e :
        #Print any error massages to stdout
        print(e)
    finally:
        server.quit()


def loe_failist(kasutaja,paroolid):
    """Loeme failist read ja salvestame järjendisse. Funktsioon tagastab järjend
    :param str fail:
    rtype: list
    """
    fail="Kasutajad_ja_paroolid"
    f=open(fail,'r',encoding="utf-8") #try
    järjend=[kasutaja,paroolid]
    for rida in f:
        järjend.append(rida.strip())
    f.close()
    return järjend
def kirjuta_failisse(fail:str,kasutaja,paroolid):
    """
    funktioon ümber kirjutab andmed failis
    """
    fail="Kasutajad_ja_paroolid"
    try :
        f=open(fail,'w',encoding="utf-8")
        for i in range(len(kasutaja)):
            k=kasutaja[i]
            p=paroolid[i]
            f.write(f"{k}  {p}"+"\n")
    except: 
            print("Viga")

    kirjuta_failisse("Text.txt")

        



import string
def mypass(k: int):
    while True :
            parool=input("Sisesta parooli : ")
            if len(parool)<8:            
                print("Parool peab koosnema vähemalt 8 tähemärgist")
                continue        
            elif re.search("[1,2,3,4,5,6,7,8,9,0]", parool) is None:
                print("Numbreid pole")   
                continue
            elif re.search("[a-z]", parool) is None:      
                print("Paroolis ei ole väiketähti") 
                continue       
            elif re.search("[A-Z]", parool) is None:
                print("Paroolis pole suuri tähti")            
                continue
            elif re.search("[$@^=.,:;!_*-+()/#¤%&]", parool) is None:        
                print("Paroolis pole erimärke")
                continue      
            else:
                print("Teie parool on turvaline!")         
                return parool


    
def autopass():
    str0=".,:;!_*-+()/#¤%&"
    str1 = '0123456789'
    str2 = 'qwertyuiopasdfghjklzxcvbnm'
    str3 = str2.upper()
    print(str3) # 'QWERTYUIOPASDFGHJKLZXCVBNM'
    str4 = str0+str1+str2+str3
    print(str4)
    ls = list(str4)
    print(ls)
    random.shuffle(ls)
    print(ls)
    # Извлекаем из списка 12 произвольных значений
    paroolid = ''.join([random.choice(ls) for x in range(12)])
    # Пароль готов
    print(paroolid)
    return paroolid
