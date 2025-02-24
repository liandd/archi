#!/usr/bin/env python3
#clase 8 Operadores Basicos
# a + b, a - b, a ** b, a/b, a%b
first_number = 222
second_number = 4
result = first_number ** second_number
print("{:,}".format(result).replace(",","."))

# Cadenas
first_str = "Hola"
second_str = " "
third_str = "Mundo!"
print(first_str + second_str + third_str)
print(first_str * 3)
print(first_str[0] * 3)
print(third_str[0:3] * 8)

# Listas
odd_numbers = [1, 3, 5, 7, 9]
even_numbers = [2, 4, 6, 8, 10]
result = odd_numbers + even_numbers
print(result)

# ZIP
result = zip(odd_numbers, even_numbers) # -> crea objeto
# MAP -> iterador de cada tupla hecha por zip y aplicar operatorias
result = list(map(sum, zip(odd_numbers, even_numbers))) # -> sum suma
print(result)
for element in result:
    print(element)
