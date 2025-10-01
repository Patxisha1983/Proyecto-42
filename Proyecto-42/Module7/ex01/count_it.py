#!/usr/bin/python3
import sys

# Verificar si hay parámetros
if len(sys.argv) > 1:
    # Mostrar el número total de parámetros
    print(f"parameters: {len(sys.argv) - 1}")
    
    # Iterar sobre cada parámetro (excluyendo el nombre del script)
    for param in sys.argv[1:]:
        # Mostrar el parámetro y su longitud
        print(f"{param}: {len(param)}")
else:
    # Si no hay parámetros, mostrar "none"
    print("none")

