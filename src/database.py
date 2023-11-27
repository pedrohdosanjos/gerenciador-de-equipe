from funcionario import *
from func import *

# Database to store elements based on their IDs
class Database:
    def __init__(self, path: str="database.csv", overwrite=False):
        self.elements = {}
        self.databasePath = path
        if not overwrite:
            self.load()
    #
    def append(self, func):
        self.elements[func.id] = func
        self.save()
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
    #
    def save(self):
        with open(self.databasePath, 'w') as f:
            for func in self.elements.values():
                attr, hours = extractInfo(func)
                f.write(attr + "\n")
                f.write(hours + "\n")
    #
    def load(self):
        with open(self.databasePath, 'r') as f:
            for attr in f:
                attr = attr[:-1]
                hrs = next(f, "")[:-1]
                attributes = attr.split(',')
                id, name, year, role, wage = attributes
                print(attributes)
                id = int(id)
                year = int(year)
                wage = float(wage)
                func = Funcionario(id, name, year, role, wage)
                self.elements[func.id] = func
                #
                hours = hrs.split(',')
                if len(hours) > 0 and hours[0] == '':
                    continue
                for period in hours:
                    start = [-1]*6
                    end = [-1]*6
                    different = period.split('-(')
                    a = different[0].split('-')
                    for i in range(len(a)):
                        start[i] = a[i]
                        end[i] = a[i]
                    i += 1
                    pivot = i
                    while i < 6:
                        start[i] = different[1].split(')')[0].split('--')[0].split('.')[i-pivot]
                        end[i] = different[1].split(')')[0].split('--')[1].split('.')[i-pivot]
                        i += 1
                    start = [int(i) for i in start]
                    end = [int(i) for i in end]
                    startDate = Data(start[2], start[1], start[0], start[3], start[4], start[5])
                    endDate = Data(end[2], end[1], end[0], end[3], end[4], end[5])
                    func.hours.append([startDate, endDate])
                print(func.hours[0][0].getAttributes(), "\t", func.hours[0][1].getAttributes())

    

# Inicializando a Lista de funcionarios
tabela_funcionarios = Database()