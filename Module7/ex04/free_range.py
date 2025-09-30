#!/usr/bin/python3
import sys

# Verificar si hay exactamente dos parámetros
if len(sys.argv) == 3:
    try:
        # Obtener los parámetros y convertirlos en números
        start = int(sys.argv[1])
        end = int(sys.argv[2])

        # Verificar que el primer número es estrictamente menor que el segundo
        if start < end:
            # Crear un rango de números entre start y end (inclusive)
            print(list(range(start, end + 1)))
        else:
            print("none")
    except ValueError:
        # Si no se pueden convertir los parámetros a enteros, mostrar "none"
        print("none")
else:
    # Si no se pasaron exactamente dos parámetros, mostrar "none"
    print("none")
