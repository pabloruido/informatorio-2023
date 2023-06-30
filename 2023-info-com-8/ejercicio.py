
6


def perfecto (numero):
    divisores = []
    for num in range(1, numero):
          if (numero % num == 0):
            divisores.append(num)

    if (numero == suma(divisores)):
        print("Es perfecto.")
    else:
        print("No es.")

def suma (numeros_lista):
    suma_de_lista = 0
    for num in numeros_lista:
        suma_de_lista += num

    return suma_de_lista

perfecto(int(input("Ingrese un numero: ")))
