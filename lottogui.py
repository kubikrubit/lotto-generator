from tkinter import *
from tkinter.messagebox import *


def printer(event):
    global s # use global StringVar to show the results
    import random

    r_sample = random.sample(range(a.get(), b.get() + 1), c.get())

    # set the s variable with the random sample
    s.set(",".join(map(str,r_sample)))
    return

def close_win():
     if askyesno("Exit", "Do you want to quit?"):
          root.destroy()
 
def about():
     showinfo("Editor", "Numbers Generator v1 (created by 5n31d3R aka kubikrubit)")

root = Tk()

m = Menu(root)
root.config(menu=m)

fm = Menu(m)
m.add_cascade(label="Menu", menu=fm)
fm.add_command(label="About", command=about)
fm.add_command(label="Exit", command=close_win)

s = StringVar()

# IntVars added here
a = IntVar()
b = IntVar()
c = IntVar()

fra1 = Frame(root,width=900,height=900)
fra1.pack()

lab = Label(fra1, text="Minimum", font="Arial 10")
ent = Entry(fra1,width=30,bd=5, textvariable=a)
lab.pack()
ent.pack()

lab = Label(fra1, text="Maximum", font="Arial 10")
ent = Entry(fra1,width=30,bd=5, textvariable=b)
lab.pack()
ent.pack()

lab = Label(fra1, text="Quantity", font="Arial 10")
ent = Entry(fra1,width=30,bd=5, textvariable=c)
lab.pack()
ent.pack()


but = Button(fra1, text="GO!",
             width=20,height=5,
             bg="green",fg="yellow")
but.bind("<Button-1>", printer)
but.pack()

lab = Label(fra1, text="Result", font="Arial 10")
ent = Entry(fra1,width=30,bd=5, textvariable=s)
lab.pack()
ent.pack()

lab = Label(fra1, text="[-_-]", font="Arial 20 bold")
lab.pack()

root.mainloop()
