# 8. Utilizando pandas, como realizar a leitura de um arquivo CSV em um DataFrame e exibir as primeiras linhas?

# 📌 Como ler um arquivo CSV com pandas e visualizar as primeiras linhas?

# 🧱 1️⃣ Passo a passo básico
import pandas as pd

# Lendo o arquivo CSV
df = pd.read_csv('dados.csv')

# Exibindo as 5 primeiras linhas (padrão)
print(df.head())

# 📊 O que acontece?
## pd.read_csv('dados.csv') → Carrega o arquivo para um DataFrame
## f.head() → Mostra as 5 primeiras linhas
## df.head(n) → Mostra as n primeiras linhas

# Exemplo:
print(df.head(10))  # Mostra as 10 primeiras linhas

#--------------------------------------------------------------------------

# 📂 2️⃣ Lendo arquivos com configurações específicas:
# 🔹 Arquivo com separador diferente (ex: ;)

df = pd.read_csv('dados.csv', sep=';')

# 🔹 Arquivo com codificação específica
df = pd.read_csv('dados.csv', encoding='utf-8')

# ou
df = pd.read_csv('dados.csv', encoding='latin-1')

# 🔹 CSV sem cabeçalho
df = pd.read_csv('dados.csv', header=None)

#--------------------------------------------------------------------------

# 🔎 3️⃣ Outras formas úteis de visualizar os dados:
# Além do head():
df.tail()        # Últimas 5 linhas
df.info()        # Informações gerais do DataFrame
df.describe()    # Estatísticas descritivas
df.shape         # Número de linhas e colunas
df.columns       # Nome das colunas

# 🧠 Exemplo Completo:
import pandas as pd

# Lendo o arquivo
df = pd.read_csv('dados.csv')

# Verificando estrutura
print("Dimensão do dataset:", df.shape)

# Visualizando primeiras linhas
print("\nPrimeiras linhas:")
print(df.head())

# 🎯 Resumo:
# | Função          | Finalidade                    |
# | --------------- | ----------------------------- |
# | `pd.read_csv()` | Lê arquivo CSV                |
# | `df.head()`     | Mostra primeiras 5 linhas     |
# | `df.head(n)`    | Mostra n primeiras linhas     |
# | `df.tail()`     | Mostra últimas linhas         |
# | `df.info()`     | Mostra estrutura do DataFrame |

#--------------------------------------------------------------------------

# 🚀 Conclusão
# Para ler um CSV e visualizar os dados iniciais:
import pandas as pd
df = pd.read_csv('arquivo.csv')
df.head()
# Esse modelo é simples, direto e essencial para qualquer pipeline de análise de dados ou machine learning!