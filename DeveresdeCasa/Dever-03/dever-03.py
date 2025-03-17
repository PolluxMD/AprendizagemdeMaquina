import csv

# Define os dados
dados = [
    ["Nome", "Idade"],
    ["Ana", 25],
    ["Bruno", 30],
    ["Carla", 22],
    ["Daniel", 28],
    ["Eduardo", 35]
]

# Cria e escreve no arquivo CSV
with open("dados.csv", mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerows(dados)

print("Arquivo 'dados.csv' criado com sucesso!")

# Lê o arquivo CSV e armazena os dados em uma lista
dados_lidos = []
with open("dados.csv", mode="r", newline="", encoding="utf-8") as file:
    reader = csv.reader(file)
    next(reader)  # Pula o cabeçalho
    for row in reader:
        row[1] = int(row[1])  # Converte a idade para inteiro
        dados_lidos.append(row)

# Pede ao usuário para digitar um nome
nome_procurado = input("Digite um nome: ")

# Verifica se o nome está na lista
encontrado = False
idades = [pessoa[1] for pessoa in dados_lidos]
maior_idade = max(idades)

for pessoa in dados_lidos:
    if pessoa[0].lower() == nome_procurado.lower():
        encontrado = True
        idade = pessoa[1]
        print(f"{nome_procurado} tem {idade} anos.")
        if idade == maior_idade:
            print(f"{nome_procurado} é a pessoa mais velha da lista.")
        else:
            print(f"{nome_procurado} não é a pessoa mais velha da lista.")
        break

if not encontrado:
    print("Nome não encontrado.")