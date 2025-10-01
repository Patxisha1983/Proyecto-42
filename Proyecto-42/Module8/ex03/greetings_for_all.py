#!/usr/bin/python3

# Definir el método greetings
def greetings(name="noble stranger"):
    # Verificar si el argumento es una cadena
    if isinstance(name, str):
        print(f"Hello, {name}.")
    else:
        print("Error! It was not a name.")

# Llamadas al método con diferentes argumentos
greetings('Alexandra')
greetings('Wil')
greetings()
greetings(42)

