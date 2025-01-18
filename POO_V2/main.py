from abc import ABC, abstractmethod

# Clase abstracta: Abstracción
class Animal(ABC):
    
    def __init__(self, nombre, edad):
        self._nombre = nombre  # Encapsulamiento: Atributo protegido
        self._edad = edad      # Encapsulamiento: Atributo protegido

    @abstractmethod
    def hacer_sonido(self):
        pass

    def describir(self):
        return f"{self._nombre} tiene {self._edad} años."

    # Getter y Setter para el nombre: Encapsulamiento
    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nuevo_nombre):
        if len(nuevo_nombre) > 0:
            self._nombre = nuevo_nombre
        else:
            raise ValueError("El nombre no puede estar vacío.")

    # Método concreto para todas las subclases
    def cumplir_años(self):
        self._edad += 1
        return f"{self._nombre} ahora tiene {self._edad} años."


# Clase concreta: Herencia de Animal
class Perro(Animal):
    def hacer_sonido(self):
        return "Guau"

    def mover_cola(self):
        return f"{self._nombre} está moviendo la cola de felicidad."


# Clase concreta: Herencia de Animal
class Gato(Animal):
    def hacer_sonido(self):
        return "Miau"

    def ronronear(self):
        return f"{self._nombre} está ronroneando felizmente."


# Clase concreta: Herencia de Animal
class Pato(Animal):
    def hacer_sonido(self):
        return "Cuac"

    def nadar(self):
        return f"{self._nombre} está nadando en el lago."


# Polimorfismo: Función que trabaja con cualquier Animal
def interactuar_con_animal(animal):
    print(animal.describir())
    print(f"Hace este sonido: {animal.hacer_sonido()}")


    # Polimorfismo: Llamado a métodos específicos según el tipo de Animal
    if isinstance(animal, Perro):
        print(animal.mover_cola())
    elif isinstance(animal, Gato):
        print(animal.ronronear())
    elif isinstance(animal, Pato):
        print(animal.nadar())


# Uso
perro = Perro("Max", 5)
gato = Gato("Luna", 3)
pato = Pato("Donald", 2)

animales = [perro, gato, pato]

# Iterar sobre los animales y usar polimorfismo
for animal in animales:
    interactuar_con_animal(animal)
    print(animal.cumplir_años())  # Encapsulamiento: Modificación controlada del atributo edad
    print("-" * 30)
