# a revisar
#!/usr/bin/python3
import sys

# Definir el método shrink
def shrink(s):
    print(s[:8])

# Definir el método enlarge
def enlarge(s):
    print(s.ljust(8, 'Z'))

# Verificar si se proporcionaron parámetros
if len(sys.argv) > 1:
    for param in sys.argv[1:]:
        if len(param) > 8:
            shrink(param)
        elif len(param) < 8:
            enlarge(param)
        else:
            print(param)
else:
    print(“none")

