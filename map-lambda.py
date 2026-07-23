#test 1
precos = [1500.00, 320.50, 89.90, 4500.00]

lmb = map(lambda x: x*0.85, precos)
print(list(lmb))

#test 2
funcionarios = ["Carlos Souza", "Mariana Oliveira", "Pedro Almeida"]

lmb_func = map(lambda x: f'{x.lower().replace(' ', '.')}@hospitalrhn.com.br', funcionarios)

lista_func = list(lmb_func)
print(lista_func)

#test 3
logs_servidor = [
    "ERROR: Falha de comunicação com o banco",
    "INFO: Atualização do sistema concluída",
    "WARNING: Uso de CPU acima de 80%",
    "DEBUG: Conexão estabelecida na porta 8080"
]

print(list(map(lambda x: x.split(':')[0], logs_servidor)))
