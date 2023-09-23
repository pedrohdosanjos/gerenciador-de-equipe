class Funcionario():
  def __init__(self, nome, ano_nasc, cargo, salario):
    self.nome = nome
    self.ano_nasc = ano_nasc
    self.cargo = cargo
    self.salario = salario

  def promover(self, salario):
    self.salario = salario
      