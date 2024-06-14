#Programar de Celcius A F

F = float(input('Ingrese la temperatura:'))

def conv(F):
    C = (F - 32)*5/9
    return C

print(conv(F))

