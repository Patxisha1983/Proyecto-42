#!/usr/bin/python3
import sys

# Verificar si el número de parámetros es exactamente 1
if len(sys.argv) == 2:
    # Convertir el string a mayúsculas y mostrarlo
    print(sys.argv[1].upper())
else:
    # Si no hay exactamente un parámetro, mostrar "none"
    print("none")



