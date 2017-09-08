#-*- coding: utf-8 -*-
import base64
import os
#encoded = base64.b64encode(b'data to be encoded')
#encoded = base64.b64decode(encoded)
#print(encoded)
anahtar="kilit"
def menu():
    print ("------Şifreli Yazılım V.1.0-------")
    print ("Metni Şifrelemek İçin = 1")
    print ("Metnin Şifresini Çözemek için = 2")
while True:
    menu()
    islem=input("İşleminizi Seçiniz:")
    if islem=="1":
        dosyadi=input("Dosya adını ve uzantısını giriniz:(örn: dosya.txt)\n>>>")
        metin=input(str("Şifrelenecek Metini Giriniz:\n>>"))
        password=input("Anahtarı giriniz:")
        if password==anahtar:
            encoded=base64.b64encode(metin.encode())
            text=open(dosyadi,"w")
            text.write(str(encoded))
            text.close()
        else:
            print("Anahtar Hatalı!!!")
    elif islem=="2":
        metin=input("Çözülecek metin dosyası:\n>>")
        password=input("Anahtarı Giriniz:")
        if password==anahtar:
            text=open(metin)
            a=""
            sayac=1
            for i in text.read():
                if sayac==1:
                    sayac=sayac+1
                else:
                    a=a+str(i)
                    sayac=sayac+1
            decoded=base64.b64decode(str(a))
            decoded=decoded.decode('utf-8')
            print(decoded)
        else:
            print("Hatalı Şifre!!!")
    else:
        print("Geçersiz Bir İşlem Girdiniz.")
