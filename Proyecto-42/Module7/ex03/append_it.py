#!/usr/bin/python3
import sys

# Verificar si hay parámetros
if len(sys.argv) > 1:
    # Iterar sobre los parámetros (excluyendo el nombre del script)
    for param in sys.argv[1:]:
        # Si el parámetro no termina con "ism", agregar "ism" y mostrarlo
        if not param.endswith("ism"):
            print(f"{param}ism")
else:
    # Si no hay parámetros, mostrar "none"
    print("none")

