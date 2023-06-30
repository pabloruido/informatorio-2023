# 1-Escribir un programa que pida al usuario su edad y muestre por pantalla si es
# mayor de edad (18 años o más) o no.

# edad = int(input("por favor ingrese su edad: "))
# if edad >= 18:
#     print ("sos mayor de edad, si hay delito no hay pelito")
# else:
#     print ("sos menor, no jodas.")

# 2-Escribir un programa que pida al usuario un número entero y muestre por
# pantalla si es positivo, negativo o cero.

# entero = int(input("por favor ingrese un numero entero: "))
# if entero > 0:
#     print ("es un numero positivo!!, Pronto te dira que todo va a mejorar y que todo pasa")
# elif entero == 0:
#     print ("es un 0, no tiene un valor, pero seguramente tenga precio")
# else:
#     print ("es un numero negativo, seguramente leyo a schopenhauer.")

# 3-Escribir un programa que pida al usuario dos números y muestre por pantalla
# cuál de ellos es mayor.
  
# numero1 = int(input("por favor ingrese un numero: "))
# numero2 = int(input("por favor ingrese otro numero:"))
# if numero1 > numero2:
#     print("el numero mayor entre los dos es", numero1)
# elif numero2 > numero1:
#     print ("el numero mayor entre ambos es", numero2)
# else:
#     print ("los numeros son de igual valor.")

# 4-Escribir un programa que pida al usuario una nota del 0 al 10 y muestre por
# pantalla si está aprobado (5 o más) o no.

# nota = int(input("por favor ingrese la nota que usted ha sacado en el parcial: "))

# if nota >= 8:
#     print("que weno que es uste po wn, de lo mejor de la clase.")
# elif nota >= 6:
#     print("no tai mal pero tampoco ta taan bien, pero usted se encuentra aprobaO")
# else:
#     print("ya po wn, vuelva en marzo.")

# 5-Escribir un programa que pida al usuario un número entero y muestre por
# pantalla si es par o impar.

# numero = int(input("ingrese un numero sin decimales: "))
# if numero % 2 == 0:
#     print("es un numero par")
# else:
#     print ("Es un impar.")

# 6-Escribir un programa que pida al usuario un número entero y muestre por
# pantalla si es múltiplo de 2 y de 3 a la vez

# numero = int(input("por favor ingrese un numero: "))
# if numero % 2==0 and numero % 3==0:
#     print("este numero es multiplo de dos y de tres.")
# else:
#     print("este numero no es multiplo de 2 y/o 3")

# 7-Escribir un programa que pida al usuario un carácter y muestre por pantalla si
# es una letra mayúscula, una letra minúscula, un número o un carácter especial.

# caracter = input("por favor ingrese un caracter: ")
# if caracter.isalpha() and caracter.isupper():
#     print("es una letra y es mayuscula")
# elif caracter.isalpha() and caracter.islower():
#     print("es una letra en minuscula")
# elif caracter.isdigit():
#     print("es un numero")
# else:
#     print("es un caracter especial")

# 8-Escribir un programa que pida al usuario una cadena de caracteres y muestre
# por pantalla si contiene la letra "a".

# loquequieras = str(input("por favor ingrese un texto, frase, palabra, o tipo de cadena de caracteres que quiera: "))
# if "a" in loquequieras:
#     print("la letra A se encuentra en la cadena.")
# else:
#     print("no hay letra A en lo introducido.")

# 9-Escribir un programa que pida al usuario tres números y muestre por pantalla
# el mayor de ellos.

# numero1 = int(input("ingrese un numero: "))
# numero2 = int(input("ingrese un numero: "))
# numero3 = int(input("ingrese un numero: "))

# if numero1 > numero2 and numero1>numero3:
#     print("el mayor es el", numero1)
# elif numero2 > numero1 and numero2>numero3:
#     print("el mayor es el", numero2)
# else:
#     print("el mayor es el", numero3)

# 10-Escribir un programa que pida al usuario una letra y muestre por pantalla si es
# una vocal o una consonante

# letra = str(input("por favor ingrese una letra: "))
# vocales = ["a","e","i","o","u","A","E","I","O","U"]
# if letra in vocales:
#     print("es una vocal")
# else: 
#     print("es una consonante")

# 11-Escribir un programa que pida al usuario dos números y muestre por pantalla
# la suma de ellos solo si ambos son pares

# num1 = int(input("por favor ingrese un numero: "))
# num2 = int(input("por favor ingrese otro numero: "))
# if num1 % 2 == 0 and num2 % 2 == 0:
#     print(num1 + num2)
# else:
#     print("no son numeros pares.")