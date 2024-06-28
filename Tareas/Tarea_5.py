import pandas as pd
from datetime import datetime

# Crear DataFrame con datos ficticios de ventas para una tienda
data = {
    'Producto': ['Producto A', 'Producto B', 'Producto C', 'Producto A', 'Producto B', 'Producto C'],
    'Precio': [10.5, 20.0, 15.75, 10.5, 20.0, 15.75],
    'Cantidad Vendida': [5, 3, 6, 7, 2, 8],
    'Fecha': [datetime(2023, 6, 1), datetime(2023, 6, 2), datetime(2023, 6, 1), datetime(2023, 6, 3), datetime(2023, 6, 3), datetime(2023, 6, 4)]
}

df = pd.DataFrame(data)

# 1. Mostrar los primeros 5 registros del DataFrame
print("Primeros 5 registros del DataFrame:")
print(df.head())

# 2. Calcular el ingreso total por cada producto
df['Ingreso Total'] = df['Precio'] * df['Cantidad Vendida']
ingreso_por_producto = df.groupby('Producto')['Ingreso Total'].sum()
print("\nIngreso total por cada producto:")
print(ingreso_por_producto)

# 3. Calcular el ingreso total de todas las ventas
ingreso_total = df['Ingreso Total'].sum()
print("\nIngreso total de todas las ventas:")
print(ingreso_total)

# 4. Filtrar los productos vendidos en una fecha especifica
fecha_especifica = datetime(2023, 6, 1)
productos_vendidos_fecha = df[df['Fecha'] == fecha_especifica]
print(f"\nProductos vendidos en la fecha {fecha_especifica.strftime('%Y-%m-%d')}:")
print(productos_vendidos_fecha)

# 5. Ordenar los productos por cantidad vendida en orden descendente
productos_ordenados = df.sort_values(by='Cantidad Vendida', ascending=False)
print("\nProductos ordenados por cantidad vendida en orden descendente:")
print(productos_ordenados)

