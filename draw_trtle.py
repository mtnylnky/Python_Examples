#Python çizim kütüphanesi
import turtle

#Kare çizimi
wn = turtle.Screen()
alex = turtle.Turtle()
alex.forward(150)
alex.left(90)
alex.forward(150)
alex.left(90)
alex.forward(150)
alex.left(90)
alex.forward(150)

#Çok kenarlı yıldız
from turtle import *
color('red', 'yellow')
begin_fill()
while True:
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break
end_fill()
done()
