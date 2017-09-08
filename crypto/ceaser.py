#Ceaser's crypto
yeni_metin=""
metin=input("Please enter your text:")
anahtar=input("Please enter key:")
secim=input("crypto=1\ndecode=2\n:")
if secim=="1":
	if anahtar.isdigit():
		for i in metin:
			yeni_metin+=str(chr(ord(i)+int(anahtar)))
	else:
		print ("enter numeric key")
elif secim=="2":
	if anahtar.isdigit():
		for i in metin:
			yeni_metin+=str(chr(ord(i)-int(anahtar)))
	else:
		print ("enter numeric key")
print (yeni_metin)