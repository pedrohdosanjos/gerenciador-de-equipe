from janela import*

login = Janela("Login", 200, 200)
login.createWindow(0)

boss_menu = Janela("Menu de chefe", 1000, 500)
empl_menu = Janela("Menu de funcionário", 250, 70)

def open_menu1():
  boss_menu.createWindow(1)

def open_menu2():
  empl_menu.createWindow(2)

  label = tk.Label(empl_menu.window, text= "Identificação do funcionário")
  label.grid (column = 0, row = 0)

  id_entry = tk.Entry(empl_menu.window, width=10)
  id_entry.grid(column=1, row=0)

  def begin_work(): #aqui será registrado o horário de inicio de trabalho do funcionario
    id_entry.delete(0, 4)

  def end_work(): #aqui será registrado o horário de fim de trabalho do funcionario
    id_entry.delete(0,4)

  empl_menu.createButton("Início do expediente", begin_work, 5, 40)
  empl_menu.createButton("Fim do expediente", begin_work, 135, 40)


login.createButton("Chefe", open_menu1, 80, 60)
login.createButton("Funcionário", open_menu2, 65, 105)

login.update()
boss_menu.update()
empl_menu.update()