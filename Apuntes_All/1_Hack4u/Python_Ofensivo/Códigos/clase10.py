#!/usr/bin/env python3

# Bucles for
nombres = ["alicia", "ekaterina", "nastya", "katerina"]
animals = ["perro" , "gato", "pez", "colibri"]
frutas = {"manzanas" : 3, "uvas" : 7, "bananos" : 5, "mangos" : 10}
my_list = [[2, 4, 6, 8], [1, 3, 5, 7]]
# Iterada de 0 a 4 -> igual a un seq en Bash
for i in range(5):
    print(i)

# Iteracion en lista
for animal in animals:
    print(f"El animal en esta iteracion es {animal}")

# Bucles while
i = 0
while i < 5:
    print("El valor de i para esta iteracion es {}".format(i))
    i = i + 1

# Usando enumerate -> crea un objeto que es iterable
# Retorna indice y elemento
for i, nombre in enumerate(nombres):
    print("Para la iteracion %d, el nombre es: %s" % (i + 1, nombre))

# Iteracion en diccionarios
for key, value in frutas.items():
    print(f"Hay {value} cantidad de la fruta {key}")

# Bucles anidados
for element in my_list:
    for element_in_list in element:
        print(element_in_list)

# Listas de comprension
odd_list = [1, 3, 5, 7, 9]
cuadrado_de_odd_list = [i ** 2 for i in odd_list]
print(cuadrado_de_odd_list)

# Break, Continue y else's en bucles
print("\n")
for i in range(10):
    if i == 5:
        break # rompe
    print(i)
print("\n")
for i in range(10):
    if i == 5:
        continue # salta a la siguiente iteracion
    print(i)
# Uso de else en for
for i in range(10):
    if i == 10:
        break
else:
    print("Bucle concluido exitosamente")
# -------------------
print("continua el flujo del programa exitosamente")

# While
i = 0
while i < 10:
    if i == 10:
        break
    i += 1
else:
    print("Bucle while concluido exitosamente")
