#! /usr/bin/python3

class Funcionario(Persona):

	def __init__(self,cargo,empresa):
		Persona.__init__(self,nombre,apellido,ci)
		self.cargo = cargo
		self.empresa = empresa



	def getCargos(self):
		return self.cargos
	def	getEmpresa(self):
		return self.empresa


	def mostrarFuncionario(self):
		print ("\nCargo" +self.getCargos() +"\nEmpresa"+self.getEmpresa) )	

cargo=raw_input("ingrese el cargo")
empresa=raw_input("ingrese empresa")