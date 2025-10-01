#!/usr/bin/env python3

# Primer bucle while para las tablas de multiplicar del 0 al 10
i = 0
while i <= 10:
	print(f"Table of {i}:", end=" ")
	# Segundo bucle while para calcular los productos 
	j = 0
	while j <= 10:
		print(i * j, end =" ")
		j += 1
	print() # Salto de línea después de cada tabla
	i += 1 # Avanza al siguiente número de la tabla



