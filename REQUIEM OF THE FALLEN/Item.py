class Item:
    vida: int = None
    mana: int = None
    boost: int = None
    nombre: str = None
    imagen: str = None

    def __init__(self, vida, mana, boost, nombre, imagen):
        print("Creating an Item")
        self.vida = vida
        self.mana = mana
        self.boost = boost
        self.nombre = nombre
        self.imagen = imagen