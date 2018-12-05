#! /usr/bin/python3
#model.py

import pickle
import os
from Persona import *
from Entidad import *

class Model:
	def guardarEntidad(self, Entidad):
		result = []
		try:
			archivo = open('entidad.pickle', 'rb')
			result = pickle.load(archivo)
			archivo.close()
			archivoNuevo = open('entidad.pickle','wb')
			result.append(Entidad)
			pickle.dump(result, archivoNuevo)
			archivoNuevo.close()
		except IOError:
			archivoNuevo = open('entidad.pickle','wb')
			result.append(Entidad)
			pickle.dump(result, archivoNuevo)
			archivoNuevo.close()
		return

	def guardarPersona(self, Persona):
		result = []
		try:
			archivo = open('persona.pickle', 'rb')
			result = pickle.load(archivo)
			archivo.close()
			archivoNuevo = open('persona.pickle','wb')
			result.append(Persona)
			pickle.dump(result, archivoNuevo)
			archivoNuevo.close()
		except IOError:
			archivoNuevo = open('persona.pickle','wb')
			result.append(Persona)
			pickle.dump(result, archivoNuevo)
			archivoNuevo.close()
		return
	def listarEntidad(self):
		result = []
		try:
			archivo = open('entidad.pickle','rb')
			result = pickle.load(archivo)
			archivo.close()
			return result
		except IOError:
			return result 
		return	
#	 def listarPersonas(self):
#		result = []
#		try:
#			archivo = open('persona.pickle','rb')
#			result = pickle.load(archivo)
#			archivo.close()
#			return result
#		except IOError:
#			return result 
#		return
		
	def BuscarEmpresa(self, nombreEmp):
		noEncontrado = "Empresa no esta registrada"
		try:
			archivo = open('entidad.pickle','rb')
			listaempresas = pickle.load(archivo)
			archivo.close()
			for Entidad in listaempresas:
				if(Entidad.nombreEmp == nombreEmp):
					resultado =  [ Entidad.productovendido, Entidad.caja, Entidad.productocontrol, Entidad.montocontrol]
					return resultado
			return noEncontrado
		except IOError:
			return noEncontrado 
		return
		
	def buscarPorCedula(self, cedula):
		noEncontrado = "Persona no Encontrada"
		try:
			archivo = open('persona.pickle','rb')
			listaPersonas = pickle.load(archivo)
			archivo.close()
			for persona in listaPersonas:
				if(persona.documento == cedula):
					resultado = {"Nombre ": persona.nombre, "Apellido ": persona.apellido}
					return resultado
			return noEncontrado
		except IOError:
			return noEncontrado 
		return

	def realizarPruebas(self, nombreEmp):
		noEncontrado = "Empresa no esta registrada"
		try:
			archivo = open('entidad.pickle','rb')
			listaempresas = pickle.load(archivo)
			archivo.close()

			for Entidad in listaempresas:
				if(Entidad.nombreEmp == nombreEmp):
					resultado =  [ Entidad.productovendido, Entidad.caja, Entidad.productocontrol, Entidad.montocontrol]
				else:
					resultado = noEncontrado
		except IOError:
			return noEncontrado
		if resultado[0]==resultado[2] and resultado[1]==resultado[3]:
			
			print ("no hay irregularidad ")
			reporte="En esta empresa no se encontro irregularidades"
				#generarReporte(self,reporte)
		else:
			print ("los datos no coinciden")
			reporte="las cantidades vendidas no coinciden"
			
				#generarReporte(self,reporte)
