import csv
from datetime import datetime

# Criando e escrevendo no arquivo CSV
dados = [
    ["Nome", "DataNasc", "DataCadastrado", "HoraCadastro"],
    ["Pablo Coelho", "01/26/1974", "2025/02/17", "20:30"],
    ["Mariana Ferreira", "04/26/1995", "2025/02/17", "20:31"],
    ["Carlos Lima", "11/15/1988", "2025/02/17", "20:32"],
    ["Ana Souza", "07/08/2000", "2025/02/17", "20:33"],
    ["Roberto Silva", "05/30/1980", "2025/02/17", "20:34"]
]

with open("dados_dever_01.csv", mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerows(dados)

print("Arquivo 'dados_dever_01.csv' criado com sucesso!")

# Lendo o arquivo CSV
dados_lidos = []
with open("dados_dever_01.csv", mode="r", newline="", encoding="utf-8") as file:
    reader = csv.reader(file)
    next(reader)  # Pula o cabeçalho
    for row in reader:
        dados_lidos.append(row)

# Solicitando ao usuário um número de registro
try:
    registro = int(input("Digite o número do registro (1 a 5): "))
    if 1 <= registro <= len(dados_lidos):
        nome, data_nasc, data_cad, hora_cad = dados_lidos[registro - 1]
        
        # Convertendo as datas para o formato brasileiro
        data_nasc_br = datetime.strptime(data_nasc, "%m/%d/%Y").strftime("%d/%m/%Y")
        data_cad_br = datetime.strptime(data_cad, "%Y/%m/%d").strftime("%d/%m/%Y")
        
        print(f"Registro {registro}: Nome: {nome}; Data de nascimento: {data_nasc_br}; Data de cadastro: {data_cad_br} às {hora_cad} horas")
    else:
        print("Número de registro inválido! Deve estar entre 1 e 5.")
except ValueError:
    print("Entrada inválida! Digite um número inteiro entre 1 e 5.")
