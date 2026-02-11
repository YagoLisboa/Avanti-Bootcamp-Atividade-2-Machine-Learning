# 7. Como concatenar vários DataFrames (empilhando linhas ou colunas), mesmo que tenham colunas diferentes?
# Dica: Utiliza-se pd.concat() especificando axis=0 (linhas) ou axis=1 (colunas).
# Quando há colunas diferentes, os valores ausentes são preenchidos com NaN.

# 📌 Como concatenar vários DataFrames com pd.concat()
# A função pd.concat() é utilizada para unir dois ou mais DataFrames:
# 🔹 Empilhando linhas → axis=0
# 🔹 Unindo colunas → axis=1
# Quando os DataFrames possuem colunas diferentes, o pandas automaticamente preenche os valores ausentes com NaN.

# 🧱 1️⃣ Concatenando DataFrames por Linhas (axis=0)
# 📌 Situação:
# Queremos empilhar os dados, como se estivéssemos adicionando novos registros.

import pandas as pd

# Primeiro DataFrame
df1 = pd.DataFrame({
    'Nome': ['Ana', 'Bruno'],
    'Idade': [23, 35]
})

# Segundo DataFrame (tem coluna diferente)
df2 = pd.DataFrame({
    'Nome': ['Carlos', 'Diana'],
    'Salario': [3000, 4000]
})

# Concatenando por linhas
df_linhas = pd.concat([df1, df2], axis=0)

print(df_linhas)

# ✔ As colunas são unificadas
# ✔ Onde não há valor correspondente → NaN

# 🔹 Ignorando o índice original:
df_linhas = pd.concat([df1, df2], axis=0, ignore_index=True)
# (Isso reorganiza o índice automaticamente.)

# ------------------------------------------------------------

# 🧩 2️⃣ Concatenando DataFrames por Colunas (axis=1)
# 📌 Situação:
# Queremos juntar informações lado a lado.

df_colunas = pd.concat([df1, df2], axis=1)

print(df_colunas)
# ⚠ O pandas alinha os dados pelo índice.
# Se os índices forem diferentes, ele também preencherá com NaN.

# ---------------------------------------------------------------

# 🎯 3️⃣ Controlando a Interseção ou União das Colunas:
# O parâmetro join controla isso:
# 'outer' (padrão) → União das colunas.
# 'inner' → Apenas colunas em comum.

df_inner = pd.concat([df1, df2], axis=0, join='inner')
print(df_inner)
# Como não há colunas em comum além de Nome, o resultado será apenas os nomes.

# 🧠 Resumo Conceitual
# | Objetivo                  | Parâmetro           |
# | ------------------------- | ------------------- |
# | Empilhar linhas           | `axis=0`            |
# | Unir colunas              | `axis=1`            |
# | União de colunas (padrão) | `join='outer'`      |
# | Apenas colunas em comum   | `join='inner'`      |
# | Reorganizar índice        | `ignore_index=True` |

# ---------------------------------------------------------------

# 🚀 Conclusão
# pd.concat() é ideal para empilhar ou combinar DataFrames
# - Quando existem colunas diferentes:
# 1. O pandas cria todas as colunas necessárias
# 2. Valores inexistentes são preenchidos com NaN
# - O comportamento pode ser controlado com axis, join e ignore_index