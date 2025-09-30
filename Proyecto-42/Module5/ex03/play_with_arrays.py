#!/usr/bin/env python3

# Definir un array de números
original_array = [2, 8, 9, 48, 8, 22, -12, 2]

# Crear un nuevo array sumando 2 a los valores mayores a 5 del array original
new_array = {x + 2 for x in original_array if x > 5}

# Mostrar el array original y el nuevo array procesado (sin duplicados)
print(original_array)
print(new_array)

