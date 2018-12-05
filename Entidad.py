#! /usr/bin/python3

from Universo import *

class Entidad(Universo):

	def __init__(self,nombre,tipo, nombreEmp,duenho,productovendido,caja,productocontrol,montocontrol):

		Universo.__init__(self,nombre,tipo)

		self.nombreEmp= nombreEmp
		self.duenho= duenho
		self.productovendido= productovendido
		self.caja= caja
		self.productocontrol= productocontrol
		self.montocontrol= montocontrol
	