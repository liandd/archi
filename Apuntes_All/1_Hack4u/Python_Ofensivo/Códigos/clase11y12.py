#!/usr/bin/env python3
from functools import reduce

# Ambito de las variables
variable = "Soy global"
def funcion():
    print("Soy funcion y mi contenido de variable es: %s " % variable)

def funcion2():
    variable = "Soy local"
    print("Soy funcion2 y mi contenido ha sido editado local, {}".format(variable))

def funcion3():
    global variable
    variable = "Soy global pero he sido modificado con 'global'"
    print(f"Soy funcion3 y usando 'global' el contenido de variable es: {variable}")

print(variable)
funcion()
funcion2()
funcion3()
print("Se ha terminado ambito de variables, valor resultante de 'variable es {}'".format(variable))

# uso de funciones
def mi_funcion():
    print("Hola Mundo")

mi_funcion()

def saludo(nombre):
    print("Hola {}, un saludo!".format(nombre))

saludo("convolk")
saludo("nastya")

def suma(x, y):
    return x+y

print("La suma de los numeros es %d" % suma(8,10))

# uso de funciones lambda anonimas
mi_suma = lambda x,y: x+y
print("Usando lambda la suma es {}".format(mi_suma(6,4)))

lista = [1, 2, 3, 4, 5]
# Cuadrado de cada elemento usando lambda
cuadrado = list(map(lambda x: x**2, lista))
print(f"Los cuadrados de {lista} son : {cuadrado}")
# Numeros pares o impares
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = list(filter(lambda x: x % 2 == 0, numeros))
impares = list(filter(lambda y: y % 2 != 0, numeros))
print(f"Los numeros pares son {pares}")
print("Los numeros impares son {}".format(impares))
# Producto de un numero
numeros = [1, 2, 3, 4, 5]
producto = reduce(lambda x, y: x*y, numeros)
print(f"El ultimo producto de la lista es: {producto}")
