from database import *
from janela import *
from funcionario import *
from func import *
from tkinter import messagebox

login = Janela("Main", 350, 250)
login.createWindow(0)

boss_menu = Janela("Menu de chefe", 350, 350)
empl_menu = Janela("Menu de funcionário", 350, 250)

def open_menu1():
    boss_menu.createWindow(1)

    padding=0.05
    X,Y = 0.5, 0.05
    line_height = 0.07
    i = 0
    # Valor de entrada
    label_id = tk.Label(boss_menu.window, text="Identificação")
    label_id.place(relx=X-padding, rely=Y+i*line_height, anchor="ne")

    id_entry = tk.Entry(boss_menu.window, width=20)
    id_entry.place(relx=X, rely=Y+i*line_height, anchor="nw")
    i+=1
    
    # Valor de entrada
    label_nm = tk.Label(boss_menu.window, text="Nome")
    label_nm.place(relx=X-padding, rely=Y+i*line_height, anchor="ne")

    nm_entry = tk.Entry(boss_menu.window, width=20)
    nm_entry.place(relx=X, rely=Y+i*line_height, anchor="nw")
    i+=1

    # Valor de entrada
    label_yr = tk.Label(boss_menu.window, text="Ano de nascimento")
    label_yr.place(relx=X-padding, rely=Y+i*line_height, anchor="ne")

    yr_entry = tk.Entry(boss_menu.window, width=20)
    yr_entry.place(relx=X, rely=Y+i*line_height, anchor="nw")
    i+=1

    # Valor de entrada
    label_rl = tk.Label(boss_menu.window, text="Cargo")
    label_rl.place(relx=X-padding, rely=Y+i*line_height, anchor="ne")

    rl_entry = tk.Entry(boss_menu.window, width=20)
    rl_entry.place(relx=X, rely=Y+i*line_height, anchor="nw")
    i+=1

    # Valor de entrada
    label_wg = tk.Label(boss_menu.window, text="Salário")
    label_wg.place(relx=X-padding, rely=Y+i*line_height, anchor="ne")

    wg_entry = tk.Entry(boss_menu.window, width=20)
    wg_entry.place(relx=X, rely=Y+i*line_height, anchor="nw")
    i+=2

    def func_table(lista):
        table_window = tk.Tk()
        table_window.title("Tabela de Funcionários")
        total_rows = len(lista)
        total_columns = 5  # Número de atributos (úteis) de um funcionário

        for i in range(total_rows):
            for j in range(total_columns):
                e = tk.Entry(table_window, width=20, fg="black", font=("Arial", 16))
                e.grid(row=i, column=j)
                e.insert(tk.END, lista.get(list(lista.keys())[i]).getAttributes()[j])

    # ação do botão de cadastro de funcionário
    def new_empl(lista):
        # Testa se os valores inseridos são válidos
        if (
            id_entry.get() == "" or is_of_type(id_entry.get(), int) or
            nm_entry.get() == "" or
            yr_entry.get() == "" or is_of_type(yr_entry.get(), int) or
            rl_entry.get() == "" or
            wg_entry.get() == "" or is_of_type(wg_entry.get(), float)
           ):
            messagebox.showerror("Erro", "Erro: Um ou mais valores inseridos não são válidos...")
            return

        # insere o novo funcionário na lista de funcionários
        ID = int(id_entry.get())
        Nome = nm_entry.get()
        Ano = int(yr_entry.get())
        Cargo = rl_entry.get()
        Salario = float(wg_entry.get())

        func = Funcionario(ID, Nome, Ano, Cargo, Salario)

        lista.append(func)
    

    boss_menu.createButton("Cadastrar novo funcionário", new_empl, tabela_funcionarios, X, Y+i*line_height, relative=True, anch="center")
    i+=2

    # Valor de entrada
    label_emplID = tk.Label(boss_menu.window, text="ID à Pesq.")
    label_emplID.place(relx=X-padding, rely=Y+i*line_height, anchor="ne")

    emplID_entry = tk.Entry(boss_menu.window, width=20)
    emplID_entry.place(relx=X, rely=Y+i*line_height, anchor="nw")
    i+=2
    
    # Lista todas as informações sobre um funcionário específico
    def inspect_empl(lista):
        # Conferindo se o ID é válido                
        if emplID_entry.get() != "":            
            ID = int(emplID_entry.get())
        else:            
            messagebox.showerror("Erro", "Erro: Digitar um ID válido")
            return
                   
        el, state = lista.get(ID)
        if state == False:
            messagebox.showerror("Erro", "Erro: ID não consta no Banco de Dados")
            return
        attr = el.getAttributes(all=True)
        table_window = tk.Tk()
        table_window.title(f"Informações sobre \'{attr[1]}\'")
        total_columns = len(attr)-1  # Número de atributos (úteis) de um funcionário
        j = 0
        for i in range(total_columns):
            e = tk.Entry(table_window, width=20, fg="black", font=("Arial", 16))
            e.grid(row=j, column=0)
            e.insert(tk.END, attr[j])
            j += 1
        e = tk.Entry(table_window, width=20, fg="black", font=("Arial", 16))
        e.grid(row=j, column=0)
        e.insert(tk.END, attr[j])

    boss_menu.createButton("Pesquisar funcionário", inspect_empl, tabela_funcionarios, X-padding, Y+i*line_height, relative=True, anch="ne")
    boss_menu.createButton("Tabela de Funcionários", func_table, tabela_funcionarios, X+padding, Y+i*line_height, relative=True, anch="nw")
    i+=2

def open_menu2():
    empl_menu.createWindow(2)


    padding=0.05
    X,Y = 0.5, 0.3
    line_height = 0.1
    i = 0
    label_id = tk.Label(empl_menu.window, text="Identificação")
    label_id.place(relx=X-padding, rely=Y+i*line_height, anchor="ne")   

    id_entry = tk.Entry(empl_menu.window, width=20)
    id_entry.place(relx=X, rely=Y+i*line_height, anchor="nw")
    i+=2

    # Aqui será registrado o horário de inicio de trabalho do funcionario
    def begin_work(lista):
        # Conferindo se o ID é válido
        if id_entry.get() != "":
            lista.get(int(id_entry.get()))[0].begin()
            id_entry.delete(0, 4)
        else:
            messagebox.showerror("Erro", "Erro: Digitar um ID válido")

    # Aqui será registrado o horário de fim de trabalho do funcionario
    def end_work(lista):
        if id_entry.get() != "":
            lista.get(int(id_entry.get()))[0].end()
            id_entry.delete(0, 4)
        else:
            messagebox.showerror("Erro", "Erro: Digitar um ID válido")

    empl_menu.createButton("Início do expediente", begin_work, tabela_funcionarios, X-padding, Y+i*line_height, relative=True, anch="ne")
    empl_menu.createButton("Fim do expediente", end_work, tabela_funcionarios, X+padding, Y+i*line_height, relative=True, anch="nw")


login.createButton("Chefe", open_menu1, placex=0.5, placey=0.35, relative=True, anch="center")
login.createButton("Funcionário", open_menu2, placex=0.5, placey=0.65, relative=True, anch="center")

# Updates all "Janela" class's instances
for inst in Janela.getInstances():
    inst.update()
