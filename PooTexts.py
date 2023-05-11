#tipo, estructura, caractetisticas y ejemplos
# ESTRUCTURA, PERIODISTICO, NARRATIVO, EXPOSITIVO
#::::::::::::::::::::::::::CLASS::::::::::::::::::::::::::
class Textos:
    def __init__(self, tipo, caracteristicas):
        self._tipo = tipo
        self._caracteristicas = caracteristicas

    def clasificacion(self):
        print(f'Este es un texto {self._tipo} ')
    def detalle(self):
        print(f'Sus principales caracteristicas son: {self._caracteristicas}')
    
    def get_tipo(self):
        return self._tipo
    def set_tipo(self,tipo):
        self._tipo = tipo

Tipo1 = Textos('Descriptivo', 'Texto que describe detalladamente cualquier cosa: objetos, paisajes, personas, situaciones, etc.')
Tipo2 = Textos('Argumetativo', 'Texto que busca la expresión de opiniones de forma argumentada. A menudo incluyen diferentes puntos de vista.')

Tipo1.clasificacion()
Tipo1.detalle()
Tipo2.clasificacion()
Tipo2.detalle()
print()
Tipo1.set_tipo('Categoría')
print(Tipo1.get_tipo())
Tipo2.set_tipo('Categoría')
print(Tipo2.get_tipo())
print()
#_______________________________Inheritance_____________________
class Casos(Textos):
    def __init__(self, tipo, caracteristicas, ejemplos):
        super().__init__(tipo, caracteristicas)
        self.ejemplos = ejemplos
    def generos(self):
        print(f'Dentro de estos podemos encontrar: {self.ejemplos}')

Tipo3 = Casos('Narrativo','Texto literario, normalmente escrito en prosa y que narra una historia.', 'Novela, Cuento, Leyenda, Fábula, Anécdota, Mito')

Tipo3.clasificacion()
Tipo3.detalle()
Tipo3.generos()
print()
#_______________________________Inheritance_____________________
class Orden(Textos):

    def __init__(self, tipo, caracteristicas, estructura):
        super().__init__(tipo, caracteristicas)
        self.estructura = estructura
    def detalle(self):
        print(f'La estructura común en este tipo de textos, es: {self.estructura}')

Tipo4 = Orden('Expositivo',	'Texto destinado a la exposición de ideas, conceptos o conocimiento.', 'Introducción, Desarrollo, Conclusión.')

Tipo4.clasificacion()
Tipo4.detalle()
