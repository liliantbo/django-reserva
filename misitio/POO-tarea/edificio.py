from inmueble import Inmueble

class Edificio(Inmueble):

    #constructor
    def __init__(self, propietario, ciudad, direccion):
        super().__init__(propietario, ciudad, direccion)
        self._posee_elevador="NO"
        self._total_pisos=0

    #seteo de atributos
    def set_total_pisos(self, total_pisos):
        self._total_pisos = total_pisos
    
    def set_posee_elevador(self, posee_elevador):
        self._posee_elevador = posee_elevador
    
    #obtener atributos

    def get_total_pisos(self):
        return self._total_pisos
    
    def get_posee_elevador(self):
        return self._posee_elevador
    
    def getInfo(self):
        info = "--------Información del Edificio--------"
        info += "\n Propietario: " + self.get_propietario()
        info += "\n Ciudad: " + self.get_ciudad()
        info += "\n Dirección: " + self.get_direccion()
        info += "\n Área de construcción: " + str(self.get_area_construccion()) + " "+ self.get_unidad_medida_area()
        info += "\n Área de terreno: " + str(self.get_area_terreno())+" "+ self.get_unidad_medida_area()
        info += "\n Pisos: " + str(self.get_total_pisos())
        info += "\n Posee elevador: " + self.get_posee_elevador()

        return info
    