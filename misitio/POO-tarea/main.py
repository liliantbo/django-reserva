from casa import Casa
from edificio import Edificio

mi_casa = Casa("Lilian", "Guayaquil", "Norte")
mi_casa.set_numero_habitaciones(3)
mi_casa.set_numero_habitantes(4)
mi_casa.set_area_construccion(110)
mi_casa.set_area_terreno(100)

mi_edificio = Edificio("Lilian", "Guayaquil", "Centro")
mi_edificio.set_total_pisos(5)
mi_edificio.set_posee_elevador("SI")
mi_edificio.set_area_construccion(600)
mi_edificio.set_area_terreno(230)

print(mi_casa.getInfo())
print ("Tipo de objeto " + str(type(mi_casa)))

print(mi_edificio.getInfo())
print ("Tipo de objeto " +str(type(mi_edificio)))
