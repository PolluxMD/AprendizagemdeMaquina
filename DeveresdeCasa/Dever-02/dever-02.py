def validar_entrada():
    """Solicita ao usuário uma frase e verifica se não está vazia."""
    while True:
        frase = input("Digite uma frase: ").strip()
        if frase:
            return frase
        print("Entrada inválida! Digite uma frase válida.")


def analisar_frase(frase):
    """Realiza a análise da frase e retorna os resultados."""
    num_caracteres = len(frase)
    palavras = frase.split()
    num_palavras = len(palavras)
    maior_palavra = max(palavras, key=len) if palavras else ""
    frase_invertida_chars = frase[::-1]
    frase_invertida_palavras = " ".join(reversed(palavras))
    frase_maiuscula = frase.upper()
    frase_minuscula = frase.lower()
    tupla_palavras = tuple(palavras)

    return {
        "num_caracteres": num_caracteres,
        "num_palavras": num_palavras,
        "maior_palavra": maior_palavra,
        "frase_invertida_chars": frase_invertida_chars,
        "frase_invertida_palavras": frase_invertida_palavras,
        "frase_maiuscula": frase_maiuscula,
        "frase_minuscula": frase_minuscula,
        "tupla_palavras": tupla_palavras
    }


def exibir_resultados(resultados):
    """Exibe os resultados formatados."""
    print(f"Número de caracteres: {resultados['num_caracteres']}")
    print(f"Número de palavras: {resultados['num_palavras']}")
    print(f"Maior palavra: {resultados['maior_palavra']}")
    print(f"Frase invertida (por caracteres): {resultados['frase_invertida_chars']}")
    print(f"Frase invertida (por palavras): {resultados['frase_invertida_palavras']}")
    print(f"Frase em maiúsculas: {resultados['frase_maiuscula']}")
    print(f"Frase em minúsculas: {resultados['frase_minuscula']}")
    print(f"Tupla das palavras: {resultados['tupla_palavras']}")


# Execução do programa
frase_usuario = validar_entrada()
resultados = analisar_frase(frase_usuario)
exibir_resultados(resultados)
