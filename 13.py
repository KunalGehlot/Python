import tkinter
import tkinter.messagebox

tki = tkinter.Tk()


def trigger():
    tkinter.messagebox.showinfo("Tasty buns", "BANANA")


# B = Button(Master, Opetions....)
B = tkinter.Button(tki, text="Click", command=trigger,
                   font='calibri', bd=12, bg='green', activeforeground='blue')

B.pack()

# tki.mainloop()
