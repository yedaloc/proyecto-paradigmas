#! /usr/bin/python3
#controller.py

from model import *
from view import *
#from Entidad import Entidad
#from Persona import Persona
class Controller:
	def __init__(self):
		self.model = Model()
		self.view = View()
	
	def agregarPersona(self):
		persona = self.view.vistaAgregarPersona()
		self.model.guardarPersona(Persona)

	def agregarEntidad(self):
		Entidad = self.view.vistaAgregarEntidad()
		self.model.guardarEntidad(Entidad)
		
	#def buscarEmpresa(self):
	#		empresa = self.view.vistaBuscarEmpresa()
	#		respuesta = self.model.BuscarEmpresa(empresa)
	#		return respuesta
	def realizarPruebas(self):
		empresa= self.view.vistarealizarPruebas()
		respuesta= model.Model.realizarPruebas(empresa)

	def listarPersonas(self):
		listaDePersonas = self.model.listarPersonas()
		self.view.vistaListarPersona(listaDePersonas)
		return listaDePersonas

	def listarEntidad(self):
		listaDeEntidad = self.model.listarEntidad()
		self.view.vistaListarEntidad(listaDeEntidad)
		return listaDeEntidad	
	
	
			
