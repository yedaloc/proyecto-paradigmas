#! /usr/bin/python3
#view.py

from Persona import Persona
from Entidad import Entidad
class View:
	
	def vistaAgregarPersona(self):
		print("Crear una nueva persona:")
		cedula  = input("Ingrese documento de la nueva persona: ")
		nombre = input("Ingrese el nombre de la nueva persona:")
		apellido = input("ingrese el apellido de la nueva persona:")
		nuevaPersona = Persona(cedula, nombre, apellido)
		return nuevaPersona

	def vistaAgregarEntidad(self):
		print("Agregar una nueva entidad:")
		nombre = input("Ingrese el nombre de que shopping:")
		tipo = input("que tipo de local es:")

		nombreEmp = input("Ingrese el nombre de la nueva Empresa:")
		duenho = input("Ingrese el nombre del dueño Empresa:")
		productovendido = input("Ingrese la cantidad de productos vendidos: ")
		caja = input("monto total recaudado de productos vendidos: ")
		productocontrol = input("Ingrese la cantidad de productos vendidos segun facturas: ")
		montocontrol = input("Ingrese la cantidad de productos segun facturas: ")
		nuevaEntidad = Entidad(nombre, tipo, nombreEmp, duenho, productovendido, caja, productocontrol, montocontrol)
		return nuevaEntidad	

	def vistaListarPersona(self, listaPersonas):
		print('Listado de personas en la base de datos: \n')
		if listaPersonas:
			for persona in listaPersonas:
				print('Nombre: ', persona.nombre, ', Apellido: ', persona.apellido, ', Documento: ', persona.documento)

	def vistaListarEntidad(self, listaEntidad):
		print('Listado de Empresas en la base de datos: \n')
		
		if listaEntidad:
			for Entidad in listaEntidad:
				print(Entidad.nombreEmp)			


	def vistaBuscarPorCedula(self):
		cedula = input("Ingrese el numero de documento de la persona a buscar: ")
		return cedula
	#def vistaBuscarEmpresa(self):
	#	empresa = input("Ingrese nomre de la empresa  ")
	#	return empresa	
	def vistarealizarPruebas(self):
		empresa = input("Ingrese nomre de la empresa  ")
		return empresa		
	def vistaImprimirPersonaBuscadaPorCedula(self, resultado):
		print("La persona encontrada es: ", resultado)
