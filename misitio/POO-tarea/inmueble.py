class Inmueble:
    _unidad_medida_area = "metros cuadrados"
    _area_construccion=0
    _area_terreno=0

    #constructor
    def __init__(self, propietario, ciudad, direccion,):
        self._propietario = propietario
        self._ciudad = ciudad
        self._direccion = direccion
          
    #setear atributos
    def set_propietario(self, propietario):
        self._propietario = propietario
    
    def set_ciudad(self, ciudad):
        self._ciudad = ciudad
    
    def set_direccion(self, direccion):
        self._direccion = direccion
    
    def set_unidad_medida_area(self, unidad_medida_area):
        self._unidad_medida_area=unidad_medida_area

    def set_area_construccion(self, area_construccion):
        self._area_construccion = area_construccion

    def set_area_terreno(self, area_terreno):
        self._area_terreno = area_terreno
       
    #obtener atributos

    def get_propietario(self):
        return self._propietario
    
    def get_ciudad(self):
        return self._ciudad
    
    def get_direccion(self):
        return self._direccion
    
    def get_area_construccion(self):
        return self._area_construccion
    
    def get_area_terreno(self):
        return self._area_terreno
    
    def get_unidad_medida_area(self):
        return self._unidad_medida_area