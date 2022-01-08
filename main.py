"""
Ejercicio 2
Enunciado: Crea una agenda de teléfonos que se gestione por consola, que te permita:
    1) Añadir a cualquier persona, indicando nombre y después teléfono
    2) Buscar el teléfono de una persona
Objetivo:
    - Aprender a manejar la entrada y la salida por consola.
    - El uso de colecciones (array o diccionario)

Ampliación del ejercicio 2:
- Al buscar a una persona, que te muestre todas aquellas que comiencen por el texto que has introducido. Ejemplo:
   Introduce un nombre: Pep
   Resultados:
   - Pepe 659331013
   - Pepe Martín 633743551
"""
agenda = {"Rafael":"987","Rafa":"9876787","Radilo86":"3232","vero":"233","Rodrigo":"23432"}

def texto_menu():
    print("*****************************************")
    print("*\t\tMENU")
    print("* 1 - Añadir\n* 2 - Buscar (unico resultado)\n* 3 - Consultar\n* 4 - Buscar (patron)\n* 5 - Salir")
    print("*****************************************\n")

def menu(num):
    if (num == 1):
        añadir(agenda)
    elif (num == 2):
        buscar(agenda)
    elif (num == 3):
        consultar(agenda)
    elif (num == 4):
        buscarPatron(agenda)
    else:
        print("Opción incorrecta")

def añadir(agenda):
    nombre = input("Introduce el nombre: \n")
    telefono = input("Introduce el telefono: \n")
    if (nombre not in agenda):
        agenda[nombre] = telefono
    else:
        print("¡Este nombre ya existe en la agenda!")

def buscar(agenda):
    persona = input("Introduce el nombre a buscar: ")
    if persona not in agenda:
        print("Persona no encontrada, prueba otro nombre.")
    else:
        print(persona," --> ",agenda[persona])

def consultar(agenda):
    for elemento in agenda:
        print("**************************\nNombre: "+ elemento + "\nTelefono: " + agenda[elemento])

def buscarPatron(agenda):
    nombre=[]
    telefono=[]
    patron=input("Introduce el patrón a buscar: \n")
    for key in agenda:
        # find devuelve la posicion si lo encuentra y -1 si no aparece
        if key.find(patron) != -1:
            nombre.append(key)
            telefono.append((agenda[key]))

    # Devuelve la lista
    indice = 0
    while indice < len(nombre):
        print(nombre[indice],telefono[indice])
        indice=indice+1

if __name__ == "__main__":
    texto_menu()
    opcion = int(input("Introduce una opcion: " ))
    while opcion != 5:
        menu(opcion)
        if opcion != 5:
            texto_menu()
            opcion = int(input("Introduce una opcion: "))
    print("¡¡Hasta Pronto!!")
    exit()