#3.Escribir un programa que reciba una cadena de caracteres y devuelva un diccionario con cada palabra que contiene y la cantidad de veces que aparece (frecuencia).
def contar_palabras(cadena):
    # Convertir cadena a lista de palabras
    palabras = cadena.split()
    # Crear un diccionario para contar las palabras
    contador = {}
    # Recorrer la lista de palabras y contar
    for palabra in palabras:
        if palabra in contador:
            contador[palabra] += 1
        else:
            contador[palabra] = 1   
    # Devolver el diccionario con las palabras y recuencias
    return contador
# Pedir la cadena de caracteres
cadena = input("Ingrese una cadena de caracteres: ")
# Llamar función contar_palabras y mostrar el resultado
resultado = contar_palabras(cadena)
print(resultado)
