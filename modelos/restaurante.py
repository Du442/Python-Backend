class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria):  
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f"{self.nome} | {self.categoria} | {self.ativo}".ljust(50)
    
    @classmethod
    def listar_restaurantes(cls):
        for i in cls.restaurantes:
            print(f'{i._nome.ljust(25)} | {i._categoria.ljust(25)} | {i.ativo.ljust(25)}')

    @property
    def ativo(self):
        return "☑" if self._ativo else "☐"

    def alternar_estado(self):
        self._ativo = not self._ativo

restaurante_praca = Restaurante("Praça", "Gourmet")
restaurante_pizza = Restaurante("Pizza", "Italiana")

Restaurante.listar_restaurantes()