# Mini-proyecto: "Agenda de Contactos"
# Descripción:
# Crea una pequeña agenda que permita:

# Agregar un nuevo contacto (nombre y número de teléfono).

# Buscar un contacto por su nombre.

# Mostrar todos los contactos.

# Eliminar un contacto.

# Requisitos:
# Usar un diccionario donde el nombre sea la clave y el número sea el valor.

# Crear un pequeño menú en consola para elegir las acciones.

agenda = {
    "ricardo" : 6008512,
    "santiago": 5004512,
    "julian": 3005487,
}

listAgenda = []

def solo_letras(cadena):
    return cadena.isalpha()


def validar_numero(entry):
    return entry.isdigit()

while True:
    print("\n Menu:")
    print("1. Agregar nuevo contacto")
    print("2. Buscar un contacto por su nombre")
    print("3. Mostrar todos los contactos")
    print("4. Eliminar un contacto")
    print("5. Actualizar un contacto")
    print("6. Salir del programa...")
    
    opcion = input("Elige una Opcion: ")
    
    match opcion:
        case "1":
            while True:
                newContac = input("\n Agrega el nombre: ").lower()
                if solo_letras(newContac):
                    break
                else:
                    print("solo se permiten letras")

            while True:
                newNum = input("\n Agrega el numero: ")
                if validar_numero(newNum):
                    break
                else:
                    print("Solo se permiten numeros enteros")
                    
            agenda[newContac] = newNum

            listDic = {newContac : newNum}
            listAgenda.insert(0,listDic)
            print(listAgenda)

            print(f"El contacto {newContac} se ha agregado con el numero {newNum}")
              
            
            
        case "2":
            while True:
                findName = input("Coloca el nombre del contacto que deseas buscar: ").lower()
                if findName in agenda:
                    print(f"\n El contacto {findName} tiene el numero {agenda[findName]}")
                    findName1 = findName         
                    print(f"\n El contacto1 es:", listAgenda[{findName1}]  )
                    break
                else:
                    print("El contacto no existe")
                
            

        case "3":
            print (agenda)
            print (listAgenda)
        case "4":
            while True:
                delName = input("Coloca el nombre del contacto que deseas borrar: ").lower()
                if delName in agenda:
                    print(f"El contacto {delName} ha sido eliminado")
                    del agenda[delName]
                    break
                else:
                    print("El contacto no existe")
        case "5":
            while True:
                findName = input("Coloca el nombre del contacto que deseas actualizar: ").lower()
                if findName in agenda:
                    print(f"\n El contacto que se va a actualizar es: {findName}: {agenda[findName]}")
                    del agenda[findName]
                    break
                else:
                    print("El contacto no existe")
            
            while True:
                newContac = input("\n Agrega el nombre que deseas actualizar: ").lower()
                if solo_letras(newContac):
                    break
                else:
                    print("solo se permiten letras")

            while True:
                newNum = input("\n Agrega el numero que deseas actualizar: ")
                if validar_numero(newNum):
                    break
                else:
                    print("Solo se permiten numeros enteros")
                    
            agenda[newContac] = newNum
            print(f"El contacto {newContac} se ha actualizado con el numero {newNum}")

        case "6":
            break
        case _:
            print("Opcion no valida, por favor elige una Opcion del menu.")
