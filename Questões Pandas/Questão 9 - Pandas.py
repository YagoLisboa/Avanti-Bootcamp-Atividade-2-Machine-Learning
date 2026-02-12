# 9. Utilizando pandas, como selecionar uma coluna específica e filtrar linhas em um “DataFrame” com base em uma condição?

# 📌 Como selecionar uma coluna e filtrar linhas com base em uma condição no pandas. Em pandas, usamos:
# 🔹 df['coluna'] → Para selecionar uma coluna.
# 🔹 Condições booleanas → Para filtrar linhas.
# 🔹 df.loc[] → Para selecionar linhas e colunas ao mesmo tempo.

# 🧱 1️⃣ Criando um DataFrame de exemplo
import pandas as pd

df = pd.DataFrame({
    'Nome': ['Ana', 'Bruno', 'Carlos', 'Diana'],
    'Idade': [23, 35, 29, 42],
    'Salario': [3000, 5000, 4000, 7000]
})

print(df)

# 🎯 2️⃣ Selecionando uma coluna específica
print(df['Salario'])

# Ou salvando em uma variável:
salarios = df['Salario']

# 🔎 3️⃣ Filtrando linhas com base em uma condição:
# ✅ Exemplo: pessoas com salário maior que 4000
filtro = df[df['Salario'] > 4000]

print(filtro)

# 🧩 4️⃣ Filtrando com múltiplas condições
# 🔹 Usando AND (&)
# Exemplo: salário > 4000 e idade > 30
df_filtrado = df[(df['Salario'] > 4000) & (df['Idade'] > 30)]
print(df_filtrado)
# ⚠ Sempre use parênteses nas condições.

# 🔹 Usando OR (|)
# Exemplo: idade < 25 ou salário > 6000
df_filtrado = df[(df['Idade'] < 25) | (df['Salario'] > 6000)]
print(df_filtrado)

# 🧱 5️⃣ Selecionando coluna + filtro ao mesmo tempo
# ✅ Exemplo: mostrar apenas o nome de quem ganha mais de 4000
resultado = df.loc[df['Salario'] > 4000, 'Nome']
print(resultado)
# 📌 Aqui estamos dizendo:
# df.loc[condição_linhas, coluna_desejada]

# 📌 6️⃣ Selecionando múltiplas colunas com filtro
df.loc[df['Salario'] > 4000, ['Nome', 'Salario']]

# 🚀 Resumo
# | Operação            | Sintaxe                      |        |
# | ------------------- | ---------------------------- | ------ |
# | Selecionar coluna   | `df['coluna']`               |        |
# | Filtrar linhas      | `df[df['coluna'] condição]`  |        |
# | Múltiplas condições | `&` (AND) / `                | ` (OR) |
# | Linha + coluna      | `df.loc[condição, 'coluna']` |        |

# 🎯 Exemplo Final Completo:
import pandas as pd

df = pd.DataFrame({
    'Nome': ['Ana', 'Bruno', 'Carlos', 'Diana'],
    'Idade': [23, 35, 29, 42],
    'Salario': [3000, 5000, 4000, 7000]
})

# Filtrar pessoas com salário maior que 4000
resultado = df.loc[df['Salario'] > 4000, ['Nome', 'Salario']]

print(resultado)

# 💡 Conclusão
# Para selecionar uma coluna e filtrar linhas:
### df.loc[df['coluna'] condição, 'coluna_desejada']
# Esta forma é simples, poderoso e essencial para análise de dados e machine learning!