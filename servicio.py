from abc import ABC, abstractmethod
from entities import EntidadBase

class Servicio(EntidadBase):
    def __init__(self, id_servicio, nombre, costo_base):
        super().__init__(id_servicio)
        self.nombre = nombre
        self.costo_base = costo_base

    @abstractmethod
    def calcular_costo(self, cantidad=1, **kwargs):
        pass

class ReservaSalas(Servicio):
    def calcular_costo(self, cantidad=1, descuento=0):
        # Polimorfismo: cálculo por horas
        return (self.costo_base * cantidad) - descuento

class AlquilerEquipos(Servicio):
    def calcular_costo(self, cantidad=1, seguro=True):
        # Polimorfismo: cargo fijo por seguro
        adicional = 15.0 if seguro else 0.0
        return (self.costo_base * cantidad) + adicional

class AsesoriaEspecializada(Servicio):
    def calcular_costo(self, cantidad=1, es_urgente=False):
        # Polimorfismo: recargo por urgencia
        factor = 1.5 if es_urgente else 1.0
        return (self.costo_base * cantidad) * factor
