#! /usr/bin/python3
from abc import ABC,abstractmethod

class Universo(ABC):
	def __init__(self,nombre,tipo):
		self.nombre=nombre
		self.tipo= tipo		