#! /usr/bin/python3
from Entidad import *
class EmpAuditora(Entidad):

	def __init__(self,nombreEmp,duenho,productovendido,montovendido,productocontrol,montocontrol,experiencia):
		
		Entidad.__init__(self,nombreEmp,duenho,productovendido,montovendido,productocontrol,montocontrol)

		self.experiencia= experiencia

		

	