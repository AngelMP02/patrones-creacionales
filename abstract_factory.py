from __future__ import annotations
from abc import ABC, abstractmethod
import pandas as pd


class AbstractFactory(ABC):
    """
    The Abstract Factory interface declares a set of methods that return
    different abstract products. These products are called a family and are
    related by a high-level theme or concept. Products of one family are usually
    able to collaborate among themselves. A family of products may have several
    variants, but the products of one variant are incompatible with products of
    another.
    """
    @abstractmethod
    def create_product_a(self) -> AbstractModa:
        pass

    @abstractmethod
    def create_product_b(self) -> AbstractMedia:
        pass


class ConcreteFactory_HoraSolicitud(AbstractFactory):
   
        

    def create_product_a(self) -> AbstractModa:
        return ConcreteModa_HoraSolicitud(self.datos)

    def create_product_b(self) -> AbstractMedia:
        return ConcreteMedia_HoraSolicitud(self.datos)


class ConcreteFactory_Mes(AbstractFactory):
    """
    Each Concrete Factory has a corresponding product variant.
    """

    def create_product_a(self) -> AbstractModa:
        return ConcreteModa_Mes(self.datos)

    def create_product_b(self) -> AbstractMedia:
        return ConcreteMedia_Mes(self.datos)

class ConcreteFactory_HoraIntervencion(AbstractFactory):
  

    def create_product_a(self) -> AbstractModa:
        return ConcreteModa_HoraIntervencion(self.datos)

    def create_product_b(self) -> AbstractMedia:
        return ConcreteMedia_HoraIntervencion(self.datos)


class AbstractModa(ABC):
    @abstractmethod
    def calcular(self):
        pass


"""
Concrete Products are created by corresponding Concrete Factories.
"""


class ConcreteModa_HoraSolicitud(AbstractModa):
    def __init__(self, datos):
            self.datos = datos
    def calcular(self):
        return self.datos['Hora Solicitud'].mode()


class ConcreteModa_Mes(AbstractModa):
    def __init__(self, datos):
            self.datos = datos
    def calcular(self):
        return self.datos['Mes'].mode()
class ConcreteModa_HoraIntervencion(AbstractModa):
    def __init__(self, datos):
            self.datos = datos
    def calcular(self):
        return self.datos['Hora Intervencion'].mode()


class AbstractMedia(ABC):
    """
    Here's the the base interface of another product. All products can interact
    with each other, but proper interaction is possible only between products of
    the same concrete variant.
    """
    @abstractmethod
    def calcular(self):
        pass


"""
Concrete Products are created by corresponding Concrete Factories.
"""


class ConcreteMedia_HoraSolicitud(AbstractMedia):
    
    def __init__(self, datos):
            self.datos = datos
    def calcular(self):
        return self.datos['Hora Solicitud'].mean()

    


class ConcreteMedia_Mes(AbstractMedia):
    def __init__(self, datos):
            self.datos = datos
    def calcular(self):
        return self.datos['Mes'].mean()

class ConcreteMedia_HoraIntervencion(AbstractMedia):
    def __init__(self, datos):
            self.datos = datos
    def calcular(self):
        return self.datos['Hora Intervencion'].mode()

def client_code_mode(factory: AbstractFactory) -> None:
    """
    The client code works with factories and products only through abstract
    types: AbstractFactory and AbstractProduct. This lets you pass any factory
    or product subclass to the client code without breaking it.
    """
    product_a = factory.create_product_a()
    product_b = factory.create_product_b()

    print(f"{product_b.useful_function_b()}")
    print(f"{product_b.another_useful_function_b(product_a)}", end="")


def client_code_media(factory: AbstractFactory) -> None:
    """
    The client code works with factories and products only through abstract
    types: AbstractFactory and AbstractProduct. This lets you pass any factory
    or product subclass to the client code without breaking it.
    """
    product_a = factory.create_product_a()
    product_b = factory.create_product_b()

    print(f"{product_b.useful_function_b()}")
    print(f"{product_b.another_useful_function_b(product_a)}", end="")


if __name__ == "__main__":
    
data = pd.read_csv('Ejercicio1/activaciones_samur_2022.csv', delimiter = ";")

print(data.info()) 
print(data.describe())  
print(data.head()) 

#elimino los valores nulos para que no me de error al procesar lso datos
data = data.dropna()

#compruebo que no hay valores nulos en el dataset
nulos = data.isna().sum()
print(nulos)
print(data.columns)
meses_a_numeros = {
    'ENERO': 1,
    'FEBRERO': 2,
    'MARZO': 3,
    'ABRIL': 4,
    'MAYO': 5,
    'JUNIO': 6,
    'JULIO': 7,
    'AGOSTO': 8,
    'SEPTIEMBRE': 9,
    'OCTUBRE': 10,
    'NOVIEMBRE': 11,
    'DICIEMBRE': 12
}

data['Mes'] = data['Mes'].map(meses_a_numeros)

data['Hora Solicitud'] = pd.to_datetime(data['Hora Solicitud'], format='%H:%M:%S')
data['Hora Solicitud'] = (data['Hora Solicitud'].dt.hour * 60 + data['Hora Solicitud'].dt.minute + data['Hora Solicitud'].dt.second / 60).round().astype('int64')

data['Hora Intervención'] = pd.to_datetime(data['Hora Intervención'], format='%H:%M:%S')
data['Hora Intervención'] = (data['Hora Intervención'].dt.hour * 60 + data['Hora Intervención'].dt.minute + data['Hora Intervención'].dt.second / 60).round().astype('int64')

data.drop('Año', axis=1, inplace=True)

data_limpio = data.copy()