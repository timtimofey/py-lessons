import turtle
#СДЕЛАТЬ МИШЕНЬ
turtle.title("Drawing")
circle = turtle.Turtle()
circle.shape("turtle")
circle.pensize(5)
circle.pencolor("red")


circle.dot(20)

def paintCircle(color,r):
    circle.pencolor(color)
    circle.penup()
    circle.goto(0, -r)
    circle.pendown()
    circle.circle(r)


paintCircle("green", 60)


paintCircle("red", 90)

paintCircle("cyan", 120)


turtle.exitonclick()