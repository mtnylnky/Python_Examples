#Pyqt Dersleri 20.06.17

#Pyqt language translator programming
# Connect language database and column name and language like
from PyQt4.QtGui import *
import sqlite3

connectt=sqlite3.connect("language.db")#change you database name
cur=connectt.cursor()

diller=("İngilizce","Türkçe")#languages show for combobox
uygulama=QApplication([])
window=QWidget()
window.setWindowTitle("Translator")
language1=QComboBox()
language1.addItems(diller)
first=QLineEdit()
label1=QLabel("Bu dilden")
label2=QLabel("Bu dile")
language2=QComboBox()
language2.addItems(diller)
girdi=QLineEdit()
cikti=QLineEdit()

def cevir():
    cikti.clear()
    iid=""
    text=girdi.text()
    first_lang=language1.currentText()
    second_lang=language2.currentText()
    research=cur.execute("SELECT id FROM language WHERE {} like '{}'".format(first_lang,text))
    for i in research.fetchone():
        iid=i
    iid=str(iid)#Yukarıdaki satır fetchall olursa iid=iid[1]
    complete=""
    findsearch=cur.execute("SELECT {} FROM language WHERE id== {}".format(second_lang,iid))
    for i in findsearch.fetchone():
        complete=str(i)
    cikti.insert(complete)

language1.activated.connect(cevir)#combobox değiştiğinde değiştirmek için
language2.activated.connect(cevir)
#girdi.returnPressed.connect(cevir)#lineedit üzerinde enter tuşuna basıldığı zaman değiştirmek için
girdi.textEdited.connect(cevir)#lineedit üzerinde işlem değiştikçe buda değişir

yuzey=QGridLayout()
yuzey.addWidget(language1,1,0)
yuzey.addWidget(language2,1,1)
yuzey.addWidget(label1,0,0)
yuzey.addWidget(label2,0,1)
yuzey.addWidget(girdi,2,0)
yuzey.addWidget(cikti,2,1)

window.setLayout(yuzey)
window.show()
uygulama.exec()
"""
from PyQt4.QtCore import *
from PyQt4.QtGui import *
uygulama=QApplication([])
pencere=QWidget()
pencere.setWindowTitle("Veri Alma İşlemleri")
bilgi=QLabel("Lütfen isminizi Giriniz:")
ad=QLineEdit()
yaz=QPushButton("Bastır")
def degis():
    if ad.text().isalpha():
        bilgi.setText("Merhaba {0}".format(ad.text()))
    else:
        bilgi.setText("Hatalı Karakter")
yaz.pressed.connect(degis)
yuzey=QHBoxLayout()
yuzey.addWidget(bilgi)
yuzey.addWidget(ad)
yuzey.addWidget(yaz)
pencere.setLayout(yuzey)
pencere.show()
uygulama.exec()
"""


"""
from PyQt4.QtGui import *
from PyQt4.QtCore import *
uygulama=QApplication([])
pencere=QWidget()
pencere.setWindowTitle("Merhaba")
combo=QComboBox()
metin="Ali","Bali","Dali"
combo.addItems(metin)
yuzey=QHBoxLayout()
yuzey.addWidget(combo)
pencere.setLayout(yuzey)
pencere.show()
uygulama.exec()
"""


"""
from PyQt4.QtCore import *
from PyQt4.QtGui import  *
uygulama=QApplication([])
pencere=QWidget()
buton=QPushButton("Dokun")
yazi=QLabel("Merhaba")
def degis():
    yazi.setText("Ankara")
buton.pressed.connect(degis)
hepsi=QHBoxLayout()
hepsi.addWidget(yazi)
hepsi.addWidget(buton)
pencere.setLayout(hepsi)
pencere.show()
uygulama.exec()
"""

"""
#Pyqt uygulamaları
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4.QtCore import SIGNAL


uygulama=QApplication([])
pencere=QWidget()
yazi=QLabel("Deneme yazısı")
bas=QPushButton("Dokun")
def vurgitsin():
    yazi.setText("Merhaba")
pencere.connect(bas, SIGNAL("pressed()"), vurgitsin)
bas.pressed.connect(vurgitsin)
#Butona işlem atamada ister SIGANL i içeri aktarıp pencere.connect ile
#ister de butona direkt atayarak yapabiliriz.
hepsi=QHBoxLayout()
hepsi.addWidget(yazi)
hepsi.addWidget(bas)
pencere.setLayout(hepsi)
pencere.setWindowTitle("Deneme işlemleri")
pencere.show()
uygulama.exec()
"""


"""
uygulama=QApplication([]) #Uygulamayı başlatıyoruz bir nevi programı
pencere=QWidget() #pencereyi oluştur
yazi=QLabel("Merhaba") #yazı ekle
yuzey=QHBoxLayout() #eklediklerni ekranda bir yere koy
yuzey.addWidget(yazi) #tek tek ekle
pencere.setLayout(yuzey) #ekleme yüzeyini penceerenin içine koy
pencere.setWindowTitle("Deneme") #Pencereye başlık ver
pencere.show() #pencereyi göster
uygulama.exec() #uygulamayı çalıştır
"""