#File: Tarea_3.py
#Date: 18/06/2024

# Ejercicios ciclos y funciones

def votar():
    edad = int(input('Ingrese su edad: '))
    ciudadania = int(input('Si es guatemalteco coloque 1, si no lo es coloque 0: '))
    condena = int(input('Si no tiene delitos coloque 0, si tiene delitos coloque 1: '))
    
    if ciudadania == 0:
        return 'No puedes votar, no eres guatemalteco'
    if condena == 1:
        return 'No puedes votar, tienes delitos'
    
    while edad < 18:
        print(f'No puedes votar porque eres menor de edad. Te faltan {18 - edad} años para poder votar.')
        edad += 1
    
    return 'Si puedes votar, cumples con los requisitos'

# Ejecución de la función
print(votar())
