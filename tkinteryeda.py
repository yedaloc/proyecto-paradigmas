from tkinter import *
from controller import *
def abrir():
	ventAbrir=Tk()
	ventAbrir.geometry("400x200+100+100")
	ventAbrir.title("Agregar Empresa")
	
	ventAbrir.mainloop()

ventana = Tk()
ventana.geometry("600x600+0+0")
ventana.title("Programa de Auditoria")
#creacion de la barra de menu
barraMenu=Menu(ventana)
#creacion de menu
mnuArchivo=Menu(barraMenu)
#crear comando de los menu
mnuArchivo.add_command(label="Agregar Empresa",command=abrir)
mnuArchivo.add_command(label="Realizar Auditoria")
mnuArchivo.add_command(label="listar Empresas")
mnuArchivo.add_separator()
mnuArchivo.add_command(label="Salir",command=ventana.destroy)

#agregar los menu a la barra

barraMenu.add_cascade(label="Archivo",menu=mnuArchivo)

#indicamos que la barra de menu estara en la ventana
ventana.config(menu=barraMenu)

ventana.mainloop()