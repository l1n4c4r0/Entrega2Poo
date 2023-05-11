
class Persona:
    def __init__(self, nombre, edad, profesion):
        self._nombre = nombre
        self.edad = edad
        self.profesion = profesion

    def saludar(self):
        print(f'Hola, mi nombre es {self._nombre}, tengo {self.edad} años.')

    def presentarse(self):
        print(f'Soy {self.profesion}')

    def get_nombre(self):
        return self._nombre
    def set_nombre(self,nombre):
        self._nombre = nombre
print()
humano1 = Persona('Stiven', 20, 'Chef')
humano1.saludar()
humano1.presentarse()
humano2 = Persona('Paula', 23, 'Traductora')
humano2.saludar()
humano2.presentarse()
print()
humano1.set_nombre('Apellido')
print(humano1.get_nombre())
humano2.set_nombre('Apellido')
print(humano2.get_nombre())
print()

#--------------------------------------------------------------------------
#Herencia

class Estudiante(Persona): 
    def __init__(self, nombre, edad, profesion, estudio, institucion):
        super().__init__(nombre, edad, profesion)
        self.estudio = estudio
        self.institucion = institucion 

    def presentarse(self):
        print(f'Actualmente estoy estudiando {self.estudio}, en la {self.institucion}')

humano3 = Estudiante('Daniel', 21,'estudiante', 'Especializacion en gastronimía Italiana','Academia Eat is live')
humano4 = Estudiante('Karol', 19, 'bailarina', 'Taller de pintura', 'Universidad de Artes')
humano3.saludar()
humano3.presentarse()
humano4.saludar()
humano4.presentarse()
