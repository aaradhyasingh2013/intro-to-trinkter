from tkinter import *
from datetime import date
window= Tk()
window.title("sample window")
window.geometry('400x300')
lbl= Label(text="hello everyone" ,fg="blue",bg="pink",height=1,width=300)
name= Label(text="full name",bg="brown")
n_entry= Entry()
def display():
    name= n_entry.get()
    global massege
    massege="welcome to the application. \n todays date is: "
    gret="hello" + name + "\n"
    t_box.insert(END,gret)
    t_box.insert(END,massege)
    t_box.insert(END,date.today())
t_box= Text(height=3)
btn= Button(text="begun",fg="purple",bg="white",height=1,command=display)
lbl.pack()
name.pack()
n_entry.pack()
btn.pack()
t_box.pack()
window.mainloop()
