from Item import Item
from Ataque import Ataque
from enum import Enum

class Character:
    vida: int = None
    mana: int = None
    boost: float = None
    nombre: str = None
    items = None  # [Item]
    ataques = None  # [Ataque]
    tipo = None  # Character(Enum)

    def __init__(self, vida, mana, boost, nombre, items, ataques, tipo):
        print("Creating character")
        self.vida = vida
        self.mana = mana
        self.boost = boost
        self.nombre = nombre
        self.items = items
        self.ataques = ataques
        self.tipo = tipo

    def getHealth(self):
        return self.vida

    def getMana(self):
        return self.mana

    def getName(self):
        return self.nombre

    def getBoost(self):
        return self.boost

    def getItems(self):
        return self.items

    def getAttacks(self):
        return self.ataques

    def getType(self):
        return self.tipo
#Definición de los argumentos de los personajes