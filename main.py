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
agenda = {"Rafael":"987"}

def menu(num):
    if (num == 1):
        añadir(agenda)
    elif (num == 2):
        buscar(agenda)
    elif (num == 3):
        consultar(agenda)
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

if __name__ == "__main__":
    opcion = int(input("Introduce una opcion (Presiona 4 para salir): " ))
    while opcion != 4:
        menu(opcion)
        if opcion != 4:
            opcion = int(input("Introduce una opcion: "))
    print("¡¡Hasta Pronto!!")
    exit()