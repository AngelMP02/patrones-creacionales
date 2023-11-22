 # pizza_deliciosa_builder.py
from pizza_builder import PizzaBuilder
from pizza import Pizza

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
        if "Prosciutto" in self.pizza.ingredientes_principales:
            self.pizza.maridaje_recomendado = "Vino tinto"
        else:
            self.pizza.maridaje_recomendado = "Maridaje genérico"

    def get_pizza(self):
        return self.pizza
