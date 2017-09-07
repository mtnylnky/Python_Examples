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
    iid=str(iid)
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
