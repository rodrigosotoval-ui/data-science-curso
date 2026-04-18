# Ejercicio 1
# Actualizar valores en diccionarios y listas

matriz = [[10, 15, 20], [3, 7, 14]]
cantantes = [
    {"nombre": "Ricky Martin", "pais": "Puerto Rico"},
    {"nombre": "Chayanne", "pais": "Puerto Rico"}
]

ciudades = {
    "México": ["Ciudad de México", "Guadalajara", "Cancún"],
    "Chile": ["Santiago", "Concepción", "Viña del Mar"]
}

coordenadas = [
    {"latitud": 8.2588997, "longitud": -84.9399704}
]

matriz[1][0] = 6
cantantes[0]["nombre"] = "Enrique Martin Morales"
ciudades["México"][2] = "Monterrey"
coordenadas[0]["latitud"] = 9.9355431

print("Resultado ejercicio 1:")
print(matriz)
print(cantantes)
print(ciudades)
print(coordenadas)
print()


# Ejercicio 2
# Iterar a través de una lista de diccionarios

def iterarDiccionario(lista):
    for diccionario in lista:
        print(f'nombre - {diccionario["nombre"]}, pais - {diccionario["pais"]}')


cantantes2 = [
    {"nombre": "Ricky Martin", "pais": "Puerto Rico"},
    {"nombre": "Chayanne", "pais": "Puerto Rico"},
    {"nombre": "José José", "pais": "México"},
    {"nombre": "Juan Luis Guerra", "pais": "República Dominicana"}
]

print("Resultado ejercicio 2:")
iterarDiccionario(cantantes2)
print()


# Ejercicio 3
# Obtener valores de una lista de diccionarios

def iterarDiccionario2(llave, lista):
    for diccionario in lista:
        print(diccionario[llave])


print("Resultado ejercicio 3 - nombres:")
iterarDiccionario2("nombre", cantantes2)
print()

print("Resultado ejercicio 3 - países:")
iterarDiccionario2("pais", cantantes2)
print()


# Ejercicio 4
# Iterar a través de un diccionario con valores de lista

def imprimirInformacion(diccionario):
    for llave, lista in diccionario.items():
        print(f"{len(lista)} {llave.upper()}")
        for valor in lista:
            print(valor)
        print()


costa_rica = {
    "ciudades": ["San José", "Limón", "Cartago", "Puntarenas"],
    "comidas": ["gallo pinto", "casado", "tamales", "chifrijo", "olla de carne"]
}

print("Resultado ejercicio 4:")
imprimirInformacion(costa_rica)
