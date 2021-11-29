import turtle
turtle.speed(50)
turtle.pencolor("cyan")
for i in range(100):
    turtle.circle(5 * i)
    turtle.circle(-5 * i)
    turtle.right(5)
turtle.exitonclick()