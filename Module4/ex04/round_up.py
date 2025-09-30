#!/usr/bin/env python3
import math

# Solicitar al usuario que ingrese un número
user_input = input("Give me a number: ")

# Convertir la entrada a un número flotante
number = float(user_input)

# Redondear el número hacia arriba
rounded_number = math.ceil(number)

# Mostrar el número redondeado
print(rounded_number)

