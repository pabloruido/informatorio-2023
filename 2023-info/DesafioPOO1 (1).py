# GRUPO 3 - COMISION 5
# ---INTEGRANTES---
# RAMIREZ FERNANDO ARIEL
# FERNANDEZ D'ELIA SOL
# DINERSTEIN BERNARDO
# RAMIREZ NICOLAS ALEJANDRO

from datetime import datetime

class Usuario:
    contador = 0

    def __init__(self, id, nombre, apellido, telefono, username, email, contraseña):
        self.__id = id
        self.nombre = nombre
        self.apellido = apellido
        self.__telefono = telefono
        self.username = username
        self.__email = email
        self.__contraseña = contraseña
        self.fechaderegistro = datetime.now()
        self.avatar = None
        self.estado = "Mi estado"
        self.online = False      

    def registrar(self):
        Usuario.contador += 1
        print("---REGISTRO---")
        self.__id = Usuario.contador
        self.nombre = input("Ingrese su nombre: ")
        self.apellido = input("Ingrese su apellido: ")
        self.__telefono = input("Ingrese su telefono: ")
        self.username = input("Ingrese su nombre de usuario: ")
        self.__email = input("Ingrese su correo electronico: ")
        self.__contraseña = input("Ingrese su contraseña: ")

        print("Te registraste con exito, bienvenido.")

    def login(self):
        username = input("Ingrese su usuario: ")
        contraseña = input("Ingrese su contraseña: ")
        if self.username == username and self.__contraseña == contraseña:
            print("Iniciaste sesión.")
            self.online = True
            return True
        else:
            print("Nombre de usuario o contraseña incorrectos.")
            return False
        
    def get_id(self):
        return self.__id
    
    def get_telefono(self):
        return self.__telefono
    
    def get_email(self):
        return self.__email
    
    def get_contraseña(self):
        return self.__contraseña

class Publico(Usuario):
    contador1 = 0
    def __init__(self, id, nombre, apellido, __telefono, username, __email, __contraseña):
        super().__init__(id, nombre, apellido, __telefono, username, __email, __contraseña)
        self.es_publico = True

    def comentar(self):
        Publico.contador1 += 1
        if self.online and self.es_publico:
            id_comentario = Publico.contador1
            id_usuario = usuario1.get_id()
            id_articulo = input("Selecciona el articulo para comentar: ")
            contenido = input("Ingresa un comentario: ")
            comentario = Comentario(id_comentario, id_articulo, id_usuario, contenido)
            print("Gracias por dejar tu comentario.")
        else:
            cuenta_existente = input("¿Ya tienes una cuenta creada? (Si / No):")
            if cuenta_existente.upper() == "si" or cuenta_existente.upper() == "SI":
                return super().login()     
            elif cuenta_existente.upper() == "NO" or cuenta_existente.upper() == "no":                
                return super().registrar()
            else:
                print("Opcion invalida.")


class Colaborador(Usuario):
    contador2 = 0
    contador3 = 0
    def __init__(self, id, nombre, apellido, __telefono, username, __email, __contraseña):
        super().__init__(id, nombre, apellido, __telefono, username, __email, __contraseña)
        self.es_colaborador = True
        self.es_publico = True

    def comentar(self):
        Colaborador.contador2 += 1
        if self.online and self.es_publico:
            id_comentario = Colaborador.contador2
            id_usuario = usuario1.get_id()
            id_articulo = input("Selecciona el articulo para comentar: ")
            contenido = input("Ingresa un comentario: ")
            comentario = Comentario(id_comentario, id_articulo, id_usuario, contenido)
            print("Gracias por dejar tu comentario.")
        else:
            cuenta_existente = input("¿Ya tienes una cuenta creada? (Si / No):")
            if cuenta_existente.upper() == "si" or cuenta_existente.upper() == "SI":
                return super().login()     
            elif cuenta_existente.upper() == "NO" or cuenta_existente.upper() == "no":
                return super().registrar()
            else:
                print("Opcion invalida.")

    def publicar(self):
        Colaborador.contador3 += 1
        if self.online and self.es_colaborador:
            id_publicacion = Colaborador.contador3
            id_usuario = usuario1.get_id()
            titulo = input("Ingresa un titulo para el articulo: ")
            resumen = input("Haz un breve resumen: ")
            contenido = input("Desarrolla tu articulo: ")
            articulo = Articulo(id_publicacion, id_usuario, titulo, resumen, contenido)
            print("Articulo creado correctamente.")
        else:
            print("No estas autorizado para publicar.")


class Articulo:
    def __init__(self, id, id_usuario, titulo, resumen, contenido):
        self.id = id
        self.id_usuario = id_usuario
        self.titulo = titulo
        self.resumen = resumen
        self.contenido = contenido
        self.fecha_publicacion = datetime.now()
        self.imagen = None
        self.estado = "Mi estado"

class Comentario():
    def __init__(self, id, id_articulo, id_usuario, contenido):
        self.id = id
        self.id_articulo = id_articulo
        self.id_usuario = id_usuario
        self.contenido = contenido
        self.fecha_hora = datetime.now()
        self.estado = "Mi estado"

    def __str__(self):
        return self.contenido

def menu():
    print("\n-- BIENVENIDO AL BLOG --")
    print("1. Registrarse")
    print("2. Iniciar Sesion")
    print("3. Comentar o publicar")
    print("4. Salir")

escolaborador = False
espublico = False
registrado = False
sesion_iniciada = False

while True:
    menu()
    opcion = input("Seleccione una opción (1-4): ")

    if opcion == '1':
        print("Que tipo de usuario eres?")
        print("1. Publico")
        print("2. Colaborador")
        tipo_usuario = input("Selecciona una opcion (1-2): ") 
        if tipo_usuario == '1':
            usuario1 = Publico("id", "nombre", "apellido", "telefono", "username", "email", "contra")
            usuario1.registrar()
            espublico = True
            escolaborador = False
            registrado = True
            sesion_iniciada = False
        elif tipo_usuario == '2':
            usuario1 = Colaborador("id", "nombre", "apellido", "telefono", "username", "email", "contra")
            usuario1.registrar()
            escolaborador = True
            espublico = False
            registrado = True
            sesion_iniciada = False
        else:
            print("Opcion invalida, volviendo al menu.")


    elif opcion == '2':
        if registrado:
            if sesion_iniciada == False:
                if usuario1.login():
                    sesion_iniciada = True
                else:
                    print("Error en inicio de sesion, volviendo al menu principal")
            else:
                print("Ya iniciaste sesion.")
        else:
            print("Debes registrarte primero.")


    elif opcion == '3':
        if sesion_iniciada == True:
            if escolaborador:
                print("¿Que deseas hacer?")
                print("1. Comentar")
                print("2. Publicar")
                opcion_colaborador = input("Selecciona una opcion (1-2): ")
                if opcion_colaborador == '1':
                    usuario1.comentar()
                elif opcion_colaborador == '2':
                    usuario1.publicar()
                else:
                    print("Opcion invalida.")
        
            elif espublico:
                print("¿Te gustaria comentar?")
                print("1. Si")
                print("2. No")
                opcion_publico = input("Selecciona una opcion (1-2): ")
                if opcion_publico == '1':
                    usuario1.comentar()
                else:
                    print("Volviendo al menu principal")
        else:
            print("Necesitas iniciar sesion para comentar o publicar")


    elif opcion == '4':
        print("Hasta luego!")
        break


    else:
        print("Opcion no valida, volviendo al inicio del menu")