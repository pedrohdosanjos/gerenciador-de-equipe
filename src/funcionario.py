import datetime as dt

class Funcionario():
  def __init__(self, id, name, year, role, wage):
    self.id = int(id)
    self.name = name
    self.year = int(year)
    self.role = role
    self.wage = float(wage)
    self.hours = []

  def promote(self, wage):
    self.wage = float(wage)

  def begin(self):
    self.begin = dt.datetime.now()

  def end(self):
    self.end = dt.datetime.now()

  def getAttributes(self):
    return [self.id, self.name, self.year, self.role, self.wage]
      