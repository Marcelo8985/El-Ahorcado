#importe la libreria random para mi juego
import random
#se ha creado el inicio del juego
print("Bienvenido al juego del ahorcado")
Nombre = input("Ingrese su nombre")
print(f"Bienvenido {Nombre} evita morir")
NumeroVIdas= 0
Palabras= ["jojo", "caballo", "loco", "ingeniero", "software"]
secreto= random.choice(Palabras)
cadena= "-" * len(secreto)
#Se crea los posibles caminos que el usuario puede elegir
while True:
    print (cadena)
    letra= input("ingresa una letra:")
    if letra in secreto:
        for i in range (len(secreto)):
            if secreto[i]== letra:
                cadena= cadena[:i]+ letra + cadena[i+1 :]
    else:
        NumeroVIdas+=1
        if NumeroVIdas== 1:
            print("O")
        elif NumeroVIdas==2:
            print(" O")
            print("/")
        elif NumeroVIdas==3:
            print(" O")
            print("/|")
        elif NumeroVIdas==4:
            print(" O")
            print("/|\\")
        elif NumeroVIdas==5:
            print(" O")
            print("/|\\")
            print("/")
        elif NumeroVIdas==6:
             print(" O")
             print("/|\\")
             print("/ \\")
             print(f"Haz perdido el juego, la palabra secreto era {secreto}")
             break
    if cadena == secreto:
        print(f"Felicidades has ganado el juego, la palabra secreta era {secreto}")    
        break