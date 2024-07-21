class Invento:
    
    innovador = True
    
    def __init__(self, nombre):
        self.nombre = nombre
    
    # Método de instancia: Pueden aceder y modificar atributos de un objeto, de la clase, y llamar a otros métodos de la misma
    def getDescription(self):
        print(f'Descripción del invento llamado {self.nombre}')
        
    # Método de clase: Pueden acceder a los atributos de clase, no de instancia de clase
    @classmethod
    def getClassDescriprtion(cls):
        print('Clase que describe un invento del concurso del Innovatec')
        print(f'Innovador {Invento.innovador}')
        
    # Métodos estáticos
    @staticmethod
    def sumar(a, b):
        return a+b



## HERENCIA
class Animal:
    
    def __init__(self, especie, edad):
        self.especie = especie
        self.edad = edad
    
    def nacer(self):
        print('Ya nací')

class Perro(Animal):
    
    __atributo_privado = 'ola'
    animal = 'perro'
    
    def __init__(self, especie, edad, raza):
        super().__init__(especie, edad)
        self.raza = raza
        
    def nacer(self):
        print(f'Ya nací, soy un {Perro.animal}')
    
    def ladrar():
        print('GUAUUUUU!!')
        
perro = Perro('canino', 10, 'Chihuahua')
print(perro.especie)
perro.nacer()
# print(Perro.__mro__) # Method order resolution