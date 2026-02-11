# 3. Escreva uma função que receba duas listas e retorne outra lista com os elementos que estão presentes em apenas uma das listas:

# 🐍 Solução 1 – Usando apenas listas:
# Isso é conhecido como diferença simétrica.

def diferenca_simetrica(lista1, lista2):
    resultado = []
    
    for elemento in lista1:
        if elemento not in lista2:
            resultado.append(elemento)
    
    for elemento in lista2:
        if elemento not in lista1:
            resultado.append(elemento)
    
    return resultado

lista_a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista_b = [5, 6, 7, 8, 9, 10, 11, 12, 13]

resultado = diferenca_simetrica(lista_a, lista_b)

print("Os elementos que estão presentes em apenas uma das listas são: ", resultado)

# 🚀 Solução 2 – Usando conjuntos:
# Se a ordem não for importante e nós quisermos uma solução mais performática e que mantenha a ordem dos elementos da lista:

def diferenca_simetrica_ordenada(lista1, lista2):
    set_lista1 = set(lista1)
    set_lista2 = set(lista2)
    
    resultado = []
    
    # Elementos exclusivos da lista1
    for elemento in lista1:
        if elemento not in set_lista2:
            resultado.append(elemento)
    
    # Elementos exclusivos da lista2
    for elemento in lista2:
        if elemento not in set_lista1:
            resultado.append(elemento)
    
    return resultado


lista_a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista_b = [5, 6, 7, 8, 9, 10, 11, 12, 13]

resultado = diferenca_simetrica_ordenada(lista_a, lista_b)

print("Os elementos que estão presentes em apenas uma das listas são: ", resultado)

# Obs.: Essa versão:
## 1. Mantém a ordem original.
## 2. Mantém duplicatas exclusivas e é eficiente.
## 3. Não mantém duplicatas repetidas se estiverem nas duas listas (porque usamos set apenas para consulta).