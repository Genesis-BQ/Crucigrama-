#-----Las biblotecas de uso------------
from tkinter import *
from PIL import ImageTk, Image #importar imagen 
from tkinter import messagebox
import os
import subprocess
#-------------------------------------------Metodos para llmar otros proyectos--------------------------
def animales():
    # Ruta al archivo del proyecto que deseas ejecutar
    ruta_proyecto = 'animales.py'  # Reemplaza con la ruta adecuada a tu proyecto
    try:
        # Ejecuta el proyecto utilizando la función subprocess.call()
        subprocess.call(['python', ruta_proyecto])
    except FileNotFoundError:
        print(f'El archivo del proyecto no fue encontrado: {ruta_proyecto}')
def Paises():
    # Ruta al archivo del proyecto que deseas ejecutar
    ruta_proyecto = 'paises.py'  # Reemplaza con la ruta adecuada a tu proyecto
    try:
        # Ejecuta el proyecto utilizando la función subprocess.call()
        subprocess.call(['python', ruta_proyecto])
    except FileNotFoundError:
        print(f'El archivo del proyecto no fue encontrado: {ruta_proyecto}')
def Deportes():
    # Ruta al archivo del proyecto que deseas ejecutar
    ruta_proyecto = 'deportes.py'  # Reemplaza con la ruta adecuada a tu proyecto
    try:
        # Ejecuta el proyecto utilizando la función subprocess.call()
        subprocess.call(['python', ruta_proyecto])
    except FileNotFoundError:
        print(f'El archivo del proyecto no fue encontrado: {ruta_proyecto}')
#-------------------------------------------Ventana Principal-------------------------------
raiz = Tk() #Crea la ventana
raiz.title("Principal") #titulo de la ventana
global dimension_entry,verticales_entry,horizontales_entry,casillas_nulas_entry,palabra_resultante_entry
ancho_ventana = 900
alto_ventana = 600
ancho_pantalla = raiz.winfo_screenwidth()
alto_pantalla = raiz.winfo_screenheight()
posicion_x = int((ancho_pantalla / 2) - (ancho_ventana / 2))
posicion_y = int((alto_pantalla / 2) - (alto_ventana / 2))
raiz.geometry(f"{ancho_ventana}x{alto_ventana}+{posicion_x}+{posicion_y}")  # Establecer el tamaño y posición de la ventana 
#-----------------------------------------Ventana principal-------------------------------
#--------------------Fondo de la ventana------------------------
imagen_fondo = Image.open("mente.png")
imagen_fondo = ImageTk.PhotoImage(imagen_fondo)
label_fondo = Label(raiz, image=imagen_fondo)
label_fondo.place(x=0, y=0, relwidth=1, relheight=1)
#---------------------------------------------------------------
def abri_ventana():
    global ventana 
    raiz.withdraw() #cierra la ventana principal raiz
    global imagen
    ventana= Toplevel(raiz)#Crea la ventana
    ventana.title("Juego Cucigrama")#titulo de la ventana
    ancho_ventana2 = 900
    alto_ventana2 = 600
    ancho_pantalla2 = ventana.winfo_screenwidth()
    alto_pantalla2 = ventana.winfo_screenheight()
    posicion_x2 = int((ancho_pantalla2 / 2) - (ancho_ventana2 / 2))
    posicion_y2 = int((alto_pantalla2 / 2) - (alto_ventana2 / 2))
    ventana.geometry(f"{ancho_ventana2}x{alto_ventana2}+{posicion_x2}+{posicion_y2}")
