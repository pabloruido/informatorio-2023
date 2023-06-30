# Se te pide crear un programa que le pida al usuario que ingresar un texto
# cualquiera, por ejemplo, un artículo o una frase.
# Luego el programa le va a pedir al usuario que también ingrese 3 letras a su
# elección.
# Nuestro código va a procesar esa información para realizar los análisis
# necesarios para devolverle al usuario la siguiente información:
# 1- Cantidad de veces que aparece cada una de letras que eligió.
# Tip 1: almacenar las letras en una lista para usar algún método de contar un substring en un
# string
# Tip 2: al buscar las letras puede haber mayúscula y minúsculas. Para asegurar que se
# encuentren todas las letras, pasa tanto el texto original como las letras a buscar a
# minúscula
# 2- Cuantas palabras hay en total en todo el texto.
# Tip 3: usa métodos para transformar el texto en lista de palabras y para calcular su longitud.
# 3- Cual es la primera letra y cuál es la última. (Indexación)
# 4- Mostrar el texto en orden inverso.
# 5- Decir si la palabra "python" aparece en el texto.
# Tip 4: usa bool para verificar si se encuentra, y un diccionario para asociar el booleano con un
# string para mostrar al usuario
texto = str(input('por favor ingrese un texto, articulo o frase: '))

letra1 = str(input('por favor ingrese una letra: '))
letra2 = str(input('por favor ingrese otra letra: '))
letra3 = str(input('por favor ingrese la tercera letra: '))

texto = texto.lower()  #transforme todo el texto a minusculas, o utilizando #upper() podria pasarlo a min.
letras = [letra1.lower(), letra2.lower(), letra3.lower()]

for letra in letras:
    print(f'La letra {letra} aparecio {texto.count(letra)} veces')

palabras = texto.replace ('.','')
palabras = palabras.replace (':','')
palabras_separadas = palabras.split ( )
cantidad_de_palabras = len(palabras_separadas)
print ('la cantidad de palabras que hay en el texto es de: ', cantidad_de_palabras)

print ('la primer letra es ', palabras [0], 'y la ultima letras es:', palabras [-1])

palabras_reversa = palabras_separadas [::-1]
print ('texto en forma inversa: ', palabras_reversa)

opciones = {True: "existe", False: "no existe"}
existePython = "python" in texto
print (f'la palabra python', opciones [existePython],'en el texto ingresado')
