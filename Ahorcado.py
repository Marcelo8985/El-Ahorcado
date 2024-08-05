#importe la libreria random para mi juego
import random
#se ha creado el inicio del juego
print("Bienvenido al juego del ahorcado")
Nombre = input("Ingrese su nombre")
print(f"Bienvenido {Nombre} evita morir")
NumeroVIdas= 6
Palabras= ["jojo", "caballo", "loco", "ingeniero", "software"]
secreto= random.choice(Palabras)
#este print es para verificar que la variable secreto funciona posteriormente se la quitara
print(secreto)
#Desconozco aun mucho de python por lo que solo puedo avanzar hasta aqui, espero y en proximas clases pueda avanzar mas
