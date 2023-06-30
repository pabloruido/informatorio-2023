# --- Grupo: Los discipulos de Adrian y Pablo
# -- Integrantes: 
# -- Aguirre Kremer	Matias Leandro
# -- Alfonso Braian Yamil
# -- Campo Arnoldo Agustín
# -- Haedo Enzo Gabriel
# -- Perez Elías Leonel
# -- Perez Julián
# -- Ruido Pablo Gabriel
# -- Diaz Barraza David Exequiel 
# -- Montiel Gustavo
# -- Lopez Lautaro


# Desafío 8: Principios de programación orientada a objetos

from datetime import datetime

# Crear las siguientes clases con sus atributos y métodos.
# Clase Usuario
#  atributos: id, nombre, apellido, teléfono, username, email, contraseña, fecha de
# registro, avatar, estado, online
#  métodos: login(), registrar()

class Usuario:
    contador = 0
    contadorcomentario = 0
    contadorpublicaciones = 0
    
    def __init__(self, id, nombre, apellido, telefono, username, email, contrasenia):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.username = username
        self.email = email
        self.contrasenia = contrasenia
        self.fecha_de_registro = datetime.now()
        self.avatar = None
        self.estado = None
        self.online = False


    def registrar (self):
        Usuario.contador += 1
        self.id = Usuario.contador
        self.nombre = input("ingrese su nombre: ")
        self.apellido = input("ingrese su apellido: ")
        self.telefono = input("ingrese su numero de telefono: ")
        self.username = input("elija su nombre de usuario: ")
        self.email = input("ingrese su email: ")
        self.contraseña = input("elija su contraseña: ")
        self.fecha_de_registro = datetime.now()

        print ("te has registrado exitosamente.")

    def login (self):
        username = input("por favor ingrese su nombre de usuario: ")
        contraseña = input("por favor ingrese su contraseña: ")

        if username == self.username and contraseña == self.contraseña:
            self.online = True
            print ("has iniciado sesión correctamente. ")
            return True
        else:
            print ("usuario o contraseña invalidos. ")
            return False

# Clase Publico(Usuario)
#  atributo: es_publico
#  métodos: registrar(), comentar()

class Publico(Usuario):
    
    def __init__(self, id, nombre, apellido, telefono, username, email, contraseña):
        super().__init__(id, nombre, apellido, telefono, username, email, contraseña)
        self.es_publico = True
       

    def comentar(self):
        Publico.contadorcomentario += 1
        if self.online and self.es_publico:
            id_comentario = Publico.contadorcomentario
            id_usuario = self.id
            id_articulo = input("en que articulo desea comentar?")
            contenido = input ("Ingrese su comentario: ")
            comentario = Comentario (id_comentario, id_usuario, id_articulo, contenido)
            print ("Gracias por su cmentario.")
        else:
            print ("debe iniciar sesión.")

# clase Colaborador(Usuario)
#  atributos: es_colaborador
#  métodos: registrar(), comentar(), publicar()

class Colaborador(Usuario):
    contadorpublicaciones = 0
    def __init__(self, id, nombre, apellido, telefono, username, email, contraseña):
        super().__init__(id, nombre, apellido, telefono, username, email, contraseña)
        self.es_colaborador = True
        self.es_publico = True

    def comentar(self):
        Colaborador.contadorcomentario += 1
        if self.online and self.es_colaborador:
            id_comentario = Colaborador.contadorcomentario
            id_usuario = self.id
            id_articulo = input("en que articulo desea comentar?")
            contenido = input ("Ingrese su comentario: ")
            comentario = Comentario (id_comentario, id_usuario, id_articulo, contenido)
            print ("gracias por su comentario")
        else:
            print ("debe iniciar sesión.")

    def publicar(self):
        Colaborador.contadorpublicaciones += 1
        if self.online and self.es_colaborador:
            id_articulo = Colaborador.contadorpublicaciones
            id_usuario = self.id
            titulo = input("Titulo del articulo: ")
            resumen = input("Ingrese un resumen: ")
            contenido = input("Contenido del articulo: ")
            ilustración = input("url de la foto o suba desde su dispositivo: ")
            fechapublicación = datetime.now()
            articulo = Articulo(id_articulo, id_usuario, titulo, resumen, contenido, ilustración, fechapublicación)
            self.id = True
            print ("articulo publicado.")
        else:
            print("inicie sesión en su cuenta.")

