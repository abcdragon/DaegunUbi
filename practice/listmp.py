from tkinter import *

master = Tk()

listbox = Listbox(master)
listbox.pack()

txt = Entry(master)
txt.pack()

def event():
    listbox.insert(END, txt.get())
    txt.delete(0, 'end')
btn = Button(master, text="insert", width=15, command=event)
btn.pack()

listbox.insert(END, "a list entry")
listbox.insert(END, "bbb")

master.mainloop()