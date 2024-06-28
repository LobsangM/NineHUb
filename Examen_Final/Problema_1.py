# File: Problema_1.py
# Date: 28 de Junio del 2024
# Nombre Lobsang Derek Méndez Ojeda 
# Variante: Forma A 


#PROBLEMA 1
# Cada año la poblacion de peces se duplica
# Cada año, 23% de porcentaje de la poblacion es pecado
# Cada año, 9% de la población de peces muere
# En un total de 10 años  


x = int(input("Ingrese la cantidad de peces iniciales: "))
t = int(input("Ingrese la cantidad de años a simular : "))

pesca = 0.23
muerte = 0.09

# Iteramos por cada año y aplicamos las condiciones
for año in range(1, t+1):
    x = x*2                        # La población se duplica
    pecado = int(x*pesca)               # Calculamos el número de peces pecado
    muertes = int(x*muerte)             # Calculamos el número de muertes
    x = x-pecado-muertes           # Actualizamos la población

    print(f"Año {año}: {x:.2f} peces")



