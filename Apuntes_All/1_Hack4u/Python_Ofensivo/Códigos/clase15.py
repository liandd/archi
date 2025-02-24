#!/usr/bin/env python3

# Repaso listas
cve_list = ['CVE-2023', 'CVE-2021', 'CVE-2024']
puertos_tcp = [21, 22, 25, 80, 443, 8080, 445, 69]
print(puertos_tcp)
print(len(puertos_tcp))
puertos_tcp.append(80)
print(len(puertos_tcp))

for puerto in puertos_tcp:
    print("Este es el puerto: {}".format(puerto))

print(cve_list)
cve_list.remove('CVE-2023')
print(cve_list)

# ordenar
puertos_tcp.sort()
print(f"Los puertos ordenados son: {puertos_tcp}")
puertos_tcp.reverse()
print("Se han revertido los puertos: {}".format(puertos_tcp))

# Poner listas en mayuscula
# animales = ["perro", "gato", "pez"]
# animales_mayus = [animal.upper() for animal in animales]
# animales_minus = [animal.lower() for animal in animales]

# Zip para combinatorias de listas
frutas = ["manzanas", "uvas", "mangos", "kiwis"]
cantidades = [3, 5, 6, 10]

for fruta, cantidad in zip(frutas, cantidades):
    print("cantidad %d de %s" % (cantidad, fruta))
