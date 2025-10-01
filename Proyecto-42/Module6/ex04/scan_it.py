#!/usr/bin/python3
import sys
import re

# Verificar si se recibieron exactamente dos parámetros
if len(sys.argv) == 3:
    keyword = sys.argv[1]
    search_string = sys.argv[2]

    # Usar re.findall() para encontrar todas las ocurrencias de la palabra clave
    matches = re.findall(r'\b' + re.escape(keyword) + r'\b', search_string)

    # Imprimir el número de ocurrencias
    print(len(matches))
else:
    # Si no hay exactamente dos parámetros, mostrar "none"
    print(“none")

