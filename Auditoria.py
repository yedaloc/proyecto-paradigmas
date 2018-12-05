#! /usr/bin/python3
from Departamento import *
from abc import ABC,abstractmethod
class Auditoria(ABC):
 	def __init__(self,accion,hallazgo,control,ult_eval):

 		Departamento.__init__(self, nombre,jerarquia)
 		self.accion= accion
 		self.hallazgo= hallazgo
 		self.control= control
 		self.ult_eval= ult_eval

 		#generar reporte
 	