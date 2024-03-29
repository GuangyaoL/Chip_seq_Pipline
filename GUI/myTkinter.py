#! -*- utf-8 -*-
from tkinter import *

class Quitter(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.quitter()

    def say_hi(self):
        print("hi there, everyone!")

    def createWidgets(self):
        self.QUIT = Button(self)
        self.QUIT["text"] = "QUIT"
        self.QUIT["fg"]   = "red"
        self.QUIT["command"] =  self.quit

        self.QUIT.pack({"side": "left"})

        self.hi_there = Button(self)
        self.hi_there["text"] = "Hello",
        self.hi_there["command"] = self.say_hi

        self.hi_there.pack({"side": "left"})

root = Tk()
app = Application(master=root)
app.mainloop()
root.destroy()