import turtle
#СДЕЛАТЬ МИШЕНЬ
turtle.title("Drawing")
circle = turtle.Turtle()
circle.shape("turtle")
circle.pensize(5)
circle.pencolor("red")
num = 400
circle.dot(num)
circle.penup()
circle.goto(0, -num)
circle.pendown()
circle.circle(num)




turtle.exitonclick()