

class Animales:
    def __init__(self, nombre, especie, alimentacion  ):

        self._nombre = nombre
        self._especie = especie
        self._alimentacion = alimentacion

    def info(self):
        print(f'Este es el/la {self._nombre}.')
    
    def clasificacion(self):
        print(f'Es {self._especie} y su clasificación alimenticia es {self._alimentacion} ')

    def get_nombre(self):
        return self._nombre
    def set_nombre(self,nombre):
        self._nombre = nombre
animal1 = Animales('Oveja', 'mamifero', 'herbivoro')
animal2 = Animales('Gallina', 'ave', 'omnivoro')

animal1.info()
animal1.clasificacion()
animal2.info()
animal2.clasificacion()
print()
animal1.set_nombre('Grupo')
print(animal1.get_nombre())
animal2.set_nombre('Grupo')
print(animal2.get_nombre())
print()
#--------------------------------------------------------------------------
#Herencia
class Adicional(Animales):
    def __init__(self, nombre, especie, alimentacion, edad, peso  ):
        super().__init__(nombre, especie, alimentacion)
        self._edad = edad
        self._peso = peso
    def caracteristias(self):
        print(f'Su edad aproximada de vida es {self._edad} años y su peso aproximado es {self._peso}')

Ganado = Adicional('Vaca', 'mamifero', 'herbivoro', 12, '720 kg')
Ave = Adicional('Loro', 'ave', 'omnivoro', 35, '480 g' )

Ganado.info()
Ganado.clasificacion()
Ganado.caracteristias()
print('_____________________________________________________________')
Ave.info()
Ave.clasificacion()
Ave.caracteristias()

