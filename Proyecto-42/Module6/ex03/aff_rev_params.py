#!/usr/bin/python3
import sys

# Verificar si hay al menos dos parámetros
if len(sys.argv) > 1:
    # Mostrar los parámetros en orden invertido, excluyendo el nombre del script
    for param in reversed(sys.argv[1:]):
        print(param)
else:
    # Si no hay al menos dos parámetros, mostrar "none"
    print(“none")

