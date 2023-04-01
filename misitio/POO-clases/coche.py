class Coche: 
 # Atributos o propiedades
    color = "Rojo"
    marca = "Ferrari"
    modelo="Aventador"
    velocidad = 300
    caballaje = 500
    plazas = 2
    
    def __init__(self, color, marca, velocidad):
        self.color = color
        self.marca = marca
        self.velocidad = velocidad      

    def acelerar(self):
        self.velocidad += 1

    def frenar(self):
        self.velocidad -= 1

    def getVelocidad(self):
        return self.velocidad

    # Getters y setters

    def setColor(self, color):
        self.color = color 

    def getColor(self):
        return self.color