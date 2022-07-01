import tkinter
import random

x = 20
limite_superior = x
limite_inferior = 1

#Configuracion de la ventana
v = tkinter.Tk()
v.title("Adivina el número")
v.geometry("1270x600")
v.configure(background="gray10")

#Limites
if limite_inferior != limite_superior:
    prediccion = random.randint(limite_inferior, limite_superior)
else:
    prediccion = limite_superior

#Definicion de las alternativas
def alta():

    limite_superior = prediccion - 1
    texto4.configure(text=f"{limite_superior}")



def baja():
    limite_inferior = prediccion + 1
    texto4.configure(text=f"{limite_inferior}")


texto1 = tkinter.Label(v, text="- - - - -| Bienvenido al juego |- - - - -", fg="green2", bg="gray10", font="Helvetica, 20")
texto2 = tkinter.Label(v, text=f"Seleccione un número entre el 1 y el {x} para que la computadora trate de adivinarlo",
                       fg="green2", bg="gray10", font="Helvetica, 20")
texto3 = tkinter.Label(v, text="Mi predicción es:", fg="green2", bg="gray10", font="Helvetica, 20")
texto4 = tkinter.Label(v, text=f"{prediccion}", fg="yellow", bg="gray10", font="Helvetica, 20")
boton1 = tkinter.Button(v, text="Es muy alta", fg="black", bg="green2", font="Helvetica, 20", command=alta)
boton2 = tkinter.Button(v, text="Es muy baja", fg="black", bg="green2", font="Helvetica, 20", command=baja)
boton3 = tkinter.Button(v, text="Es la correcta", fg="black", bg="green2", font="Helvetica, 20")

texto1.pack(pady=20)
texto2.pack(pady=20)
texto3.pack(pady=20)
texto4.pack(pady=20)
boton1.pack(pady=20)
boton2.pack(pady=20)
boton3.pack(pady=20)

v.mainloop()