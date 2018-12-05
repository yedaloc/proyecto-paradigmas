#! /usr/bin/python3
from abc import ABC,abstractmethod

class Persona(ABC):
	def __init__(self,nombre,apellido,ci):
		self.nombre=nombre
		self.apellido= apellido
		self.ci= ci
