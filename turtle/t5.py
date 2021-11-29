import turtle

polygon = turtle.Turtle()
num_sides = 6
side_length = 100
angle = 360 / num_sides
polygon.color("green", "red",)

polygon.begin_fill()

for i in range(num_sides):
    polygon.forward(side_length)
    polygon.left(angle)
polygon.end_fill()
turtle.exitonclick()