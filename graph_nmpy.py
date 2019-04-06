import numpy as np
import matplotlib.pyplot as plt

#Veri Görselleştirme
fig_size = [16,9]
plt.figure(figsize=fig_size)
y=[10,5,3,12,20,32,44,16,2,11,12,19]
x_labels=['Ocak','Şubat','Mart','Nisan','Mayıs',"Haziran","Temmuz","Ağustos","Eylül","Ekim","Kasım","Aralık"]
x_pos=np.arange(len(y))
plt.bar(x_pos,y)#barh => Horizantal graph(Yatay grafik)
plt.title("Satış Grafiği")
plt.xticks(x_pos,x_labels)
plt.xlabel("Aylar")
plt.ylabel("Miktar")
plt.show();