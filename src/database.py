from funcionario import *

# Database to store elements based on their IDs
class Database:
    def __init__(self):
        self.elements = {}
    #
    def append(self, func):
        self.elements[func.id] = func
    #
    def get(self, id):
        if id not in self.elements.keys():
            return None, False
        else:
            return self.elements[id], True
    #
    def __len__(self):
        return len(self.elements)
    #
    def keys(self):
        return self.elements.keys()
    

# Inicializando a Lista de funcionarios
tabela_funcionarios = Database()

pedro = Funcionario(1, "Pedro", 2003, "Estagiario", 2000)

tabela_funcionarios.append(pedro)