# clase Articulo
#  id, id_usuario, titulo, resumen, contenido, fecha_publicacion, imagen, estado

class Articulo:
    def __init__(self, id, id_usuario, titulo, resumen, contenido):
        self.id = id
        self.id_usuario = id_usuario
        self.titulo = titulo
        self.resumen = resumen
        self.contenido = contenido
        self.fecha_publicacion = datetime.now()
        self.imagen = None
        self.estado = None
        

# clase Comentario
#  id, id_articulo, id_usuario, contenido, fecha_hora, estado

class Comentario:
    def __init__(self, id, id_articulo, id_usuario, contenido):
        self.id = id
        self.id_articulo = id_articulo
        self.id_usuario = id_usuario
        self.contenido = contenido
        self.fecha_hora = datetime.now()
        self.estado = None

    def __str__(self):
            return self.contenido

# Código para elegir entre registrar usuarios o hacer login (si ya está registrado). Una vez registrado y
# logueado, código que permita comentar al Publico y además publicar al Colaborador.


def Menu():
    print ("BIENVENIDO AL MENU PRINCIPAL")
    print ("1 - Registrarse como usuario.")
    print ("2 - Hacer login.")
    print ("3 - Salir.")
    

logueado = False
registrado = False
escolaborador = False
espublico = False
    
while True:
    Menu()
       
    opcion = input("Seleccione la opción que deseé: ")

    if opcion == "1":
        print ("Te registraras como usuario Publico(1) o eres Colaborador(2)?")
        tipo_usuario = input("Selecciona según corresponda(1)o(2):")
        
        if tipo_usuario == "1":
            nuevo_user = Publico (None, None, None, None, None, None, None)
            nuevo_user.registrar()  
            espublico = True
            registrado = True

        elif tipo_usuario == "2":
            nuevo_user = Colaborador (None, None, None, None, None, None, None)
            nuevo_user.registrar() 
            escolaborador = True
            registrado = True
        else:
            print ("Opción invalida. Intente nuevamente.")
    
    elif opcion == "2":
        if registrado == True:
            if not logueado:
                if nuevo_user.login():
                    logueado = nuevo_user.online
                    if espublico:
                        print ("Desea comentar? Si (1) o  No (2)")
                        opciones_publico = input("Seleccione su opción: ")
                        if opciones_publico == "1":
                            nuevo_user.comentar()
                        else:
                            print ("Volviendo al menú.")
                    elif escolaborador:
                        print ("Que desea hacer? Comentar (1) o Publicar (2) ?")
                        opciones_colaborador = input ("Seleccione su opción: ")
                        if opciones_colaborador == "1":
                            nuevo_user.comentar()
                        elif opciones_colaborador == "2":   
                            nuevo_user.publicar()
                        else:
                            print ("Opcion invalida.")
            else: 
                logueado = nuevo_user.online
                if espublico:
                    print ("Desea comentar? Si (1) o  No (2)")
                    opciones_publico = input("Seleccione su opción: ")
                    if opciones_publico == "1":
                        nuevo_user.comentar()
                    else:
                        print ("Volviendo al menú.")
                elif escolaborador:
                    print ("Que desea hacer? Comentar (1) o Publicar (2) ?)")
                    opciones_colaborador = input ("Seleccione su opción: ")
                    if opciones_colaborador == "1":
                        nuevo_user.comentar()
                    elif opciones_colaborador == "2":   
                        nuevo_user.publicar()
                    else:
                        print ("Opcion invalida.") 
        else: 
            print("Proceda a registrarse en el menú principal.")
    elif opcion == "3":
        print ("Vuelva pronto!")
        break 
    else:
        print ("opción invalida.")

# Menu()

 

