#:::::::::::::::::::::::::::CLASS:::::::::::::::::::::::::::::::::::
class CuerposCelestes: 
    def __init__(self, planeta, posicion):
        self._planeta = planeta
        self._posicion = posicion

    def nombre(self):
        print(f'Este es el planeta {self._planeta}')
    def ubicacion(self):
        print(f'Su ubicación respecto al sol es la {self._posicion}')
    
    def get_nombre(self):
        return self._planeta
    def set_nombre(self,planeta):
        self._planeta = planeta

mercurio = CuerposCelestes('Mercurio', 'primera')
saturno = CuerposCelestes('Saturno', 'sexta')

mercurio.nombre()
mercurio.ubicacion()
saturno.nombre()
saturno.ubicacion()
print()
mercurio.set_nombre('Nombre')
print(mercurio.get_nombre())
saturno.set_nombre('Nombre')
print(saturno.get_nombre())
print()
#-----------------------Inheritance----------------------------------
class Datos(CuerposCelestes):
    def __init__(self, planeta, posicion, num_satelites):
        super().__init__(planeta, posicion)
        self._num_satelites = num_satelites
    def satelites(self):
        print(f'Tiene {self._num_satelites} satélites')

tierra = Datos('Tierra', 'tercera', 'Uno')
jupiter = Datos('Júpiter', 'quinta', 'Setenta y nueve')

tierra.nombre()
tierra.ubicacion()
tierra.satelites()
print()
jupiter.nombre()
jupiter.ubicacion()
jupiter.satelites()