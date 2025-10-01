#!/usr/bin/env python3

# Solicitar al usuario que ingrese un número
user_input = input("Give me a number: ")

# Intentar convertir el número a un tipo flotante
try:
    number = float(user_input)
    
    # Comprobar si el número es entero (sin decimales)
    if number.is_integer():
        print("This number is an integer.")
    else:
        print("This number is a decimal.")
except ValueError:
    print("Thats not a valid number.")
    
    # El comanda no reconoce la comilla de contracción de That is not



