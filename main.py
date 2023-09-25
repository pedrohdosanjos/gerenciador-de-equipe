from janela import*
from funcionario import*

login = Janela("Login", 200, 200)
login.createWindow(0)

boss_menu = Janela("Menu de chefe", 1000, 500)
empl_menu = Janela("Menu de funcionário", 250, 70)

emplist = [2000]

def open_menu1():
  boss_menu.createWindow(1)

  #Valor de entrada 
  label_id = tk.Label(boss_menu.window, text= "Identificação")
  label_id.grid (column = 0, row = 0)

  id_entry = tk.Entry(boss_menu.window, width=20)
  id_entry.grid(column=1, row=0)

  #Valor de entrada 
  label_nm = tk.Label(boss_menu.window, text= "Nome")
  label_nm.grid (column = 0, row = 1)

  nm_entry = tk.Entry(boss_menu.window, width=20)
  nm_entry.grid(column=1, row=1)

  #Valor de entrada 
  label_yr = tk.Label(boss_menu.window, text= "Ano de nascimento")
  label_yr.grid (column = 0, row = 2)

  yr_entry = tk.Entry(boss_menu.window, width=20)
  yr_entry.grid(column=1, row=2)

  #Valor de entrada 
  label_rl = tk.Label(boss_menu.window, text= "Cargo")
  label_rl.grid (column = 0, row = 3)

  rl_entry = tk.Entry(boss_menu.window, width=20)
  rl_entry.grid(column=1, row=3)

  #Valor de entrada 
  label_wg = tk.Label(boss_menu.window, text= "Salário")
  label_wg.grid (column = 0, row = 4)

  wg_entry = tk.Entry(boss_menu.window, width=20)
  wg_entry.grid(column=1, row=4)

  #ação do botão de cadastro de funcionário
  def new_empl():
    #insere o novo funcionário na lista de funcionários
    emplist.insert(int(id_entry.get()), Funcionario(int(id_entry.get()), nm_entry.get(), int(yr_entry.get()), rl_entry.get(), int(wg_entry.get())))

  boss_menu.createButton("Cadastrar novo funcionário", new_empl, 40, 110)


def open_menu2():
  empl_menu.createWindow(2)

  label_id = tk.Label(empl_menu.window, text= "Identificação do funcionário")
  label_id.grid (column = 0, row = 0)

  id_entry = tk.Entry(empl_menu.window, width=10)
  id_entry.grid(column=1, row=0)

  #aqui será registrado o horário de inicio de trabalho do funcionario
  def begin_work():
    emplist[int(id_entry.get())].begin()
    id_entry.delete(0, 4)

  #aqui será registrado o horário de fim de trabalho do funcionario
  def end_work(): 
    emplist[int(id_entry.get())].end()
    id_entry.delete(0,4)

  empl_menu.createButton("Início do expediente", begin_work, 5, 40)
  empl_menu.createButton("Fim do expediente", end_work, 135, 40)


login.createButton("Chefe", open_menu1, 80, 60)
login.createButton("Funcionário", open_menu2, 65, 105)

login.update()
boss_menu.update()
empl_menu.update()