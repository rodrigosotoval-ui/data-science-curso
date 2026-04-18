# Ejercicio 1
# Lista original de ventas

ventas = [
    {"fecha": "2024-01-01", "producto": "Laptop", "cantidad": 2, "precio": 750.0},
    {"fecha": "2024-01-01", "producto": "Mouse", "cantidad": 5, "precio": 20.0},
    {"fecha": "2024-01-02", "producto": "Teclado", "cantidad": 3, "precio": 45.0},
    {"fecha": "2024-01-02", "producto": "Laptop", "cantidad": 1, "precio": 760.0},
    {"fecha": "2024-01-03", "producto": "Mouse", "cantidad": 4, "precio": 22.0},
    {"fecha": "2024-01-03", "producto": "Monitor", "cantidad": 2, "precio": 180.0}
]

print("Lista de ventas original:")
for venta in ventas:
    print(venta)
print()


# Ejercicio 2
# Calcular los ingresos totales generados

ingresos_totales = 0

for venta in ventas:
    ingresos_totales += venta["cantidad"] * venta["precio"]

print("Ingresos totales generados:")
print(ingresos_totales)
print()


# Ejercicio 3
# Calcular la cantidad total vendida por producto e identificar el más vendido

ventas_por_producto = {}

for venta in ventas:
    producto = venta["producto"]
    cantidad = venta["cantidad"]

    if producto in ventas_por_producto:
        ventas_por_producto[producto] += cantidad
    else:
        ventas_por_producto[producto] = cantidad

producto_mas_vendido = ""
cantidad_mas_vendida = 0

for producto, cantidad in ventas_por_producto.items():
    if cantidad > cantidad_mas_vendida:
        producto_mas_vendido = producto
        cantidad_mas_vendida = cantidad

print("Ventas por producto:")
print(ventas_por_producto)
print()

print("Producto más vendido:")
print(producto_mas_vendido, cantidad_mas_vendida)
print()


# Ejercicio 4
# Calcular el precio promedio por producto

precios_por_producto = {}

for venta in ventas:
    producto = venta["producto"]
    cantidad = venta["cantidad"]
    precio = venta["precio"]

    if producto in precios_por_producto:
        suma_precios, total_unidades = precios_por_producto[producto]
        precios_por_producto[producto] = (suma_precios + (precio * cantidad), total_unidades + cantidad)
    else:
        precios_por_producto[producto] = (precio * cantidad, cantidad)

print("Precios por producto:")
print(precios_por_producto)
print()

print("Precio promedio por producto:")
for producto, datos in precios_por_producto.items():
    suma_precios, total_unidades = datos
    precio_promedio = suma_precios / total_unidades
    print(producto, precio_promedio)
print()


# Ejercicio 5
# Calcular los ingresos totales por día

ingresos_por_dia = {}

for venta in ventas:
    fecha = venta["fecha"]
    ingreso = venta["cantidad"] * venta["precio"]

    if fecha in ingresos_por_dia:
        ingresos_por_dia[fecha] += ingreso
    else:
        ingresos_por_dia[fecha] = ingreso

print("Ingresos por día:")
print(ingresos_por_dia)
print()


# Ejercicio 6
# Crear el resumen de ventas por producto

resumen_ventas = {}

for producto, cantidad_total in ventas_por_producto.items():
    ingresos_producto = 0

    for venta in ventas:
        if venta["producto"] == producto:
            ingresos_producto += venta["cantidad"] * venta["precio"]

    suma_precios, total_unidades = precios_por_producto[producto]
    precio_promedio = suma_precios / total_unidades

    resumen_ventas[producto] = {
        "cantidad_total": cantidad_total,
        "ingresos_totales": ingresos_producto,
        "precio_promedio": precio_promedio
    }

print("Resumen de ventas por producto:")
for producto, resumen in resumen_ventas.items():
    print(producto, resumen)
