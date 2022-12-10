import pandas as pd
import plotly.express as px
import warnings

warnings.simplefilter(action='ignore', category=FutureWarning)

# Lendo o arquivo como um dataframe pandas.

df = pd.read_csv("winequality-red.csv", sep=";")

df.columns = ["Acidez Fixa", "Acidez Volátil", "Ácido Cítrico",
              "Açúcar Residual", "Cloretos", "Dióxido de Enxofre Livre",
              "Dióxido de Enxofre Total", "Densidade", "pH", "Sulfatos",
              "Álcool", "Qualidade"]

# Classificando por categoria do vinho (Seco, Meio-Seco e Suave) e adicionando a coluna "Categoria".

categoria = []

for line in range(len(df)):
    if df.loc[line, 'Açúcar Residual'] <= 4:
        categoria += ["Seco"]
    elif df.loc[line, 'Açúcar Residual'] > 4 and df.loc[line, 'Açúcar Residual'] <= 25:
        categoria += ["Meio-Seco"]
    elif df.loc[line, 'Açúcar Residual'] > 25:
        categoria += ["Suave"]

df["Categoria"] = categoria

# Classificando por tipo de corpo do vinho (Leve, Médio, Encorpado e Pesado) e adicionando a coluna "Tipo de Corpo".

tipoDeCorpo = []

for line in range(len(df)):
    if df.loc[line, 'Álcool'] <= 12.5:
        tipoDeCorpo += ["Leve"]
    elif df.loc[line, 'Álcool'] > 12.5 and df.loc[line, 'Álcool'] <= 13.5:
        tipoDeCorpo += ["Médio"]
    elif df.loc[line, 'Álcool'] > 13.5 and df.loc[line, 'Álcool'] <= 15:
        tipoDeCorpo += ["Encorpado"]
    elif df.loc[line, 'Álcool'] > 15:
        tipoDeCorpo += ["Pesado"]

df["Tipo de Corpo"] = tipoDeCorpo

# Totalizando por Categoria.

seco = 0
for i in range(len(df)):
    if df.loc[i, 'Categoria'] == 'Seco':
        seco += 1

meioSeco = 0
for i in range(len(df)):
    if df.loc[i, 'Categoria'] == 'Meio-Seco':
        meioSeco += 1

suave = 0
for i in range(len(df)):
    if df.loc[i, 'Categoria'] == 'suave':
        suave += 1

dfCategoria = pd.DataFrame({
    "Categoria": ["Seco", "Meio-Seco", "Suave"],
    "Quantidade": [seco, meioSeco, suave]
})

# Totalizando os valores por tipo de corpo.

leve = 0
for i in range(len(df)):
    if df.loc[i, 'Tipo de Corpo'] == 'Leve':
        leve += 1

medio = 0
for i in range(len(df)):
    if df.loc[i, 'Tipo de Corpo'] == 'Médio':
        medio += 1

encorpado = 0
for i in range(len(df)):
    if df.loc[i, 'Tipo de Corpo'] == 'Encorpado':
        encorpado += 1

pesado = 0
for i in range(len(df)):
    if df.loc[i, 'Tipo de Corpo'] == 'Pesado':
        pesado += 1

dfBT = pd.DataFrame({
    "Tipo de Corpo": ["Leve", "Médio", "Encorpado", "Pesado"],
    "Quantidade": [leve, medio, encorpado, pesado],
})

# Exibindo Gráfico das Categorias

fig = px.bar(dfCategoria, x='Quantidade', y='Categoria', barmode='group', orientation="h", template='plotly_dark', title="Quantidades por Categoria")

fig.show()

# Exibindo Gráfico dos Tipos de Corpo

fig = px.bar(dfBT, x='Quantidade', y='Tipo de Corpo', barmode='group', orientation="h", template='plotly_dark', title="Quantidades por Tipo de Corpo")

fig.show()

# Exibindo as médias dos compostos.

df.mean()

# Vinho mais forte do DataSet (Com base em álcool)

alcool = 0

for line in range(len(df)):
    if df.loc[line, 'Álcool'] > alcool:
        alcool = df.loc[line, 'Álcool']
        maisForte = line
    else:
        continue

df.loc[maisForte]

# Vinho mais fraco do DataSet (Com base em álcool)

alcool = 20

for line in range(len(df)):
    if df.loc[line, 'Álcool'] < alcool:
        alcool = df.loc[line, 'Álcool']
        maisFraco = line
    else:
        continue

df.loc[maisFraco]
