# a revisar

#!/usr/bin/python3

# Definir el método array_of_names
def array_of_names(names_dict):

	 # Crear una lista para almacenar los nombres completos
    full_names = []

	 # Iterar sobre cada entrada en el diccionario
    for first_name, last_name in names_dict.items():
        # Capitalizar el primer nombre y el apellido
        full_name = f"{first_name.capitalize()} {last_name.capitalize()}"
        full_names.append(full_name)

	# Devolver la lista de nombres completos
	return full_names
	
# Diccionario de personas con nombres y apellidos
persons={
"jean":"valjean"
"grace":"hopper",
"xavier":"niel",
"fifi":"brindacier"
}

#Imprimir el resultado del método
print(array_of_names(persons))


