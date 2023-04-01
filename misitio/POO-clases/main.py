from coche import Coche

coche1 = Coche("Amarillo", "Renault", 20)
if type(coche1) == Coche:
    print("Es un objeto correcto !!")
    print(coche1.getColor())
else:
    print("No es un objeto!!")