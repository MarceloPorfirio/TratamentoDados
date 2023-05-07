import plotly.express as px
import plotly.figure_factory as ff
import plotly.subplots as sp
import pandas as pd

# Lê o arquivo Excel
df_vendas = pd.read_excel('vendas.xlsx')

# Agrupa por ID Loja e soma o valor final
df_resultado = df_vendas.groupby(['ID Loja']).sum()['Valor Final'].reset_index()


# Cria o gráfico de barras com plotly.express
fig1 = px.bar(df_resultado, x='ID Loja', y='Valor Final', title='Valor Final por ID Loja')

# Converte o dataframe para uma matriz de valores
table_data = df_resultado.to_numpy()

# Cria a tabela com plotly.figure_factory
fig2 = ff.create_table(table_data)

# Cria um objeto subplot com 2 linhas e 1 coluna
fig = sp.make_subplots(rows=2, cols=1)

# Adiciona o gráfico de barras à primeira linha
fig.add_trace(fig1.data[0], row=1, col=1)
fig.update_layout(title=fig1.layout.title.text, yaxis_title=fig1.layout.yaxis.title.text)

# Adiciona a tabela à segunda linha
fig.add_trace(fig2.data[0], row=2, col=1)

# Exibe o objeto subplot no navegador
fig.show()
