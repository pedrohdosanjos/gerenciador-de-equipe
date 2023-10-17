from janela import *
from funcionario import *
from banco_dados import *

from tkinter import messagebox
import psycopg2

login = Janela("Login", 200, 200)
login.createWindow(0)

boss_menu = Janela("Menu de chefe", 350, 250)
empl_menu = Janela("Menu de funcionário", 250, 70)


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
        conn = None
        try:
            params = config()

            print("Connecting to the PostgreSQL Database...")
            conn = psycopg2.connect(**params)
            cur = conn.cursor()
            cur2 = conn.cursor()

            cur.execute("SELECT * FROM funcionários")
            rows = cur.fetchall()

            cur2.execute("SELECT COUNT(*) FROM funcionários")
            qtd = cur2.fetchone()

            table_window = tk.Tk()
            table_window.title("Tabela de Funcionários")
            total_rows = qtd[0]
            total_columns = 5  # Número de atributos de um funcionário

            for i in range(total_rows):
                for j in range(total_columns):
                    e = tk.Entry(table_window, width=20, fg="black", font=("Arial", 16))
                    e.grid(row=i, column=j)
                    e.insert(tk.END, rows[i][j])

            conn.commit()
            cur.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()
                print("Database connection closed.")

    # ação do botão de cadastro de funcionário
    def new_empl():
        ID = id_entry.get()
        Nome = nm_entry.get()
        Ano = yr_entry.get()
        Cargo = rl_entry.get()
        Salario = wg_entry.get()

        conn = None

        try:
            params = config()

            print("Connecting to the PostgreSQL database...")
            conn = psycopg2.connect(**params)

            cur = conn.cursor()

            cur.execute(
                "INSERT INTO funcionários(id,nome,anonascimento,cargo,salário) VALUES({0},'{1}', {2}, '{3}', {4})".format(
                    ID, Nome, Ano, Cargo, Salario
                )
            )

            conn.commit()
            cur.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            print("Cliente não encontrado")
        finally:
            if conn is not None:
                conn.close()
                print("Database connection closed.")

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
        ID = id_entry.get()
        conn = None

        try:
            params = config()

            print("Connecting to the PostgreSQL database...")
            conn = psycopg2.connect(**params)

            cur = conn.cursor()

            cur.execute(
                "UPDATE batePonto SET horachegada = CURRENT_TIMESTAMP WHERE id = {0}".format(
                    ID
                )
            )

            conn.commit()
            cur.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            print("Cliente não encontrado")
        finally:
            if conn is not None:
                conn.close()
                print("Database connection closed.")

    # aqui será registrado o horário de fim de trabalho do funcionario
    def end_work():
        ID = id_entry.get()
        conn = None

        try:
            params = config()

            print("Connecting to the PostgreSQL database...")
            conn = psycopg2.connect(**params)

            cur = conn.cursor()

            cur.execute(
                "UPDATE batePonto SET horasaida = CURRENT_TIMESTAMP WHERE id = {0}".format(
                    ID
                )
            )

            conn.commit()
            cur.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            print("Cliente não encontrado")
        finally:
            if conn is not None:
                conn.close()
                print("Database connection closed.")

    empl_menu.createButton("Início do expediente", begin_work, 5, 40)
    empl_menu.createButton("Fim do expediente", end_work, 135, 40)


login.createButton("Chefe", open_menu1, 80, 60)
login.createButton("Funcionário", open_menu2, 65, 105)

login.update()
boss_menu.update()
empl_menu.update()
