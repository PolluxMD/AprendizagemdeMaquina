import pandas as pd
import os
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

arquivo_csv = "dados_imc.csv"  # Ou o caminho absoluto, se necessário
if not os.path.exists(arquivo_csv):
    print(f"Erro: O arquivo {arquivo_csv} não foi encontrado.")
else:
    df = pd.read_csv(arquivo_csv)
    print("Arquivo carregado com sucesso!")

df = pd.read_csv(arquivo_csv)

#Dividindo os dados em conjunto de treinamento e teste
X = df[["IMC"]]  # Características (coluna IMC)
y = df["Obeso"]  # Rótulos (coluna Obeso)
X_treino, X_teste, y_treino, y_teste = train_test_split(X, y, test_size=0.2, random_state=42)

#Escolhendo e treinando modelo
modelo = LogisticRegression()
modelo.fit(X_treino, y_treino)

#Testar o modelo
predicoes = modelo.predict(X_teste)
print("Acurácia do modelo:", accuracy_score(y_teste, predicoes))

#Entrada dinâmica do usuário
while True:
    try:
        entrada_usuario = float(input("Insira o valor do IMC (ou digite -1 para Encerrar): "))
        if entrada_usuario == -1:  # Condição de saída
            print("Encerrando Teste...")
            break
        previsao = modelo.predict([[entrada_usuario]])  # Previsão com o valor do usuário
        if previsao[0] == 1:
            print(f"Para o IMC {entrada_usuario}, o modelo indica: Obeso")
        else:
            print(f"Para o IMC {entrada_usuario}, o modelo indica: Não Obeso")
    except ValueError:
        print("Por favor, insira um número válido!")
