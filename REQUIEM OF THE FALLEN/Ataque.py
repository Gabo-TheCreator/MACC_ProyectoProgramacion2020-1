class Ataque:
    dano: int = None
    costoDeMana: int = None
    nombre: str = None
    boost: int = None

    def __init__(self, dano, costoDeMana, nombre, boost):
        print("Creating an Attack")
        self.dano = dano
        self.costoDeMana = costoDeMana
        self.nombre = nombre
        self.boost = boost