#File: Tarea_4.py
#Date: 19/06/2024

#Ejercicio en clase:

#Crear un diccionario de listas que contengan los nombres y calificaciones de los 5 alumnos en la seccion de matemática. Luego realiza una búsqueda para conocer el nombre y calificación de cada alumno en el diccionario.

seccion = {
    "alumnos": ["Juan", "María", "Carlos", "Ana", "Luis"],
    "calificaciones": [85, 92, 78, 88, 90]
}


def buscar(diccionario):

    for i in range(len(diccionario["alumnos"])):

        nombre = diccionario["alumnos"][i]
        calificacion = diccionario["calificaciones"][i]
        
        print(f"Nombre: {nombre}, Calificación: {calificacion}")


buscar(seccion)
