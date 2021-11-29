from tkinter import *

def clicked():
    lbl.configure(text="Я же просил")

window = Tk()
window.title("приложение")
window.geometry('740x740')
window.resizable(True,True)

btn = Button(window, text = "Не нажимать!", command=clicked, bg="black", fg="white")

btn.grid(column = 1, row = 0)

lbl = Label(window, text="Привет", font=("Arial Bold", 40))
lbl.grid(column=0, row=0)

window.mainloop()