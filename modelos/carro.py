# class Carro:
#     modelo = ""
#     cor = ""
#     ano = 0

# class Restaurante:
#     nome = ''
#     categoria = ''
#     ativo = ''
#     ano = 0
#     teste = ''

# r1 = Restaurante():
# r1.nome = 'A'
# r1.categoria = 'B'

class Restaurantes:
    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
    
    def __str__(self):
        return f"{self.nome} | {self.categoria}"
    
r1 = Restaurantes("Junior", "Teste")
# print(r1)

class Cliente:
    def __init__(self, nome, idade, numero, email):
        self.nome = nome
        self.idade = idade
        self.numero = numero
        self.email = email

    def __str__(self):
        return f"{self.nome} | {self.idade} | {self.numero} | {self.email}"
    
c1 = Cliente("Juninho", 18, 112321313, 'teste@gmail.com')
c2 = Cliente("Pedro", 23, 213123123412, 'teste2@gmail.com')
c3 = Cliente("Abu", 53, 5345345, 'teste3@gmail.com')

print(c1)
print(c2)
print(c3)