from fastapi import FastAPI, Query
import requests

app = FastAPI()

@app.get('/api/hello')
def hello():
    '''
    Endpoint que exibe a clássica mensagem do mundo da programação.


    '''
    return {'message': 'Hello world!'}

@app.get('/api/restaurantes/')
def get_restaurantes(restaurante: str = Query(None)):

    '''
    Endpoint para visualizar todos os restaurantes e poder consultar cada um.

    '''

    url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'
    response = requests.get(url)
    print(response)

    if response.status_code == 200:
        dados_json = response.json()
        if restaurante is None:
            return {'Dados': dados_json}

        dados_restaurante = []
        for i in dados_json:
            if i['Company'] == restaurante:
                dados_restaurante.append({'item': i['Item'], 'price': i['price'], 'description': i['description']})
        return {'Restaurante': restaurante, 'Cardapio': dados_restaurante}

    else:
        return {'erro': f'{response.status_code} - {response.text}'}
