from janela import*

login = Janela("Login", 200, 200)
login.createWindow(0)

boss_menu = Janela("Menu de chefe", 1000, 500)
empl_menu = Janela("Menu de funcionário", 1000, 500)

def open_menu1():
  boss_menu.createWindow(1)

def open_menu2():
  empl_menu.createWindow(2)

login.createButton("Chefe", open_menu1, 80, 60)
login.createButton("Funcionário", open_menu2, 65, 105)

login.update()
boss_menu.update()
empl_menu.update()