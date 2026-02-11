# 6. Como identificar e tratar outliers em uma coluna numérica usando desvio padrão ou quartis?

import pandas as pd
import numpy as np

# Criando um DataFrame de exemplo
df = pd.DataFrame({
    'valores': [10, 12, 11, 13, 12, 11, 10, 14, 100]  # 100 é outlier
})

# Antes de tratar outliers é uma boa prática visualizar os dados primeiro:
import matplotlib.pyplot as plt

plt.boxplot(df['valores'])
plt.show()

# 🎯 Qual método usar?
# | Situação                  | Melhor escolha          |
# | ------------------------- | ----------------------- |
# | Dados normais             | Z-score                 |
# | Dados assimétricos        | IQR                     |
# | Dados com muitos extremos | Transformação           |
# | ML robusto                | Mediana ou Winsorização |

# 🔎 1️⃣ Método do Desvio Padrão (Z-Score):

# Calculando média e desvio padrão
media = df['valores'].mean()
desvio = df['valores'].std()

# Calculando o Z-score
df['z_score'] = (df['valores'] - media) / desvio

# Identificando outliers
outliers = df[np.abs(df['z_score']) > 3]

print("Outliers encontrados:")
print(outliers)

# 📊 2️⃣ Método dos Quartis (IQR):
# Esse método é mais robusto que o desvio padrão (funciona melhor quando os dados não são normais).

# 📌 Passos:
# 1. Calcular Q1 (25%).
# 2. Calcular Q3 (75%).
# 3. Calcular IQR.
# 4. Definir limites.

# Calculando quartis
Q1 = df['valores'].quantile(0.25)
Q3 = df['valores'].quantile(0.75)

IQR = Q3 - Q1

limite_inferior = Q1 - 1.5 * IQR
limite_superior = Q3 + 1.5 * IQR

# Identificando outliers
outliers_iqr = df[
    (df['valores'] < limite_inferior) |
    (df['valores'] > limite_superior)
]

print("Outliers pelo método IQR:")
print(outliers_iqr)

# -------------------------------------------------

# 🛠️ Como Tratar Outliers?
# Existem 4 estratégias principais:

# 🔹 1️⃣ Remover os Outliers:
df_sem_outliers = df[
    (df['valores'] >= limite_inferior) &
    (df['valores'] <= limite_superior)
]

#  Obs.: ✔ Útil quando são erros claros.
## ⚠ Pode remover dados importantes!

# 🔹 2️⃣ Substituir pela Mediana (mais robusto):
mediana = df['valores'].median()

df.loc[
    (df['valores'] < limite_inferior) |
    (df['valores'] > limite_superior),
    'valores'
] = mediana

# Obs.: ✔ Essa é uma boa prática para ML!

# 🔹 3️⃣ Winsorização (Limitar valores extremos):
df['valores'] = np.where(
    df['valores'] < limite_inferior,
    limite_inferior,
    np.where(
        df['valores'] > limite_superior,
        limite_superior,
        df['valores']
    )
)
# ✔ Mantém todos os dados.
# ✔ Muito usado em modelos financeiros.

# 🔹 4️⃣ Transformações:
## Exemplo: log, raiz quadrada
df['valores_log'] = np.log(df['valores'])

# ✔ Reduz impacto de valores extremos
