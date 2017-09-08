#Ceaser's crypto
yeni_metin=""
metin=input("Please enter your text:")
anahtar=input("Please enter key:")
if anahtar.isdigit():
	for i in metin:
		yeni_metin+=str(chr(ord(i)+int(anahtar)))
else:
	print ("enter numeric key")
print (yeni_metin)