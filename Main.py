#! /usr/bin/python3

#Main.py
import os

from controller import Controller

c = Controller()

def menu():

	"""

	Función que limpia la pantalla y muestra nuevamente el menu

	"""

	os.system('clear') 

	print ("Sistema de Auditoria")

	print ("\t1 - Agregar empresa")

	print ("\t2 - Realizar Auditoria")

	print ("\t3 - listar Empresa")

	print ("\t9 - salir")

 

 

while True:

	# Mostramos el menu

	menu()

 

	# solicituamos una opción al usuario

	opcionMenu = input("inserta un numero valor >> ")

 

	if opcionMenu=="1":
			#ingresando para crear una empresa
			c.agregarEntidad()
			
		

			input("Se ha Agregado una empresa \npulsa una tecla para continuar")

	elif opcionMenu=="2":
			#realizar auditoria
			print("Elija Empresa a tomar auditoria")
		
			c.listarEntidad()
			c.realizarPruebas()

			input("Has pulsado la opción 2...\npulsa una tecla para continuar")

	elif opcionMenu=="3":
		#genera reportes e imprime los reportes obtenidos

		c.listarEntidad()

		print ("")

		input("Has pulsado la opción 3...\npulsa una tecla para continuar")

	elif opcionMenu=="9":

		break

	else:

		print ("")

		input("No has pulsado ninguna opción correcta...\npulsa una tecla para continuar")