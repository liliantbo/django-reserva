from inmueble import Inmueble

class Casa(Inmueble):
    
    #constructor
    def __init__(self, propietario, ciudad, direccion):
        super().__init__(propietario, ciudad, direccion)
        self._numero_habitaciones=0
        self._numero_habitantes=0
    #seteo de atributos
    def set_numero_habitaciones(self, numero_habitaciones):
        self._numero_habitaciones = numero_habitaciones
    
    def set_numero_habitantes(self, numero_habitantes):
        self._numero_habitantes = numero_habitantes
    
    #obtener atributos

    def get_numero_habitaciones(self):
        return self._numero_habitaciones
    
    def get_numero_habitantes(self):
        return self._numero_habitantes
    
    def getInfo(self):
        info = "--------Información de la Casa--------"
        info += "\n Propietario: " + self.get_propietario()
        info += "\n Ciudad: " + self.get_ciudad()
        info += "\n Dirección: " + self.get_direccion()
        info += "\n Área de construcción: " + str(self.get_area_construccion()) + " " + self.get_unidad_medida_area()
        info += "\n Área de terreno: " + str(self.get_area_terreno()) + " " +self.get_unidad_medida_area()
        info += "\n Número de habitaciones: " + str(self.get_numero_habitaciones())
        info += "\n Número de habitantes: " + str(self.get_numero_habitantes())

        return info
    