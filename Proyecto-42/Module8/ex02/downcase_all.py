#!/usr/bin/python3
import sys

# Definir el método downcase_it
def downcase_it(s):
    return s.lower()

# Verificar si se proporcionaron parámetros
if len(sys.argv) > 1:
    # Iterar sobre cada parámetro (excluyendo el nombre del script)
    for param in sys.argv[1:]:
        print(downcase_it(param))
else:
    print(“none")

