import turtle
import random
pen=turtle.Turtle()
wn=turtle.Screen()
wn.bgcolor('black')
ang=[59,61,60,58]
angles=random.choice(ang)

color=["green", "red", "blue", "purple", "yellow"]
pen.speed(10)
for i in range(200):
    pen.color(color[i%5])
    pen.pensize(i/10+1)
    pen.forward(i)
    pen.left(angles)
print(angles)
input('')
