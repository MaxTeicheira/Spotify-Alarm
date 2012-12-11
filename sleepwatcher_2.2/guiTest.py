import Tkinter
top = Tkinter.Tk()


instruc = Tkinter.Label(top, text="Enter a Time:")
instruc.pack(side = Tkinter.LEFT)
timeEntry = Tkinter.Entry(top, bd=5)

timeEntry.pack(side=Tkinter.RIGHT)


top.mainloop()
