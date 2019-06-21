#Basit rastgele sayı üretme
#Basic random number generate
import time

class RandomNumbGenerate:

    def __init__(self):
        self.deger=0
        self.sayac=0
        self.bosluk=""

    def zamani_al(self):
        mlsnow=time.time()
        mlsnow=int(str(mlsnow).replace(".",""))
        return mlsnow

    def zamani_hesapla(self):
        islem=(self.zamani_al()+3.14)**8-int(self.zamani_al())
        return int(islem)

    def sonuc(self):
        randomliste=int(len(str(self.zamani_hesapla))/2)
        for i in str(self.zamani_hesapla()):
            self.sayac=self.sayac+1
            if(self.sayac==randomliste):
                self.bosluk=self.bosluk+i
        print (self.bosluk)

if __name__=='__main__':
    calistir=RandomNumbGenerate()
    calistir.sonuc()
