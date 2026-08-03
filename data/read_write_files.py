import csv
import json

# write an filetxt
with open('dados.txt', 'w') as f:
    f.write('Olá mundo!')

# reading an file txt
with open('dados.txt', 'r') as file:
    conteudo = file.read()
    
print(conteudo)

# adding an information to file txt
with open('dados.txt', 'a') as f:
    f.write(f'\nultima linha')

with open('dados.csv', 'w') as f:
    escritor_csv = csv.writer(f)
    escritor_csv.writerow(['nome', 'idade'])
    escritor_csv.writerow(['Eduardo', 20])

with open('dados.csv', newline='') as f:
    leitor = csv.reader(f)
    for linha in leitor:
        print(linha)

dados = {'nome': 'Ana', 'idade': 32, 'enderecos':['a', 'b']}
with open('dados.json', 'w') as f:
    json.dump(dados, f)

with open('dados.json', 'r') as f:
    dados_lidos = json.load(f)
    print(dados_lidos)