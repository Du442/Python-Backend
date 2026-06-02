class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria):  
        self.nome = nome
        self.categoria = categoria
        self._ativo = False
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f"{self.nome} | {self.categoria} | {self.ativo}".ljust(50)
    
    def listar_restaurantes():
        for i in Restaurante.restaurantes:
            print(f'{i.nome.ljust(25)} | {i.categoria.ljust(25)} | {i.ativo.ljust(25)}')

    @property
    def ativo(self):
        return "☑" if self._ativo else "☐"

restaurante_praca = Restaurante("Praça", "Gourmet")
restaurante_pizza = Restaurante("Pizza", "Italiana")

Restaurante.listar_restaurantes()