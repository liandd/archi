#!/usr/bin/env python3

ip_address = "192.168.0.17"
print(ip_address)
print(type(ip_address))

port = 80
print(port)
print(type(port))

number = 4.5
print(number)
print(type(number))

print(int(number))
print(type(int(number)))

# Concepto Listas -> Array

my_ports = []
my_ports.append(22) # Primer Elemento
my_ports.append(80)
my_ports.append(443)

# Extiende la lista
my_ports.extend([22, 21, 84, 85])
my_ports += [8080, 87]
print(my_ports[0]) # -> Acceder al indice de la lista

for port in my_ports:
    print("El puerto " + str(port))

#print("El total de elementos en la lista es de: " + str(len(my_ports)))
print(f"El total de elementos en la lista es de: {len(my_ports)} elementos")

# Se ordena
my_ports = sorted(my_ports)

# Eliminar
del my_ports[1]

for port in my_ports:
    print(f"El puerto ordenado : {port}")


