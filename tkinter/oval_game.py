from tkinter import*

root = Tk()
canvas = Canvas(width=300, height=300, bg = 'white')
canvas.focus_set() #передать фокус виджету.
canvas.pack()#

ball = canvas.create_oval(140,140,160,160, fill='green')

#all = canvas.create_line(100,100,100,100, fill='green')

"""
canvas.bind('<Up>', lambda event: canvas.move(ball, 0, -10))
canvas.bind('<Down>', lambda event: canvas.move(ball, 0, 10))
canvas.bind('<Left>', lambda event: canvas.move(ball, -10, 0))
canvas.bind('<Right>', lambda event: canvas.move(ball, 10, 0))
"""


root = Tk()
canvas = Canvas(width=300, height=300, bg = 'white')
canvas.focus_set() #передать фокус виджету.
canvas.pack()#

ball = canvas.create_oval(150,150,170,170, fill='green')







root.mainloop()


