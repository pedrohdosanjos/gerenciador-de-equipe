import tkinter as tk
class Janela():
  def __init__(self, name, sizex, sizey):
    self.window = tk.Tk(useTk=False)
    self.name = name
    self.sizex = sizex
    self.sizey = sizey
    self.buttons = []

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

  def createButton(self, name, action, placex, placey):
    self.buttons.append(tk.Button(self.window, text=name, command= action).place(x=placex,y=placey)) 
    
