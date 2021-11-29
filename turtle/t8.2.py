import random
import turtle
#СДЕЛАТЬ МИШЕНЬ
turtle.title("Drawing")
circle = turtle.Turtle()
circle.shape("turtle")
circle.pensize(5)
circle.pencolor("red")
circle.speed(10)
colors = ["red", "orange", "blue", "black", "purple"]

circle.dot(20)

def paintCircle(color,r):
    circle.pencolor(color)
    circle.penup()
    circle.goto(0, -r)
    circle.pendown()
    circle.circle(r)


ls = 0
for i in range(100):
    ls = ls + 30
    paintCircle(random.choice(colors), ls)


paintCircle("green", 60)


paintCircle("red", 90)

paintCircle("cyan", 120)


turtle.exitonclick()