from janela import *
from funcionario import *
from tkinter import messagebox

login = Janela("Login", 200, 200)
login.createWindow(0)

boss_menu = Janela("Menu de chefe", 350, 250)
empl_menu = Janela("Menu de funcionário", 250, 70)

# Inicializando a Lista
emplist = [("1", "Pedro", "2003", "Estagiario", "2000")]


def open_menu1():
    boss_menu.createWindow(1)

    # Valor de entrada
    label_id = tk.Label(boss_menu.window, text="Identificação")
    label_id.grid(column=0, row=0)

    id_entry = tk.Entry(boss_menu.window, width=20)
    id_entry.grid(column=1, row=0)

    # Valor de entrada
    label_nm = tk.Label(boss_menu.window, text="Nome")
    label_nm.grid(column=0, row=1)

    nm_entry = tk.Entry(boss_menu.window, width=20)
    nm_entry.grid(column=1, row=1)

    # Valor de entrada
    label_yr = tk.Label(boss_menu.window, text="Ano de nascimento")
    label_yr.grid(column=0, row=2)

    yr_entry = tk.Entry(boss_menu.window, width=20)
    yr_entry.grid(column=1, row=2)

    # Valor de entrada
    label_rl = tk.Label(boss_menu.window, text="Cargo")
    label_rl.grid(column=0, row=3)

    rl_entry = tk.Entry(boss_menu.window, width=20)
    rl_entry.grid(column=1, row=3)

    # Valor de entrada
    label_wg = tk.Label(boss_menu.window, text="Salário")
    label_wg.grid(column=0, row=4)

    wg_entry = tk.Entry(boss_menu.window, width=20)
    wg_entry.grid(column=1, row=4)

    def func_table():
        table_window = tk.Tk()
        table_window.title("Tabela de Funcionários")
        total_rows = len(emplist)
        total_columns = 5  # Número de atributos de um funcionário

        for i in range(total_rows):
            for j in range(total_columns):
                e = tk.Entry(table_window, width=20, fg="black", font=("Arial", 16))
                e.grid(row=i, column=j)
                e.insert(tk.END, emplist[i][j])

        print(len(emplist))

    # ação do botão de cadastro de funcionário
    def new_empl():
        # insere o novo funcionário na lista de funcionários
        ID = id_entry.get()
        Nome = nm_entry.get()
        Ano = yr_entry.get()
        Cargo = rl_entry.get()
        Salario = wg_entry.get()

        Funcionario(ID, Nome, Ano, Cargo, Salario)

        tmp_list = (ID, Nome, Ano, Cargo, Salario)

        emplist.append(tmp_list)

    boss_menu.createButton("Cadastrar novo funcionário", new_empl, 40, 110)
    boss_menu.createButton("Tabela de Funcionários", func_table, 40, 140)


def open_menu2():
    empl_menu.createWindow(2)

    label_id = tk.Label(empl_menu.window, text="Identificação do funcionário")
    label_id.grid(column=0, row=0)

    id_entry = tk.Entry(empl_menu.window, width=10)
    id_entry.grid(column=1, row=0)

    # aqui será registrado o horário de inicio de trabalho do funcionario
    def begin_work():
        # Conferindo se o ID é válido
        if id_entry.get() != "":
            emplist[int(id_entry.get())].begin()
            id_entry.delete(0, 4)
        else:
            messagebox.showerror("Erro", "Erro: Digitar um ID válido")

    # aqui será registrado o horário de fim de trabalho do funcionario
    def end_work():
        if id_entry.get() != "":
            emplist[int(id_entry.get())].end()
            id_entry.delete(0, 4)
        else:
            messagebox.showerror("Erro", "Erro: Digitar um ID válido")

    empl_menu.createButton("Início do expediente", begin_work, 5, 40)
    empl_menu.createButton("Fim do expediente", end_work, 135, 40)


login.createButton("Chefe", open_menu1, 80, 60)
login.createButton("Funcionário", open_menu2, 65, 105)

login.update()
boss_menu.update()
empl_menu.update()
