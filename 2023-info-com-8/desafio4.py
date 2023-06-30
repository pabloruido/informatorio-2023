# Desafío 4: La inmobiliaria
# Requisitos técnicos:
# - Operadores.
# - Estructuras de datos.
# - Estructuras de control de flujo.
# - Funciones
# Una inmobiliaria de tu ciudad solicita un sistema para automatizar la gestión de sus inmuebles.
# Se te pide construir un programa que permita:
#  Agregar, editar y eliminar inmuebles a la lista.
# Las funciones deben ajustarse al formato de lista y reglas de validación.
#  Cambiar el estado de un inmueble, sin modificar sus demás datos.
# Las funciones deben ajustarse al formato de lista y reglas de validación.
#  Hacer búsqueda de inmuebles en función de un presupuesto dado.
# La función recibirá como entrada la lista de inmuebles y un precio, y devolverá otra lista con
# los inmuebles cuyo precio sea menor o igual que el dado y el estado sea Disponible o
# Reservado. Los inmuebles de la lista que se devuelva deben incorporar un nuevo par a cada
# diccionario con el precio del inmueble, donde el precio de un inmueble se calcula con las
# reglas de precio en función de la zona.
# Formato de lista
# [{'año': 2010, 'metros': 150, 'habitaciones': 4, 'garaje': True, 'zona': 'C', 'estado': 'Disponible'},
# {'año': 2016, 'metros': 80, 'habitaciones': 2, 'garaje': False, 'zona': 'B', 'estado': 'Reservado'},
# {'año': 2000, 'metros': 180, 'habitaciones': 4, 'garaje': True, 'zona': 'A', 'estado': 'Disponible'},
# {'año': 2015, 'metros': 95, 'habitaciones': 3, 'garaje': True, 'zona': 'B', 'estado': 'Vendido'},
# {'año': 2008, 'metros': 60, 'habitaciones': 2, 'garaje': False, 'zona': 'C', 'estado': 'Disponible'}]
# Reglas de validación
#  Inmuebles solo de zona: A, B o C.
#  Inmuebles con estado: Disponible, Reservado o Vendido.
#  No opera con inmuebles:
#  Anteriores al año 2000.
#  Menores de 60 metros cuadrados.
#  Menores de 2 habitaciones.
# Reglas de precio
#  Zona A: precio = (metros x 100 + habitaciones x 500 + garaje x 1500) x (1 - antigüedad / 100)
#  Zona B: precio = (metros x 100 + habitaciones x 500 + garaje x 1500) x (1 - antigüedad / 100) x 1.5
#  Zona C: precio = (metros x 100 + habitaciones x 500 + garaje x 1500) x (1 - antigüedad / 100) x 2

def agregar_inmueble(lista, inmueble):
    lista.append(inmueble)

def editar_inmueble(lista, indice, datos_actualizados):
    lista[indice].update(datos_actualizados)

def eliminar_inmueble(lista, indice):
    del lista[indice]

def cambiar_estado_inmueble(lista, indice, nuevo_estado):
    lista[indice]['estado'] = nuevo_estado

def buscar_inmuebles_por_presupuesto(lista, presupuesto):
    inmuebles_encontrados = []
    for inmueble in lista:
        if (inmueble['estado'] == 'Disponible' or inmueble['estado'] == 'Reservado') and calcular_precio(inmueble) <= presupuesto:
            inmueble_con_precio = inmueble.copy()
            inmueble_con_precio['precio'] = calcular_precio(inmueble)
            inmuebles_encontrados.append(inmueble_con_precio)
    return inmuebles_encontrados

def calcular_precio(inmueble):
    zona = inmueble['zona']
    metros = inmueble['metros']
    habitaciones = inmueble['habitaciones']
    garaje = inmueble['garaje']
    antiguedad = 2023 - inmueble['año']

    if zona == 'A':
        precio = (metros * 100 + habitaciones * 500 + garaje * 1500) * (1 - antiguedad / 100)
    elif zona == 'B':
        precio = (metros * 100 + habitaciones * 500 + garaje * 1500) * (1 - antiguedad / 100) * 1.5
    elif zona == 'C':
        precio = (metros * 100 + habitaciones * 500 + garaje * 1500) * (1 - antiguedad / 100) * 2
    
    return precio


def mostrar_menu():
    print("Bienvenido a la inmobiliaria")
    print("1. Agregar inmueble")
    print("2. Editar inmueble")
    print("3. Eliminar inmueble")
    print("4. Cambiar estado de inmueble")
    print("5. Buscar inmuebles por presupuesto")
    print("6. Salir")

