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
circle.hideturtle()


def paintCircle(color,r):
    circle.color(col)
    circle.begin_fill()
    circle.pencolor(color)

    circle.penup()
    circle.goto(0, -r)
    circle.pendown()
    circle.circle(r)
    circle.end_fill()

ls = 0
for i in range(100):
    col = random.choice(colors)
    ls = ls + 30
    paintCircle(col, ls)





turtle.exitonclick()