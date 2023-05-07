import pandas as pd
import plotly.figure_factory as ff
import plotly.express as px
import plotly.subplots as sp
import plotly.io as pio

dados = pd.read_excel("Vendas.xlsx")

# Agrupar os dados por 'ID Loja' e somar o 'Valor Final'
resultado = dados.groupby('ID Loja')['Valor Final'].sum()

# Criar um novo dataframe com o resultado
df_resultado = pd.DataFrame(resultado).reset_index()

# Altera o renderizador para jupyterlab
pio.renderers.default = 'jupyterlab'

# Cria a tabela com plotly.figure_factory
fig2 = ff.create_table(df_resultado)

# Cria o gráfico de barras com plotly.express
fig1 = px.bar(df_resultado, x='ID Loja', y='Valor Final', title='Valor Final por ID Loja')

# Cria um objeto subplot com 2 linhas e 1 coluna
fig = sp.make_subplots(rows=2, cols=1)

# Adiciona o gráfico de barras à primeira linha
fig.add_trace(fig1.data[0], row=1, col=1)
fig.update_layout(title=fig1.layout.title.text, yaxis_title=fig1.layout.yaxis.title.text)

# Adiciona a tabela à segunda linha
fig.add_trace(fig2.data[0], row=2, col=1)

# Exibe o objeto subplot no navegador
fig.show()
