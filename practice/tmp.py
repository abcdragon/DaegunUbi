from tkinter import *
from tkinter import messagebox

root = Tk()

lbl = Label(root, text="이름")
lbl.grid(row=0, column=0)

txt = Entry(root)
txt.grid(row=0, column=1)

def okClick():
    name = txt.get()
    messagebox.showinfo("이름", name)
btn = Button(root, text="OK", width=15, command=okClick)
btn.grid(row=1, column=1)

root.mainloop()