import tkinter as tk


class Janela:
    # Container for all instances of the class
    _instances = []

    @classmethod
    def getInstances(cls):  # Returns the conrtainer to all instances of the class
        return cls._instances
    
    def __init__(self, name, sizex, sizey):
        self.window = tk.Tk(useTk=False)
        self.name = name
        self.sizex = sizex
        self.sizey = sizey
        self.buttons = []

        Janela._instances.append(self)

    def createWindow(self, inst):
        if inst == 0:
            self.window = tk.Tk()

        else:
            self.window = tk.Toplevel()

        self.window.title(self.name)

        self.window.minsize(self.sizex, self.sizey)
        self.window.maxsize(self.sizex, self.sizey)

    def update(self):
        self.window.mainloop()

    def createButton(self, name, action, args=None, placex=0, placey=0, relative=False, anch="nw"):
        if args != None:
            btn = tk.Button(self.window, text=name, command=lambda: action(args))
        else:
            btn = tk.Button(self.window, text=name, command=action)
        if not relative:
            btn.place(x=placex, y=placey)
        else:
            btn.place(relx=placex, rely=placey, anchor=anch)
        self.buttons.append(btn)
        return btn
