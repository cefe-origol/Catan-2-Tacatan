class Asentamiento:
    def __init__(self, jugador):
        self.jugador = jugador

class Ciudad:
    pass

class Camino:
    def __init__(self, jugador):
        self.jugador = jugador

class Jugador:
    def __init__(self, nombre, color):
        self.nombre = nombre
        self.color = color
        self.madera = 0
        self.ladrillo = 0
        self.lana = 0
        self.trigo = 0
        self.piedra = 0

    def cantidad_de(self, recurso):
        if recurso == "Madera":
            return self.madera
        elif recurso == "Ladrillo":
            return self.ladrillo
        elif recurso == "Lana":
            return self.lana
        elif recurso == "Trigo":
            return self.trigo
        elif recurso == "Piedra":
            return self.piedra

    def AgregarRecurso(self, recurso, cantidad):
        if recurso == "Madera":
            self.madera += cantidad
        elif recurso == "Ladrillo":
            self.ladrillo += cantidad
        elif recurso == "Lana":
            self.lana += cantidad
        elif recurso == "Trigo":
            self.trigo += cantidad
        elif recurso == "Piedra":
            self.piedra += cantidad