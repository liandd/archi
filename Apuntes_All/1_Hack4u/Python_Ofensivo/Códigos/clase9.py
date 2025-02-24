#!/usr/bin/env python3

name = "juan"
rol = "ingeniero"

edad = 20

# Concatenar y type casting
print("Hola mi nombre es " + name + "y soy un " + rol + ". Actualmente tengo " + str(edad) + "años.")
# Usando punteros con prioridades
print("Hola mi nombre es %s y soy un %s. Actualmente tengo %d años." % (name, rol, edad))
# Usando format con posiciones
print("Hola mi nombre es {} y soy un {}. Actualmente tengo {} años.".format(name, rol, edad))
# Usando format mediante indices posicionales para asignar texto
print("Hola mi nombre es {0} y soy un {0}. Actualmente tengo {0} años.".format(name, rol, edad))
# Usando f-strings y nombrando directamente la variable
print(f"Hola mi nombre es {name} soy un {rol}. Actualmente tengo {edad}")
