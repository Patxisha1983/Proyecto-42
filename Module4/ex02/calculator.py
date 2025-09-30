#!/usr/bin/env python3

# Solicitar al usuario que ingrese dos números
first_number = input("Give me the first number: ")
second_number = input("Give me the second number: ")

# Convertir las entradas de texto a números flotantes
first_number = float(first_number)
second_number = float(second_number)

# Mostrar un mensaje de agradecimiento
print("Thank you!")

# Realizar las operaciones y mostrar los resultados
print(f"{first_number} + {second_number} = {first_number + second_number}")
print(f"{first_number} - {second_number} = {first_number - second_number}")
print(f"{first_number} / {second_number} = {first_number / second_number}")
print(f"{first_number} * {second_number} = {first_number * second_number}")

