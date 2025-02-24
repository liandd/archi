#!/usr/bin/env python3

#Conjutos sets {}, -> no guarda repetidos usando el typeCast set(mi_lista)
# Busquedas rapidas -> print(1234 in mi_conjunto) -> retorna true o falseo
# ambas -> intersection
# todas -> union
# diferente -> difference los que no estas en intersection

mi_conjunto = {1, 2, 3}
print(mi_conjunto)
print(type(mi_conjunto))
mi_conjunto.add(4)
mi_conjunto.add(5)
print(mi_conjunto)
mi_conjunto.update({6, 7, 8, 9, 10})
print(mi_conjunto)
mi_conjunto.remove(6)
print(mi_conjunto)
# ALternativa a borrado sin error
mi_conjunto.discard(11)
print(mi_conjunto)
# podemos crear intersecciones -> repetidos
mi_conjunto2 = {4, 5, 6, 11, 12, 13, 14, 15}
resultado = mi_conjunto.intersection(mi_conjunto2)
print(resultado)
# unir conjuntos con union
resultado2 = mi_conjunto.union(mi_conjunto2)
print(resultado2)
# subconjutos
p1_set = {1, 2, 3, 4}
p2_set = {1, 2, 3, 4, 5, 6, 7, 8, 9}
print(p1_set.issubset(p2_set)) # para todos los elementos True
# Basta con que UN SOLO elemento no este, retorna False


