# 1. Escreva uma função que receba uma lista de números e retorne outra lista com os números ímpares:

# 🐍 Solução 1 – Usando for:

def filtrar_impares(lista):
    impares = []
    
    for numero in lista:
        if numero % 2 != 0:
            impares.append(numero)
    
    return impares

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
resultado = filtrar_impares(numeros)

print("Os números ímpares na lista são: ", resultado)

# 🚀 Solução 2 – Usando List Comprehension:

def filtrar_impares_2(lista):
    return [numero for numero in lista if numero % 2 != 0]

numeros_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
resultado_2 = filtrar_impares_2(numeros_2)

print("Os números ímpares na lista 2 são: ", resultado_2)

# Essa versão faz exatamente a mesma coisa, mas de forma mais compacta.
## Obs.: A função não altera a lista original. Ela cria e retorna uma nova lista apenas com os valores ímpares.
### É possivel ainda realizar a atividade usando funções nativas como: lambda() e filter().