#----------------------------Fondo------------------------------------------------
    imagen= ImageTk.PhotoImage(Image.open("mente.png"))
    label_fondo2 = Label(ventana, image=imagen)
    label_fondo2.place(x=0, y=0, relwidth=1, relheight=1)
    #-----------------------------------El tiulo principal de la ventana----------------
    label = Label(ventana, text="Bienvenidos al juedo cucigrama", font=("Castellar", 14), fg="white", bg="#c20000")
    label.pack()
    #Boton para abrir la tercera ventana
    boton_1 = Button(ventana, text="Jugar",font=("Castellar", 14), fg="white", bg="#c20000", command=lambda:ventana_Jugar())
    boton_1.pack(side="right", padx=10, pady=(500, 10))
    # Botón para regresar a la ventana principal
    boton_regresar = Button(ventana, text="➢",font=("Castellar", 14), fg="white", bg="#c20000",command=lambda:regresar_ventana())
    boton_regresar.pack(side="left", padx=10, pady=(500, 10))
#--------------------------------------------Configuracion de la ventana usario------------------------------------------------
def ventana_Jugar():
    global ventana_usuario
    ventana.withdraw() 
    global imagen3
    ventana_usuario= Toplevel(raiz)#Crea la ventana
    ventana_usuario.title("Seleccion")#titulo de la ventana
    ancho_ventana2 = 900
    alto_ventana2 = 600
    ancho_pantalla2 = ventana_usuario.winfo_screenwidth()
    alto_pantalla2 = ventana_usuario.winfo_screenheight()
    posicion_x2 = int((ancho_pantalla2 / 2) - (ancho_ventana2 / 2))
    posicion_y2 = int((alto_pantalla2 / 2) - (alto_ventana2 / 2))
    ventana_usuario.geometry(f"{ancho_ventana2}x{alto_ventana2}+{posicion_x2}+{posicion_y2}")# Establecer el tamaño y posición de la ventana 
#----------------------------Fondo------------------------------------------------
    imagen3= ImageTk.PhotoImage(Image.open("preguntados.png"))
    label_fondo3 = Label(ventana_usuario, image=imagen3)
    label_fondo3.place(x=0, y=0, relwidth=1, relheight=1)
    #-----------------------------------El tiulo principal de la ventana----------------
    label = Label(ventana_usuario, text="Crucigrama", font=("Castellar", 14), fg="white", bg="#c20000")
    label.pack()
    #--------------------------------------Los botones de la ventana----------------------
    boton_resolver = Button(ventana_usuario, text="Resolver Crucigrama Animales", font=("Castellar", 10), fg="white", bg="#c20000",command=lambda:animales())
    boton_resolver.pack(side="left", padx=10, pady=(500, 10))
    boton_resolver = Button(ventana_usuario, text="Resolver Crucigrama Paises", font=("Castellar", 10), fg="white", bg="#c20000",command=lambda:Paises())
    boton_resolver.pack(side="left", padx=10, pady=(500, 10))
    boton_resolver = Button(ventana_usuario, text="Resolver Crucigrama Deportes", font=("Castellar", 10), fg="white", bg="#c20000",command=lambda:Deportes())
    boton_resolver.pack(side="left", padx=10, pady=(500, 10))
    boton_4 = Button(ventana_usuario, text="➢",font=("Castellar", 14), fg="white", bg="#c20000",command=lambda:regresar_juagr())
    boton_4.pack(side="right", padx=10, pady=(500, 10))
#-----------------------------------Metodo de regresara la ventana-------------------------------------------
def regresar_ventana():
    ventana.destroy() # Cerrar la ventana "Juego Cucigrama"
    raiz.deiconify()  # Mostrar la ventana principal nuevamente
def regresar_juagr():
    ventana_usuario.destroy() # Cerrar la ventana "Usario"
    ventana.deiconify() # Mostrar la ventana seleccion nuevamente
#-----------------------------------Metodo de regresara la ventana-------------------------------------------
#------------------------Crear el boton princinpal-----------------
boton = Button(raiz, text="Iniciar juego",font=("Castellar", 18), fg="white", bg="#c20000",command=lambda:abri_ventana())
boton.pack(side="right", padx=10, pady=(150, 10), anchor="se")
#----------------------se monostrara en la ventana----------------------------------------
raiz.mainloop() #Lo que muestra en la ventana