from tkinter import *
from tkinter import ttk
from tkinter import messagebox

class calculator:
    def __init__(self):
        self.root = Tk()
        self.root.title("CALCULATOR")
        self.root.geometry("500x450+200+100")
        self.root.resizable(0,0)

    def run(self):
        self.root.mainloop()



if __name__ == "__main__":
    calc = calculator()
    calc.run()
