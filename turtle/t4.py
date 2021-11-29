import turtle
tom = turtle.Turtle()
tom.shape("turtle")
tom.color("green", "red",)

tom.begin_fill()

for f in range(6):
    tom.left(75)
    for i in range(4):
        tom.fd(100)
        tom.left(90)

tom.end_fill()







turtle.exitonclick()