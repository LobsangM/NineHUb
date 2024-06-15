#File: Tarea_2.py
#date: 14/05/24

#Primer ejercicio de if, elif y else

edad = int(input('Ingrese su edad;'))

def mayor(edad):
    if (edad >= 18):
        return 'Es mayor de edad'
    elif (edad <= 18 ):
        return 'Es menor de edad'

print(mayor(edad))

def mayor2(edad):
    valor = False
    if (edad >= 18):
        valor = True
    else:
        valor = False
    return valor

print (mayor2(24))

def mayor3(edad):
    return (edad >= 18)

print (mayor3(17))


#Problema prupuesto:

'''
Una persona puede votar si:
1. Tener al menos 18 años
2. Ser cuidadano registrado
3. No tener restricciones legales, no tener delitos

crear programa de python para ver que persona puede votar, parametros: EDAD, CUIDADANIA, DELITO.

1. EDAD = int
2. CUIDADANIA = BOOLEANO
3. Condenado delito o no = BOOLEANO


definamos la cuidadania como guatemalteco

'''

edad = int(input('Ingrese su edad: '))
ciudadania = int(input('Si es guatemalteco coloque 1, si no lo es coloque 0: '))
condena = int(input('Si no tiene delitos coloque 0, si tiene delitos coloque 1: '))

def votar(edad, ciudadania, condena):
    if edad < 18:
        return 'No puedes votar porque eres menor de edad'
    if ciudadania == 0:
        return 'No puedes votar, no eres guatemalteco'
    if condena == 1:
        return 'No puedes votar, tienes delitos'
    return 'Si puedes votar, cumples con los requisitos'

print(votar(edad, ciudadania, condena))



#Funciones Lambda

f = lambda x: x**2
print(f(4))

f2 = lambda x,y: x**2 + 2*y
print(f2(3,1))


#función que calcule factoriales ( BUCLES WHILE )

n = 5

def fact(n):
    i = 1
    resultado = 1
    while (i<=n):
        resultado *= i   #recordemos que *= es igual a resultado = resultado*i
        i += 1
    return resultado

print(fact(n))



#Números de Fibonacci ( BUCLES WHILE )

def fibonacci(n):

    #definimos la variables
    resultado = 1
    anterior = 0
    i = 0

    while(i < n):
        memoria = resultado 
        resultado += anterior
        anterior = memoria 

    return resultado

print(fibonacci(0), fibonacci(1), fibonacci(2), fibonacci(3))


# Funciones de recurrencia

n = 5

def fibo(n):
    if (n <= 1):
        return 1
    else:
        return fibo(n-1) + fibo(n-2)
     


print('fibonacci por recurencia: ',fibo(n))


#Factorial con funciones de recurencia

def factorial (n):
    if (n>0):
        return factorial(n-1)*n
    else:
        return 1
    

print(factorial(5))


#nota: los ejercicios los trabajé en un notebook, pero al pasarlos a este archivo probablemente de error
#      porque algunas variables se llaman igual.