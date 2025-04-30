# dictionary = {
#     "name" : "ricardo",
#     "last name": "carmona",
#     "age" : 22,
#     "id" : 105046,
# }

# vehiculo = {
#     "type" : "moto",
#     "plate" : "atf67h",
#     "serial" : 12345,
# }

# print("desde terminal: ", vehiculo["type"])

# # vehiculo["type"] = "carro"
# # print(vehiculo["type"])
# # del vehiculo["serial"]

# # vehiculo["peso"] = "156kg"
# # print(vehiculo)

# for key,value in vehiculo.items():
#     print(f"{key}: {value}")



# Parte 1: Básicos
# Crea un diccionario llamado auto que contenga:

# Marca

# Modelo

# Año

# Cambia el modelo del auto a otro diferente.

# Agrega una nueva clave color al diccionario.

# Elimina la clave año.

# Imprime todas las claves del diccionario usando un bucle for.

# Imprime todos los valores del diccionario usando un bucle for.

# parte 1
# auto = {
#     "marca" : "mazda",
#     "modelo" : "2026",
#     "año" : "2025"
# }

# auto["marca"] = "mercedes"
# auto["color"] = "Rojo"
# del auto["año"]

# for key,value in auto.items():
#     print(f"{key}")


# for key,value in auto.items():
#     print(f"{value}")


# Parte 2: Intermedio
# Crea un diccionario paises donde las claves sean nombres de países y los valores sus capitales.


# paises = {
#     "colombia" : "Bogota",
#     "chile": "Santiago de Chile",
#     "peru" : "Lima"
# }


# Escribe un programa que pregunte al usuario un país y devuelva su capital (si existe).


# question = input("Escribe un pais: ").lower()

# for key,value in paises.items():
#     if question == key:
#         print(f"La capital es: {value} ")    
#         break
#     else:
#         print("pais no valido")
#         break





# Invierte el diccionario paises, es decir, que las capitales sean las claves y los países los valores.

# paises = {
#     "colombia" : "Bogota",
#     "chile": "Santiago de Chile",
#     "peru" : "Lima"
# }

# value_key = {key: value for value, key in paises.items()}

# print(value_key)


# Crea un diccionario de estudiantes donde las claves sean los nombres y los valores sus notas finales.
# Después imprime los nombres de los estudiantes que aprobaron (nota mayor o igual a 6)

estudiantes = {
    "Ricardo" : 7,
    "Sebastian" : 5,
    "Santiago" : 7,
    "Maria" : 4
}

for key,value in estudiantes.items():
    if value >= 6:
        print(f"El estudiante {key} aprobo con: {value}")
    else:
        print(f"El estudiante {key} no aprobo con: {value}")



# frutas = ["manzana", "mango", "manzana", "banano", "naranja"]
# conterName = {}

# for nombre in frutas:
#     if nombre in conterName:
#         conterName[nombre] +=1
#     else:
#         conterName[nombre] = 1

# print(conterName)