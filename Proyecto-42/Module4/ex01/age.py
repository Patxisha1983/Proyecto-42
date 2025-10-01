#!/usr/bin/env python3

# Solicitar la edad del usuario
age = input("Please tell me your age: ")

# Convertir la edad de string a entero
age = int(age)

# Calcular la edad en 10, 20 y 30 años
age_in_10 = age + 10
age_in_20 = age + 20
age_in_30 = age + 30

# Mostrar la edad actual y las edades futuras
print(f"You are currently {age} years olr.")
print(f"In 10 years, you'll be {age_in_10} years old.")
print(f"In 20 years, you'll be {age_in_20} years old.")
print(f"In 30 years, you'll be {age_in_30} years old.")




