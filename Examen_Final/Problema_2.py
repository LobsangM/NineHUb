# File: Problema_2.py
# Date: 28 de Junio del 2024
# Nombre Lobsang Derek Méndez Ojeda 
# Variante: Forma A


#PROBLEMA 2
# Cargar los datos del csv
# Calcular el total de ventas mensuales
# Calcular el producto más vendido por mes
# Graficar la evolución de las ventas a lo largo de los meses


import pandas as pd
import matplotlib.pyplot as plt

# 1. Cargar los datos
archivo_csv = 'Datos Forma A.csv'
datos = pd.read_csv(archivo_csv, delimiter=';')


#convertir a date time
datos['Fecha de Venta'] = pd.to_datetime(datos['Fecha de Venta'], dayfirst=True)
datos['Mes'] = datos['Fecha de Venta'].dt.to_period('M')



# 2. Calcular ventas mensuales
datos['Total Venta'] = datos['Cantidad Vendida'] * datos['Precio Unitario']
ventas_mensuales = datos.groupby('Mes')['Total Venta'].sum() #agrupar datos




# 3. Calcular producto más vendido por mes
productos_mas_vendidos = datos.groupby(['Mes', 'Producto Vendido'])['Cantidad Vendida'].sum().reset_index()
producto_mas_vendido_por_mes = productos_mas_vendidos.loc[productos_mas_vendidos.groupby('Mes')['Cantidad Vendida'].idxmax()]




# resultados
print("Ventas mensuales totales:")
print(ventas_mensuales)

print("\nProducto más vendido por mes:")
print(producto_mas_vendido_por_mes)




# 4. Graficar
plt.figure(figsize=(10, 6))
ventas_mensuales.plot(kind='line', marker='o')

plt.title('Evolución de las Ventas Mensuales')
plt.xlabel('Mes')
plt.ylabel('Total de Ventas')

plt.grid(True)
plt.show()
