from sklearn.datasets import load_iris  # Para carregar os dados Iris
from sklearn.neighbors import KNeighborsClassifier  # Para o modelo KNN
from sklearn.model_selection import train_test_split  # Para dividir os dados
from sklearn.metrics import accuracy_score  # Para avaliar o modelo
from sklearn.datasets import load_iris

# Carregando os dados Iris
iris = load_iris()

X = iris.data  # Dados: comprimento e largura das pétalas e sépalas
y = iris.target  # Rótulos: 0 (setosa), 1 (versicolor), 2 (virginica)

# print("Tamanho de X:", X.shape)  # Exibe o tamanho do conjunto de dados
# print("Primeiros dados de X:", X[:5])  # Exibe as primeiras 5 linhas
# print("Tamanho de y:", y.shape)  # Exibe o tamanho do conjunto de rótulos
# print("Primeiros rótulos de y:", y[:5])  # Exibe os primeiros 5 rótulos

# Divisão dos dados (30% para teste, 70% para treino)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Verifique os tamanhos das divisões
# print("Tamanho do conjunto de treino:", X_train.shape)
# print("Tamanho do conjunto de teste:", X_test.shape)

knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train, y_train)

predictions = knn.predict(X_test)
# print("Predições:", predictions)  # Exibe as predições feitas pelo modelo

accuracy = accuracy_score(y_test, predictions)
# print("Acurácia do modelo:", accuracy)

# Solicitar entrada do usuário
print("\nInsira os valores para prever a espécie da flor:")
comprimento_sepala = float(input("Comprimento da sépala: "))
largura_sepala = float(input("Largura da sépala: "))
comprimento_petala = float(input("Comprimento da pétala: "))
largura_petala = float(input("Largura da pétala: "))

# Criar a entrada para predição
entrada_usuario = [[comprimento_sepala, largura_sepala, comprimento_petala, largura_petala]]

# Fazer a previsão
resultado = knn.predict(entrada_usuario)

# Exibir o nome da flor
print("A espécie da flor é:", iris.target_names[resultado[0]])