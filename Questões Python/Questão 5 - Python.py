# 5. Crie uma função que receba uma lista de tuplas, cada uma contendo o nome e a idade de uma pessoa,
# e retorne a lista ordenada pelo nome das pessoas em ordem alfabética.

# 🐍 Solução Simples e Eficiente:

def ordenar_por_nome(lista):
    return sorted(lista, key=lambda pessoa: pessoa[0])

pessoas = [
    ("Carlos", 30),
    ("Ana", 25),
    ("Bruno", 22),
    ("Daniela", 28)
]

resultado = ordenar_por_nome(pessoas)

print("A lista ordenada pelo nome das pessoas em ordem alfabética é: ", resultado)

# 🚀 Solução 2 - Versão Alternativa (modificando a própria lista) ordenando a própria lista, sem criar outra:

def ordenar_por_nome_2(lista):
    lista.sort(key=lambda pessoa: pessoa[0].lower())
    return lista

pessoas_2 = [
    ("Carlos", 30),
    ("Ana", 25),
    ("Bruno", 22),
    ("Daniela", 28)
]

resultado_2 = ordenar_por_nome_2(pessoas_2)

print("A lista ordenada pelo nome das pessoas em ordem alfabética é: ", resultado_2)

# 🐍 Solução 3 - Versão ALternativa - Ordenando pela idade em ordem crescente:

def ordenar_por_idade(lista):
    return sorted(lista, key=lambda pessoa: pessoa[1])

pessoas_3 = [
    ("Carlos", 30),
    ("Ana", 25),
    ("Bruno", 22),
    ("Daniela", 28)
]

resultado = ordenar_por_idade(pessoas_3)

print("A lista ordenada pela idade das pessoas em ordem crescente é: ", resultado)