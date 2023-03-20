#4. Escribir una función que reciba una cadena de caracteres y devuelva un diccionario con cada palabra que contiene y la cantidad de veces que aparece (frecuencia). Escribir otra función que reciba el diccionario generado con la función anterior y devuelva una tupla con la palabra más repetida y su frecuencia.
def contar_palabras(cadena):
    palabras = cadena.split()
    contador = {}
    for palabra in palabras:
        if palabra in contador:
            contador[palabra] += 1
        else:
            contador[palabra] = 1
    return contador

def mas_repetida(diccionario):
    # Inicializar variables para la palabra más repetida y frecuencia
    palabra = ''
    frecuencia = 0
    # Recorrer el diccionario y encontrar la palabra más repetida
    for clave, valor in diccionario.items():
        if valor > frecuencia:
            palabra = clave
            frecuencia = valor
    # Devolver una tupla con la palabra más repetida y su frecuencia
    return (palabra, frecuencia)

cadena = input("Ingrese una cadena de caracteres: ")
resultado1 = contar_palabras(cadena)
print(resultado1)

resultado2 = mas_repetida(resultado1)
print(resultado2)
