#!/usr/bin/python3

import sys

# Verificar si se pasó exactamente un parámetro
if len(sys.argv) != 2:
    print("none")
else:
    # Obtener el parámetro pasado
    param = sys.argv[1]

    # Pedir al usuario que ingrese una palabra
    user_input = input("What was the parameter? ")

    # Comparar la entrada del usuario con el parámetro
    if user_input == param:
        print("Good job!")
    else:
        print("Nope, sorry…")

