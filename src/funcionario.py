import datetime as dt

class Funcionario():
  def __init__(self, id, name, year, role, wage):
    self.id = id
    self.name = name
    self.year = year
    self.role = role
    self.wage = wage

  def promote(self, wage):
    self.wage = wage

  def begin(self):
    self.begin = dt.datetime.now()

  def end(self):
    self.end = dt.datetime.now()
      