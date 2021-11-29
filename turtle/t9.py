from turtle import*
t = Turtle()
t.screen.setup(800,800)
t.setheading(270)
t.up()
t.goto(-450,0)
t.down()

for i in range(5):

    t.begin_fill()
    t.circle(50,180)
    t.end_fill()
    t.begin_fill()
    t.circle(-50,180)
    t.end_fill()





t.screen.exitonclick()
t.screen.mainloop()