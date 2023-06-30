class Vehiculo:

    nombre = "vehiculo"

    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas

    def imprimir(self):
        print(f"este {self.nombre} es de color {self.color}, tiene ruedas {self.ruedas}", end="")

class Coche(Vehiculo):

    nombre = "coche"

    def __init__(self, color, ruedas, velocidad, cilindrada):
        super().__init__(color, ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def imprimir(self):
        super().imprimir()
        print(f" tiene una velodad de {self.velocidad} kilometros por hora y una cilindrada de {self.cilindrada} cc",end="")


class Camioneta(Coche):

    nombre = "camioneta"

    def __init__(self, color, ruedas, velocidad, cilindrada, carga):
        super().__init__(color, ruedas, velocidad, cilindrada)
        self.carga = carga

    def imprimir (self):
        super().imprimir()
        print (f" y soporta una carga de {self.carga} kilogramos",end="")

class Bicicleta(Vehiculo):

    nombre = "bicicleta"

    def __init__(self, color, ruedas, tipo):
        super().__init__(color, ruedas)
        self.tipo = tipo

    def imprimir (self):
        super().imprimir()
        print(f" es de tipo {self.tipo}",end="")

class Motocicleta(Bicicleta):

    nombre = "motocicleta"

    def __init__(self, color, ruedas, tipo, velocidad, cilindrada):
        super().__init__(color, ruedas, tipo)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def imprimir (self):
        super().imprimir()
        print(f" tiene una velocidad de {self.velocidad} kilometros por hora y una cilindrada de {self.cilindrada} cc.", end="")

vehiculo = Vehiculo ("Verde", 2)

coche = Coche ("amarillo", 4, 130, 45)

camioneta = Camioneta ("bordo", 2, 180, 70, 3000)

bicicleta = Bicicleta ("blanca", 4, "deportiva")

moto = Motocicleta("negra", 6, "urbana", 150, 85)


lista_vehiculos = [vehiculo, coche, camioneta, bicicleta, moto]

def catalogar(ruedas=None):
    filtrados = [objeto for objeto in lista_vehiculos if ruedas is None or objeto.ruedas == ruedas]

    if ruedas is not None:
        print (f"se han encontrado {len(filtrados)} vehiculos con {ruedas} ruedas:")
    else:
        print ("Lista completa de Vehiculos:")

    for objeto in filtrados:
        print ("Nombre:", objeto.nombre)
        catalogar = vars(objeto)
        for atributo, valor in catalogar.items():
            print (atributo + ":", valor)
        print()

catalogar()



