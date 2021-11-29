import turtle

turtl = turtle.Turtle()

for i in range(30):
    turtl.fd(i * 20)
    turtl.rt(i*10)
    turtl.goto(10, 30)

turtle.exitonclick()
