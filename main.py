

class Asiento:
    
    def __init__(self, color, precio, registro) -> None:
        self.color = color
        self.precio = precio
        self.registro = registro

    def cambiarColor(self,nuevoColor):
        match nuevoColor:
            case "rojo"|"verde"|"amarillo"|"negro"|"blanco":
                self.color=nuevoColor

class Motor:
    
    def __init__(self, numeroCilindros, tipo, registro) -> None:
        self. registro = registro
        self. numeroCilindros = numeroCilindros
        self.tipo = tipo

    def cambiarRegistro(self, nuevoRegistro):
        self.registro=nuevoRegistro

    def asignarTipo(self, nuevoTipo):
        match nuevoTipo:
            case "gasolina"|"electrico":
                self.tipo = nuevoTipo
    
class Auto:

    def __init__(self, modelo, precio, asientos, marca, motor, registro) -> None:
        self.modelo = modelo
        self. precio = precio
        self. asientos = asientos
        self.marca = marca
        self. motor = motor
        self. registro = registro

    cantidad_creados = 0

    def cantidadAsientos(self):
        cantidad = 0
        for asiento in self.asientos:
            if asiento is Asiento:
                cantidad+=1
        return cantidad
    
    def verificarIntegridad(self):
        for asiento in self.asientos:
            if asiento is Asiento and asiento.registro!=self.registro:
                return "Las piezas no son originales"
        if self.motor.registro!=self.registro:
            return "Las piezas no son originales"
        
        return "Auto original"

