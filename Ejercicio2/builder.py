from abc import ABC, abstractmethod

# Interfaz PizzaBuilder
class PizzaBuilder(ABC):
    @abstractmethod
    def build_tipo_masa(self):
        pass

    @abstractmethod
    def build_salsa(self):
        pass

    @abstractmethod
    def build_ingredientes_principales(self):
        pass

    @abstractmethod
    def build_tecnicas_coccion(self):
        pass

    @abstractmethod
    def build_presentacion(self):
        pass

    @abstractmethod
    def build_maridaje_recomendado(self):
        pass

    @abstractmethod
    def get_pizza(self):
        pass

# Implementación concreta de PizzaBuilder
class PizzaDeliziosoBuilder(PizzaBuilder):
    def __init__(self):
        self.pizza = Pizza()

    def build_tipo_masa(self):
        self.pizza.tipo_masa = "Masa delgada premium"

    def build_salsa(self):
        self.pizza.salsa = "Salsa de autor"

    def build_ingredientes_principales(self):
        self.pizza.ingredientes_principales = ["Tomate", "Mozzarella", "Prosciutto"]

    def build_tecnicas_coccion(self):
        self.pizza.tecnicas_coccion = "Horno tradicional"

    def build_presentacion(self):
        self.pizza.presentacion = "Estilo clásico"

    def build_maridaje_recomendado(self):
        self.pizza.maridaje_recomendado = "Vino tinto"

    def get_pizza(self):
        return self.pizza

# Clase para representar la pizza
class Pizza:
    def __init__(self):
        self.tipo_masa = ""
        self.salsa = ""
        self.ingredientes_principales = []
        self.tecnicas_coccion = ""
        self.presentacion = ""
        self.maridaje_recomendado = ""

# Director para guiar la construcción de la pizza
class DirectorPizza:
    def __init__(self, builder):
        self.builder = builder

    def construir_pizza(self):
        self.builder.build_tipo_masa()
        self.builder.build_salsa()
        self.builder.build_ingredientes_principales()
        self.builder.build_tecnicas_coccion()
        self.builder.build_presentacion()
        self.builder.build_maridaje_recomendado()

# Uso del patrón Builder
builder_delizioso = PizzaDeliziosoBuilder()
director = DirectorPizza(builder_delizioso)
director.construir_pizza()
pizza_personalizada = builder_delizioso.get_pizza()

# Imprime los detalles de la pizza personalizada
print("Detalles de la pizza personalizada:")
print(f"Tipo de masa: {pizza_personalizada.tipo_masa}")
print(f"Salsa: {pizza_personalizada.salsa}")
print(f"Ingredientes principales: {', '.join(pizza_personalizada.ingredientes_principales)}")
print(f"Técnicas de cocción: {pizza_personalizada.tecnicas_coccion}")
print(f"Presentación: {pizza_personalizada.presentacion}")
print(f"Maridaje recomendado: {pizza_personalizada.maridaje_recomendado}")
