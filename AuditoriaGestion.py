#! /usr/bin/python3
import time
import pickle
from Entidad import *
from Auditoria import *

class AuditoriaGestion(Auditoria):
	
	def __init__(self, prueba1, prueba2):
		super(Auditoria, self).__init__()
		self.prueba = prueba

	def realizarPruebas(self,Entidad):

	#rirregularidades sirve para contar las falencias encontradas y asi definir si es de alto riesgo la empresa
		irregularidades=0
	#para la prueba 1 comparamos los datos brindados con los datos de la empresa
		if Entidad.productovendido==Entidad.productocontrol:
			
			print ("no hay irregularidad en la prueba 1")
			reporte="En esta empresa no se encontro irregularidades"
			generarReporte(self,reporte)
		else:
			print ("los datos no coinciden")
			reporte="las cantidades vendidas no coinciden"
			irregularidades+=1
			generarReporte(self,reporte)

		if Entidad.caja==Entidad.montocontrol:
			
			print ("no hay irregularidad en la prueba 2")
			reporte="En esta empresa no se encontro irregularidades en los montos"
			generarReporte(self,reporte)
		else:
			print ("los datos no coinciden")
			reporte="los montos vendidos no coinciden"
			irregularidades+=1
			generarReporte(self, reporte)	


		ult_eval=time.strftime("%d/%m/%y")	
		


	def buscarEmpresa(self, nombreEmp):
		noEncontrado = 'no hay entidad'
		try: 
			#se abre labd para buscar la empresa solicitada 
			archivo = open('entidad.pickle','rb')
			listaEmpresa = pickle.load(archivo)
			archivo.close()
			for Entidad in listaEmpresa:
				if(Entidad.nombreEmp == nombreEmp):
					resultado = Entidad
					return resultado
			return noEncontrado
		except IOError:
			return noEncontrado 
		return

	def generarReporte(self, reporte):
		result = []
		try:
			archivo = open('reporte.pickle', 'rb')
			result = pickle.load(archivo)
			archivo.close()
			archivoNuevo = open('reporte.pickle','wb')
			result.append(entidad)
			pickle.dump(result, archivoNuevo)
			archivoNuevo.close()
		except IOError:
			archivoNuevo = open('reporte.pickle','wb')
			result.append(reporte)
			pickle.dump(result, archivoNuevo)
			archivoNuevo.close()
		return

	def listarReporte(self):
		result = []
		try:
			archivo = open('reporte.pickle','rb')
			result = pickle.load(archivo)
			archivo.close()
			return result
		except IOError:
			return result 
		return			