#!/usr/bin/python3
import sys

# Verificar si se pasó exactamente un parámetro
if len(sys.argv) == 2:
    input_string = sys.argv[1]

    # Buscar todas las ocurrencias de "z" en el string (en minúsculas)
    z_count = input_string.lower().count('z')

    # Si hay ocurrencias de "z", imprimir "z" por cada ocurrencia
    if z_count > 0:
        print('z' * z_count)
    else:
        # Si no hay "z" en el string, mostrar "none"
        print("none")
else:
    # Si no se pasa exactamente un parámetro, mostrar "none"
    print("none")


