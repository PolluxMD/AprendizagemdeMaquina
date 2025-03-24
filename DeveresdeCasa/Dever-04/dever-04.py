import random
import pandas as pd

#Cria uma lista de frutas
frutas = ["maçã", "banana", "laranja", "uva", "maçã", "melão", "mamão", "banana"]

# Cria um conjunto de frutas e atribuir quantidades aleatórias
frutas_unicas = list(set(frutas))
quantidades = {fruta: random.randint(0, 100) for fruta in frutas_unicas}

# Grava no arquivo minhas_frutas.txt
with open("minhas_frutas.txt", "w") as arquivo:
    for fruta, quantidade in quantidades.items():
        arquivo.write(f"{fruta},{quantidade}\n")

# Lê o arquivo e soma as quantidades de frutas repetidas
data = {}
with open("minhas_frutas.txt", "r") as arquivo:
    for linha in arquivo:
        fruta, quantidade = linha.strip().split(",")
        quantidade = int(quantidade)
        if fruta in data:
            data[fruta] += quantidade
        else:
            data[fruta] = quantidade

# Cria um DataFrame e exibir no console
df = pd.DataFrame(list(data.items()), columns=["Fruta", "Quantidade"])
print(df)