#!/usr/bin/env python3

tupla = (1, 2, 3, 4, 5)
print(tupla)
print(type(tupla))
print(tupla[1:3])
print(tupla[:4])
# No podemos modificar la tupla, son inmutables -> estaticas

# asignar
a, b, c, d, e = tupla
print("Valores de %d, %d, %d, %d, %d" % (a, b, c, d, e))
tupla = tupla + (6, 7, 8, 9, 10)
print(tupla)
tupla_pares = tuple(i for i in tupla if i % 2 == 0)
print(tupla_pares)
