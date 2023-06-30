# 1-Escribe un programa que solicite al usuario su nombre y lo imprima en la
# pantalla.

# nombre = input ('Por favor, ingrese su nombre: ')
# print ('su nombre es: '+ nombre)

#2-Escribe un programa que solicite al usuario su nombre y luego imprima un
#mensaje de bienvenida.

#nombre = input ('Si tuviera usted la amabilidad de colocar aqui su nombre:')
#print ('Sea usted muy bienvenido ' + nombre + " petero")

# 3-Crea un programa que pida al usuario su edad y lo imprima en pantalla.
#edad = input ('Por favor coloque su edad: ')
#print ('su edad es '+ edad)

# 4-Crea un programa que calcule la suma de dos números y lo imprima en
# pantalla.

# numero1 = int(input ('ingrese un numero: '))
# numero2 = int(input ('ingrese otro numero: '))
# suma = numero1 + numero2
# print ('el resultado de la suma de los dos numeros ingresados es: ', suma)

# 5-Crea un programa que pida al usuario dos números enteros y muestre en
# pantalla su cociente y su resto.

# numero1 = int(input('Por favor ingrese un numero '))
# numero2 = int(input('Por favor ingrese otro numero '))
# cociente = numero1 // numero2
# resto = numero1 % numero2
# print ('el cociente de los numeros ingresados es: ', cociente, ' y el resto de los numeros es ', resto )

# 6-Crea un programa que pida al usuario el radio de un círculo y calcule su área.
# La fórmula A = pi * r^2. Luego, muestra en pantalla el resultado.
# Supongamos que pi = 3.1416
# pi = 3.1416
# radio = int(input('por favor ingrese el radio del circulito '))
# area = pi * radio ** 2
# print ('el area del circulito es ', area )

# 7-Escribe un programa que calcule el área de un triángulo a partir de la base y la
# altura dadas

# base = int(input('por favor ingrese la base del triangulo '))
# altura = int(input('y ahora ingrese la altura del mismo '))
# area = base * altura
# print ('el area del triangulo es ', area )

#8-Crea un programa que pida al usuario el radio de un círculo y muestre su
#diámetro, su circunferencia y su área.
#Supón que pi es aproximadamente 3.14159.

# pi = 3.14159
# radio = int(input('por favor ingrese el radio del circulo del cual desea saber su diametro, circunferencia y su area: '))
# diametro = radio + radio
# circunferencia = pi * diametro
# area = pi * radio ** 2
# print ('el diamentro del circulo es ', diametro)
# print ('la circunferencia del circulo es ', circunferencia)
# print ('el area del circulo es ', area)

# 9-Escribe un programa que solicite al usuario dos números y luego imprima la
# suma, la resta, la multiplicación y la división de los dos números.

# numero1 = int(input('por favor ingrese un numero: '))
# numero2 = int(input('por favor ingrese otro numero, puede ser igual al anterior: '))
# suma = numero1 + numero2
# resta = numero1 - numero2
# multiplicacion = numero1 * numero2
# division = numero1 / numero2
# print ('la suma entre ambos numeros es ', suma)
# print ('la resta entre ambos numeros es ', resta)
# print ('la multiplicacion de los numeros da ', multiplicacion)
# print ('la division de los numeros ingresados es ', division)

# 10-Crea un programa que pida al usuario una cantidad en dólares y la convierta a
# euros.
# Supón que el tipo de cambio es de 0.84 euros por dólar.

# euro = 0.84
# dolares = float(input ('por favor ingrese la cantidad de dolares que deseé convertir a euros: '))
# euros_convertidos = dolares * euro
# print ('usted tiene un equivalente de ', euros_convertidos)

# 11-Crea un programa que pida al usuario una palabra y muestre en pantalla
# cuántas letras tiene.

# palabra = str(input('por favor ingrese una palabra: '))
# cantidad_de_letras = len(palabra)
# print ('la palabra ingresada tiene ',cantidad_de_letras , 'letras')

# 12-Escribe un programa que solicite al usuario su fecha de nacimiento en formato
# dd/mm/aaaa y luego imprima su edad en años.
# Utiliza la función .split()

# import datetime
# print ('por favor ingrese su fecha de nacimiento en formato dd/mm/yyyy')
# fecha_nacimiento = input()
# dia, mes, anio = map(int, fecha_nacimiento.split ('/'))
# fechaactual = datetime.date.today()
# edad = fechaactual.year - anio 
# if ( mes > fechaactual.month) or (mes == fechaactual.month and dia > fechaactual.day):
#     edad = edad - 1
# print('tu edad es de ', edad ,'años')

# 13-Escribe un programa que solicite al usuario su nombre y su edad, y luego
# imprima un mensaje que indique cuántos años tendrá el usuario en 10 años más

# nombre = (input('por favor ingrese su nombre: '))
# edad = int(input('por favor ingrese su edad: '))
# endiezaños = edad + 10
# print (nombre, 'cuando pase una decada tendras ', endiezaños, 'años')

# 14-Escribe un programa que solicite al usuario un número entero y luego
# imprima el doble y el triple de ese número.

# numero = int(input('por favor ingrese un numero: '))
# doble = numero * 2
# triple = numero * 3
# print ('el doble del numero ingresado es ', doble)
# print ( 'el tribple del numero ingresado es ', triple)

# 15-Escribe un programa que solicite al usuario una temperatura en grados
# Celsius y luego imprima la temperatura equivalente en grados Fahrenheit.
# La fórmula para convertir de Celsius a Fahrenheit es: F = (C * 1.8) + 32

# celsius = float(input('por favor ingrese una temperatura en grados celsius: '))
# fahrenheit = (celsius * 1.8) + 32
# print ('la temperatura ingresada, transformada a grados Fahrenheit es de ', fahrenheit)

# 16-Escribe un programa que solicite al usuario su peso y su altura, y luego calcule
# e imprima su índice de masa corporal (IMC).
# La fórmula para calcular el IMC es: IMC = peso / (altura ** 2).

# peso = float(input('por favor ingrese su peso: '))
# altura = float(input('por favor ingrese su altura: '))
# masa_corporal = peso / (altura ** 2)
# print ('Su indice de masa corporal es de ', masa_corporal)

# 17-Escribe un programa que solicite al usuario dos palabras y luego las imprima
# en orden inverso.
# Por ejemplo, si el usuario ingresa "hola" y "mundo", el programa debe imprimir
# "mundo hola".
# Importante!!! Utiliza un solo print() 😈.

# palabra1 = str(input('por favor ingrese una palabra: '))
# palabra2 = str(input('por favor ingrese otra palabra: '))
# print (palabra2, palabra1)

# 18-Crea un programa que pida al usuario su nombre, su edad y su ciudad de
# residencia, y lo muestre en pantalla Utilizando una sola línea de código.
# *Recuerda el print() del ejercicio anterior

# nombre = str(input('por favor ingrese su nombre: '))
# edad = int(input('por favor ingrese su edad: '))
# ciudad = str(input('por favor ingrese su ciudad de residencia: '))
# print ('su nombre es',nombre, 'tiene', edad,'años ','y vive en la ciudad de ',ciudad)

# 19-Escribe un programa que solicite al usuario un número decimal y luego
# imprima la parte entera y decimal por separado

# numero_decimal = float(input('por favor ingrese un numero decimal: '))
# entero = int(numero_decimal)
# decimal = numero_decimal - entero
# print('la parte entera es: ',entero ,'y la parte decimal es ', decimal)

