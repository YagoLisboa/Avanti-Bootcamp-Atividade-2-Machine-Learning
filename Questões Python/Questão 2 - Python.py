# 2. Escreva uma função que receba uma lista de números e retorne outra lista com os números primos presentes:

# 🐍 Solução 1 - Primeiro criamos uma função auxiliar para verificar se um número é primo:

def eh_primo(numero):
    if numero <= 1:
        return False
    
    for i in range(2, numero):
        if numero % i == 0:
            return False
    
    return True


def filtrar_primos(lista):
    primos = []
    
    for numero in lista:
        if eh_primo(numero):
            primos.append(numero)
    
    return primos

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
resultado = filtrar_primos(numeros)

print("Os números primos encontrados na lista são :", resultado)

# 🚀 Solução 2 – Versão Otimizada - Podemos melhorar a eficiência verificando divisores apenas até a raiz quadrada do número:

import math

def eh_primo_2(numero):
    if numero <= 1:
        return False
    
    for i in range(2, int(math.sqrt(numero)) + 1):
        if numero % i == 0:
            return False
    
    return True


def filtrar_primos_2(lista):
    return [numero for numero in lista if eh_primo_2(numero)]

numeros_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
resultado_2 = filtrar_primos_2(numeros_2)

print("Os números primos encontrados na lista são :", resultado_2)

# Esta solução é melhor porque reduzimos o número de verificações, tornando o algoritmo mais eficiente.
## Obs.: 1. Números negativos e 0/1 não são primos. 
## 2. A função retorna uma nova lista sem alterar a original.