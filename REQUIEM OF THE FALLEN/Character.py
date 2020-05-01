from Item import Item
from Ataque import Ataque
from enum import Enum

class Character:
    vida: int = None
    mana: int = None
    boost: int = None
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