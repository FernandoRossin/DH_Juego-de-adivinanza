#Juego de adivinanza
import random

numero_secreto = random.randint(0,100)
adivinado = False
cant_intentos = 0
cant_max_intentos = 5

print("Bienvenido al juego de adivinar el numero secreto")

while not adivinado:
    if not cant_intentos < cant_max_intentos:
        print("Game over")
        break
    entrada = input("Introduce un número del 1 al 99: ")
    numero = int(entrada)

    if numero == numero_secreto:
        print("Felicitaciones adivinaste!")
        adivinado = True
    elif numero < numero_secreto:
        print("el numero es mayor al ingresado")
    else:
        print("el numero es menor al ingresado")
    cant_intentos += 1


