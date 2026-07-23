from cmd import PROMPT


def simula_api(**kwargs):
    pass

def somar_numeros(*args):
    total = 0
    if len(args) == 0:
        return 0
    for n in args:
        total += n
    return total

def buscar_produtos(categoria, **kwargs):
    print(categoria)
    for i in kwargs.values():
        print(i)

def gerar_log(nivel, *args, **kwargs):
    print(nivel)
    for i in args:
        print(i)
    for t, v in kwargs.items():
        print(f'{t}={v}')

def _chamada_ficticia_api(prompt, model='gpt-3.5-turbo', temperature=0.7, **kwargs):
    """
    Simula o envio de uma requisição para um serviço de LLM.
    Monta e retorna o payload com todas as configurações consolidadas.
    """
    payload = {
        "prompt": prompt,
        "model": model,
        "temperature": temperature,
        "outras_configuracoes": kwargs
    }
    return payload

def gerar_resposta_ia(prompt, **kwargs):
    """
    Recebe o prompt obrigatório e repassa todas as configurações extras (kwargs)
    diretamente para a função de chamada da API.
    """
    print(f"-> Enviando prompt: '{prompt}'")
    
    # Aqui ocorre a mágica: desempacotamos o dicionário 'kwargs'
    # usando '**' na chamada da função destino
    resposta = _chamada_ficticia_api(prompt, **kwargs)
    
    return resposta

# resultado1 = gerar_resposta_ia("O que é Python?")
# print("Resultado 1:\n", resultado1)
# print("-" * 40)


# print(somar_numeros(10,20,30))
# print(somar_numeros(5))
# print(somar_numeros())

# buscar_produtos('Eletronicos', preco_max=1500, em_estoque=True, marca='Dell')

# print(gerar_log(
#     "ERROR", 
#     "Falha ao conectar no banco de dados.", 
#     "Tentativa 3 de 3 falhou.",
#     usuario="admin",
#     ip="192.168.1.100",
#     banco="mysql_prod"
# ))

