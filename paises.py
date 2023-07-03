import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image #importar imagen 
import subprocess
class Crucigrama:
    def __init__(self, palabras):
        self.palabras = palabras
        self.tablero = [[' ' for _ in range(10)] for _ in range(10)]  # Tamaño del crucigrama: 10x10
        self.soluciones = {}
    def resolver_crucigrama(self):
        for i, palabra in enumerate(self.palabras):
            if i >= 10:
                messagebox.showwarning('Advertencia', 'No se pueden mostrar más de 10 palabras en el crucigrama.')
                return
            if len(palabra) > 10:
                messagebox.showwarning('Advertencia', f'La palabra "{palabra}" es demasiado larga para el crucigrama.')
                continue
            fila, columna, direccion = self.buscar_posicion(palabra)
            if fila is not None and columna is not None and direccion is not None:
                self.colocar_palabra(palabra, fila, columna, direccion)
                self.soluciones[palabra] = {'fila': fila, 'columna': columna, 'direccion': direccion}
            else:
                messagebox.showwarning('Advertencia', f'No se pudo ubicar la palabra "{palabra}" en el crucigrama.')
    def buscar_posicion(self, palabra):
        for fila in range(10):
            for columna in range(10):
                if self.validar_posicion(palabra, fila, columna, 'H'):
                    return fila, columna, 'H'
                elif self.validar_posicion(palabra, fila, columna, 'V'):
                    return fila, columna, 'V'
        return None, None, None
    def validar_posicion(self, palabra, fila, columna, direccion):
        if direccion == 'H':
            if columna + len(palabra) <= 10:
                for i in range(len(palabra)):
                    if self.tablero[fila][columna + i] != ' ' and self.tablero[fila][columna + i] != palabra[i]:
                        return False
                return True
        elif direccion == 'V':
            if fila + len(palabra) <= 10:
                for i in range(len(palabra)):
                    if self.tablero[fila + i][columna] != ' ' and self.tablero[fila + i][columna] != palabra[i]:
                        return False
                return True
        return False
    def colocar_palabra(self, palabra, fila, columna, direccion):
        if direccion == 'H':
            for i in range(len(palabra)):
                self.tablero[fila][columna + i] = palabra[i]
        else:
            for i in range(len(palabra)):
                self.tablero[fila + i][columna] = palabra[i]
    def mostrar_crucigrama(self):
        global ventana
        ventana = tk.Tk()
        ventana.title('Crucigrama de Paises')
        ancho_ventana = 900
        alto_ventana = 600
        ancho_pantalla = ventana.winfo_screenwidth()
        alto_pantalla = ventana.winfo_screenheight()
        posicion_x = int((ancho_pantalla / 2) - (ancho_ventana / 2))
        posicion_y = int((alto_pantalla / 2) - (alto_ventana / 2))
        ventana.geometry(f"{ancho_ventana}x{alto_ventana}+{posicion_x}+{posicion_y}")  # Establecer el tamaño y posición de la ventana 
        imagen_fondo = Image.open("preguntados.png")
        imagen_fondo = ImageTk.PhotoImage(imagen_fondo)
        label_fondo = tk.Label(ventana, image=imagen_fondo)
        label_fondo.place(x=0, y=0, relwidth=1, relheight=1)
        for i in range(10):
            for j in range(10):
                casilla = tk.Entry(ventana, width=2, font=('Arial', 12))
                casilla.grid(row=i, column=j)
        adivinar_frame = tk.Frame(ventana)
        adivinar_frame.grid(row=0, column=11, rowspan=10, padx=10)
        for i in range(5):
            palabra_label = tk.Label(adivinar_frame, text='Palabra ' + str(i + 1))
            palabra_label.grid(row=i, column=0, sticky='w')
        adivinar_entrys = []
        for i in range(5):
            adivinar_entry = tk.Entry(adivinar_frame, width=15)
            adivinar_entry.grid(row=i, column=1, padx=5, pady=5)
            adivinar_entrys.append(adivinar_entry)
        boton_adivinar = tk.Button(adivinar_frame, text='Adivinar', command=lambda: self.adivinar_palabras(adivinar_entrys, ventana))
        boton_adivinar.grid(row=5, column=0, columnspan=2)
        label_pregunta = tk.Label(adivinar_frame, text='Pregunta:')
        label_pregunta.grid(row=6, column=0, columnspan=2)
        label_pregunta1 = tk.Label(adivinar_frame, text='¿Cual es la capital de Canada?')
        label_pregunta1.grid(row=7, column=0, columnspan=2)
        label_pregunta2 = tk.Label(adivinar_frame, text='¿Cual es la capital de Corea del Sur?')
        label_pregunta2.grid(row=8, column=0, columnspan=2)
        label_pregunta3 = tk.Label(adivinar_frame, text='¿Cual es la capital de Perú?')
        label_pregunta3.grid(row=9, column=0, columnspan=2)
        label_pregunta4 = tk.Label(adivinar_frame, text='¿Cual es la capital de Rumania?')
        label_pregunta4.grid(row=10, column=0, columnspan=2)
        label_pregunta5 = tk.Label(adivinar_frame, text='¿Cual es la capital de Tailandia?')
        label_pregunta5.grid(row=11, column=0, columnspan=2)
        ventana.mainloop()
    def adivinar_palabras(self, entrys, ventana):
        for i, entry in enumerate(entrys):
            palabra = entry.get().strip().lower()
            if palabra in self.soluciones:
                solucion = self.soluciones[palabra]
                fila = solucion['fila']
                columna = solucion['columna']
                direccion = solucion['direccion']
                if direccion == 'H':
                    for j in range(len(palabra)):
                        casilla = ventana.grid_slaves(row=fila, column=columna + j)[0]
                        casilla.delete(0, tk.END)
                        casilla.insert(0, palabra[j])
                else:
                    for j in range(len(palabra)):
                        casilla = ventana.grid_slaves(row=fila + j, column=columna)[0]
                        casilla.delete(0, tk.END)
                        casilla.insert(0, palabra[j])
                messagebox.showinfo('Crucigrama', f'¡Palabra {i + 1} correcta!')
            else:
                messagebox.showinfo('Crucigrama', f'Palabra {i + 1} incorrecta')
def leer_palabras(archivo):
    palabras = []
    with open(archivo, 'r') as file:
        for linea in file:
            palabras.append(linea.strip())
    return palabras
if __name__ == '__main__':
    palabras = leer_palabras('capitales.txt')
    crucigrama = Crucigrama(palabras)
    crucigrama.resolver_crucigrama()
    crucigrama.mostrar_crucigrama()
