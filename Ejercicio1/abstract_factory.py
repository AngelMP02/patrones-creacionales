from __future__ import annotations
from abc import ABC, abstractmethod
import pandas as pd

class AbstractFactory(ABC):
    @abstractmethod
    def create_moda(self) -> AbstractModa:
        pass

    @abstractmethod
    def create_media(self) -> AbstractMedia:
        pass

class ConcreteFactory_HoraSolicitud(AbstractFactory):
    def __init__(self, datos):
        self.datos = datos

    def create_moda(self) -> AbstractModa:
        return ConcreteModa_HoraSolicitud(self.datos)

    def create_media(self) -> AbstractMedia:
        return ConcreteMedia_HoraSolicitud(self.datos)

class ConcreteFactory_Mes(AbstractFactory):
    def __init__(self, datos):
        self.datos = datos

    def create_moda(self) -> AbstractModa:
        return ConcreteModa_Mes(self.datos)

    def create_media(self) -> AbstractMedia:
        return ConcreteMedia_Mes(self.datos)

class ConcreteFactory_HoraIntervencion(AbstractFactory):
    def __init__(self, datos):
        self.datos = datos

    def create_media(self) -> AbstractModa:
        return ConcreteModa_HoraIntervencion(self.datos)

    def create_moda(self) -> AbstractMedia:
        return ConcreteMedia_HoraIntervencion(self.datos)

class AbstractModa(ABC):
    @abstractmethod
    def calcular(self):
        pass

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
        return self.datos['Hora Intervención'].mode()

class AbstractMedia(ABC):
    @abstractmethod
    def calcular(self):
        pass

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
        return self.datos['Hora Intervención'].mean()

def client_code_mode(factory: AbstractFactory) -> None:
    moda = factory.create_moda()
    print(f'Moda: {moda.calcular()}')

def client_code_media(factory: AbstractFactory) -> None:
    media = factory.create_media()
    print(f'Media: {media.calcular()}')

if __name__ == "__main__":
    data = pd.read_csv('Ejercicio1/activaciones_samur_2022.csv', delimiter=";")
    data = data.dropna()

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

    factory_hora_solicitud = ConcreteFactory_HoraSolicitud(data)
    factory_hora_intervencion = ConcreteFactory_HoraIntervencion(data)
    factory_mes = ConcreteFactory_Mes(data)
    
    print("Hora de Solicitud:")
    client_code_mode(factory_hora_solicitud)
    client_code_media(factory_hora_solicitud)

    print("Mes:")
    client_code_mode(factory_mes)
    client_code_media(factory_mes)

    print("Hora Intervencion:")
    client_code_mode(factory_hora_intervencion)
    client_code_media(factory_hora_intervencion)