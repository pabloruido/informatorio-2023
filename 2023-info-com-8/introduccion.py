print ("hola mundo")

# Variables y tipos datos

### Tipos de datos simples

enteros = 11 # int -> integer -> entero en español\\\ = es operador de asignacion
reales = 11.22 # float -> reales (?)
      # tipos string, cadena de caracteres
strings = "hola"
strings1 = 'hola'
strings2 = f"hola"
strings3 = '''hola'''

bool_verdadero = True
bool_falso = False

### Tipos de datos complejos
listas = [1, 2, 3, 4, 5, 6, 7]
listas = [1] # devuelve 2

listas.sort() # ordeno la lista, tienen valores ordenables como por ejemplo numeros
listas.reverse() # listas = [5, 4, 3, 2, 1]

# agregar elementos
listas.append(32)

#sacar elementos
listas = [1, 2, 5, 6, 8, 10]
listas.pop() # elimina el ultimo elemento de la lista, el 10
listas.pop(2) # saca por indice, en este caso al 5
listas.remove (10)# saca por valor

# son estructuras de datos complejas estaticas
tuplas = (1, 3, 32, 13, 15)
print ('elemento 32 de la tubla', tuplas [2])
#tuplas [2] = 23 # no se puede CAMBIAR LOS VALORES DE LA TUPLAS
# print (tuplas[2])

valores_tuplas = list(tuplas)
print (type(valores_tuplas)) #type () para saber el tipo de dato
print ("antes de cambiar", valores_tuplas)
valores_tuplas [2]= 23
print("despues de cambiar", valores_tuplas)

#dict, set  ESTUDIAR O BUSCAR POR NUESTRO LADO