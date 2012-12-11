#! /usr/bin/python
from Tkinter import *
import alarm

class App:
  def __init__(self, master):
    frame = Frame(master)
    frame.pack()

    self.menu = Menu(master)
    self.tkMenu = Menu(self.menu)
    self.menu.add_cascade(label='Settings', menu=self.tkMenu)
    self.tkMenu.add_command(label='Settings', command=frame.quit)
    self.tkMenu.add_command(label='Quit', command=frame.quit)
    master.config(menu=self.menu)

    #Label(frame, text="HH:MM:am/pm").pack(side=TOP)
    Label(frame, text="Enter a wakeup time:").pack(side=LEFT)
    self.button = Button(frame, text='Quit', fg='red',  command=frame.quit)
    self.button.pack(side=RIGHT)
    self.eButton = Button(frame, text='Enter', command=self.print_entry)
    self.eButton.pack(side=RIGHT)

    self.entryHour = Entry(frame, width=2)
    self.entryHour.pack(side=LEFT)

    Label(frame, text=':', padx=0).pack(side=LEFT)

    self.entryMinute = Entry(frame, width=2)
    self.entryMinute.pack(side=LEFT)
    self.entryMinute.bind('<Return>', self.print_entry)

    self.a = StringVar()
    self.a.set('am')
    self.ap = {}
    self.ap['am'] = Radiobutton(frame, text='am', variable=self.a, value='am', height=0, width=5, pady=-1).pack(anchor=W)
    self.ap['pm'] = Radiobutton(frame, text='pm', variable=self.a, value='pm', height=0, pady=0).pack(anchor=W)

  def print_entry(*args):
    time = args[0].entryHour.get() + ':' + args[0].entryMinute.get() + args[0].a.get()
    alarm.inputTkinter(time)
    print time

def main():
  root = Tk()
  try:
    root.tk.call('console', 'hide')
  except TclError:
    pass
  app = App(root)

  root.mainloop()

main()
