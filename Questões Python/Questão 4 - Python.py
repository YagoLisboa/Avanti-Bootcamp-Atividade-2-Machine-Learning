# 4. Dada uma lista de números inteiros, escreva uma função para encontrar o segundo maior valor na lista:

# 🐍 Solução 1 – Simples (usando sorted()):

def segundo_maior(lista):
    if len(lista) < 2:
        raise ValueError("A lista precisa ter pelo menos dois elementos!")
    
    lista_ordenada = sorted(set(lista))  # remove duplicatas
    if len(lista_ordenada) < 2:
        raise ValueError("Não há segundo maior valor distinto!")
    
    return lista_ordenada[-2]

numeros = [10, 5, 8, 20, 15]

print("O segundo maior número da lista é: ", segundo_maior(numeros))


# 🚀 Solução 2 – Otimizada mas sem ordenar:
# Aqui percorremos a lista apenas uma vez.

def segundo_maior_2(lista):
    if len(lista) < 2:
        raise ValueError("A lista precisa ter pelo menos dois elementos.")
    
    maior = segundo = float('-inf')
    
    for numero in lista:
        if numero > maior:
            segundo = maior
            maior = numero
        elif maior > numero > segundo:
            segundo = numero
    
    if segundo == float('-inf'):
        raise ValueError("Não há segundo maior valor distinto.")
    
    return segundo

numeros_2 = [10, 5, 8, 20, 15]

print("O segundo maior número da lista é: ", segundo_maior_2(numeros_2))
