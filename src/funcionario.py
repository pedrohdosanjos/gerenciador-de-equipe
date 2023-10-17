from Data import *

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

  def begin(self):  # returns True if validated, else False
    if len(self.hours) > 0 and self.hours[-1][1]!= -1:
      self.hours.append([Data(), -1])
      return True
    else:
      return False


  def end(self):  # returns True if validated, else False
    if len(self.hours) > 0 and self.hours[-1][1] == -1:
      self.hours[-1][1] = Data()
      return True
    else:
      return False

  def getAttributes(self):
    return [self.id, self.name, self.year, self.role, self.wage]
      