# 10. Utilizando pandas, como lidar com valores ausentes (NaN) em um DataFrame?

# 📌 Como lidar com valores ausentes (NaN) no pandas?
# No pandas, valores ausentes são representados como:
# NaN (Not a Number)
# None (em alguns casos)

# Para lidar com eles, normalmente seguimos três etapas:
# 1️⃣ Identificar.
# 2️⃣ Analisar.
# 3️⃣ Tratar (remover ou substituir).

#--------------------------------------------------------------------------

# 🔎 1️⃣ Identificando valores ausentes
# ✅ Verificar se há valores ausentes:
import pandas as pd
import numpy as np

df = pd.DataFrame({
    'Nome': ['Ana', 'Bruno', 'Carlos', 'Diana'],
    'Idade': [23, np.nan, 29, 42],
    'Salario': [3000, 5000, np.nan, 7000]
})

print(df.isnull())

# ✅ Contar valores ausentes por coluna:
print(df.isnull().sum())

# 🗑️ 2️⃣ Removendo valores ausentes:
# 🔹 Remover linhas com qualquer NaN
df_limpo = df.dropna()

# 🔹 Remover colunas com NaN
df_limpo = df.dropna(axis=1)

# 🔹 Remover apenas se houver NaN em uma coluna específica
df_limpo = df.dropna(subset=['Idade'])

#--------------------------------------------------------------------------

# 🔄 3️⃣ Substituindo valores ausentes
# Em muitos casos, não é recomendado remover os dados, principalmente em Machine Learning.

# 🔹 Substituir por um valor fixo
df['Idade'] = df['Idade'].fillna(0)

# 🔹 Substituir pela média
media_idade = df['Idade'].mean()
df['Idade'] = df['Idade'].fillna(media_idade)

# 🔹 Substituir pela mediana (mais robusto)
mediana_salario = df['Salario'].median()
df['Salario'] = df['Salario'].fillna(mediana_salario)

# 🔹 Substituir pela moda (para variáveis categóricas)
moda_nome = df['Nome'].mode()[0]
df['Nome'] = df['Nome'].fillna(moda_nome)

#--------------------------------------------------------------------------

# 🔁 4️⃣ Preenchimento baseado na linha anterior ou posterior. (Muito usado em séries temporais).
# 🔹 Forward Fill (preenche com valor anterior)
df.fillna(method='ffill', inplace=True)

# 🔹 Backward Fill
df.fillna(method='bfill', inplace=True)

#--------------------------------------------------------------------------

# 📊 5️⃣ Estratégia recomendada para Machine Learning
# | Tipo de variável      | Estratégia recomendada |
# | --------------------- | ---------------------- |
# | Numérica normal       | Média                  |
# | Numérica com outliers | Mediana                |
# | Categórica            | Moda                   |
# | Série temporal        | Forward/Backward fill  |

# 🧠 Exemplo Completo:
import pandas as pd
import numpy as np

df = pd.DataFrame({
    'Nome': ['Ana', 'Bruno', 'Carlos', 'Diana'],
    'Idade': [23, np.nan, 29, 42],
    'Salario': [3000, 5000, np.nan, 7000]
})

# Verificando valores ausentes
print(df.isnull().sum())

# Preenchendo valores numéricos com a mediana
df['Idade'].fillna(df['Idade'].median(), inplace=True)
df['Salario'].fillna(df['Salario'].median(), inplace=True)

print(df)

#--------------------------------------------------------------------------

# 🎯 Conclusão:
# Para lidar com valores ausentes no pandas, utilizamos principalmente:
### isnull() → identificar
### dropna() → remover
### fillna() → substituir
# A escolha da estratégia depende do contexto dos dados e do objetivo da análise.