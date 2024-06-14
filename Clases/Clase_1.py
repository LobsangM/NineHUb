'''

#Ejercicio Hola Mundo
print("Hola mundo")

#concatenar

nombre1 = "Abner"

nombre2 = 'Ansony'

print(nombre1 + nombre2)

#definir funciones

def saludar(nombre):
    saludo = '¡Hola '+ nombre + '!'
    return saludo

print(saludar(nombre1))
print(saludar('Maria'))


def saludar2(nombre1, nombre2): #recordemos que las funciones tienen variables locales
    nombre1 = 'Juan'
    return f'¡Hola {nombre1} y {nombre2}!'


print(saludar2('Tom', 'Toto'))
print(saludar2(nombre1,nombre2))




def deciredad(edad):
    return 'tengo' + str(edad)

print(deciredad(7))
print(deciredad(7.5))
print(deciredad('20'))



x1 = int(input('ingrese un número:'))
x2 = float(input('ingrese un número:'))
print(x1+x2)

'''


#Programar de Celcius A F

F = float(input('Ingrese la temperatura:'))

def conv(F):
    C = (F - 32)*5/9
    return C

print(conv(F))