def obtener_datos_inmueble():
    año = int(input("Año: "))
    metros = int(input("Metros cuadrados: "))
    habitaciones = int(input("Cantidad de habitaciones: "))
    garaje = input("Tiene garaje (S/N): ").upper() == 'S'
    zona = input("Zona (A/B/C): ").upper()
    estado = input("Estado (Disponible/Reservado/Vendido): ").capitalize()

    return {'año': año, 'metros': metros, 'habitaciones': habitaciones, 'garaje': garaje, 'zona': zona, 'estado': estado}

def mostrar_inmuebles(inmuebles):
    print("Listado de inmuebles:")
    for i, inmueble in enumerate(inmuebles):
        print(f"Inmueble {i+1}:")
        print("Año:", inmueble['año'])
        print("Metros cuadrados:", inmueble['metros'])
        print("Habitaciones:", inmueble['habitaciones'])
        print("Garaje:", "Sí" if inmueble['garaje'] else "No")
        print("Zona:", inmueble['zona'])
        print("Estado:", inmueble['estado'])
        print()

def mostrar_menu():
    print("Bienvenido a la inmobiliaria")
    print("1. Agregar inmueble")
    print("2. Editar inmueble")
    print("3. Eliminar inmueble")
    print("4. Cambiar estado de inmueble")
    print("5. Buscar inmuebles por presupuesto")
    print("6. Salir")

def agregar_inmueble(inmuebles, inmueble):
    inmuebles.append(inmueble)

def editar_inmueble(inmuebles, indice, datos_actualizados):
    if 0 <= indice < len(inmuebles):
        inmuebles[indice].update(datos_actualizados)

def eliminar_inmueble(inmuebles, indice):
    if 0 <= indice < len(inmuebles):
        inmuebles.pop(indice)

def cambiar_estado_inmueble(inmuebles, indice, nuevo_estado):
    if 0 <= indice < len(inmuebles):
        inmuebles[indice]['estado'] = nuevo_estado

def buscar_inmuebles_por_presupuesto(inmuebles, presupuesto):
    return [
        {**inmueble, 'precio': calcular_precio_inmueble(inmueble)}
        for inmueble in inmuebles
        if calcular_precio_inmueble(inmueble) <= presupuesto
        and inmueble['estado'] in ['Disponible', 'Reservado']
    ]

def calcular_precio_inmueble(inmueble):
    antiguedad = 2023 - inmueble['año']
    factor_zona = {'A': 1, 'B': 1.5, 'C': 2}
    return (inmueble['metros'] * 100 + inmueble['habitaciones'] * 500 + int(inmueble['garaje']) * 1500) * (1 - antiguedad / 100) * factor_zona[inmueble['zona']]

def ejecutar_programa():
    inmuebles = [
        {'año': 2010, 'metros': 150, 'habitaciones': 4, 'garaje': True, 'zona': 'C', 'estado': 'Disponible'},
        {'año': 2016, 'metros': 80, 'habitaciones': 2, 'garaje': False, 'zona': 'B', 'estado': 'Reservado'},
        {'año': 2000, 'metros': 180, 'habitaciones': 4, 'garaje': True, 'zona': 'A', 'estado': 'Disponible'},
        {'año': 2015, 'metros': 95, 'habitaciones': 3, 'garaje': True, 'zona': 'B', 'estado': 'Vendido'},
        {'año': 2008, 'metros': 60, 'habitaciones': 2, 'garaje': False, 'zona': 'C', 'estado': 'Disponible'}
    ]

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            agregar_inmueble(inmuebles, obtener_datos_inmueble())
            print("Inmueble agregado exitosamente.\n")
        elif opcion == '2':
            mostrar_inmuebles(inmuebles)
            indice = int(input("Seleccione el número de inmueble a editar: ")) - 1
            editar_inmueble(inmuebles, indice, obtener_datos_inmueble())
            print("Inmueble editado exitosamente.\n")
        elif opcion == '3':
            mostrar_inmuebles(inmuebles)
            indice = int(input("Seleccione el número de inmueble a eliminar: ")) - 1
            eliminar_inmueble(inmuebles, indice)
            print("Inmueble eliminado exitosamente.\n")
        elif opcion == '4':
            mostrar_inmuebles(inmuebles)
            indice = int(input("Seleccione el número de inmueble a modificar el estado: ")) - 1
            nuevo_estado = input("Ingrese el nuevo estado (Disponible/Reservado/Vendido): ").capitalize()
            cambiar_estado_inmueble(inmuebles, indice, nuevo_estado)
            print("Estado del inmueble cambiado exitosamente.\n")
        elif opcion == '5':
            presupuesto = float(input("Ingrese el presupuesto máximo: "))
            inmuebles_encontrados = buscar_inmuebles_por_presupuesto(inmuebles, presupuesto)
            mostrar_inmuebles(inmuebles_encontrados)
        elif opcion == '6':
            break
        else:
            print("Opción inválida. Por favor, seleccione nuevamente.\n")

ejecutar_programa()