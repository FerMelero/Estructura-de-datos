lista= [1,"a",False]
#print(lista)

lista[2] = "Ford"
#print(lista)

cadena="knfdsjfid9"
#print(len(cadena))

'''
print(cadena[3])
print(cadena[-1])
print(cadena[3:6])
print(cadena[0:-2])
'''

# Concatenar cadenas
cadena1 = "Hola"
cadena2 = "Mundo"
concatenacion = cadena1 + " " + cadena2
#print(concatenacion)  # Resultado: Hola Mundo

# Multiplicación de cadenas
repeticion = "Python " * 3
#print(repeticion)  # Resultado: Python Python Python 

# Búsqueda en cadenas
texto = "Bienvenido a Python"
busqueda = "Python" in texto
#print(busqueda)  # Resultado: True

# Bucle for para sumar elementos de una lista
lista = [1, 2, 3, 4, 5]
suma = 0
for numero in lista:
    suma += numero
#print(suma)  # Resultado: 15

# Uso de enumerate para iterar con índices
frutas = ["manzana", "plátano", "cereza"]

#for indice, fruta in enumerate(frutas):
    #print(f"Índice {indice}: {fruta}")


x, y, z = 1, 2, 3
#print(x)
x, z, y = x, y, z  # Intercambio de valores
print(x, y, z)  # Salida: 1 3 2

