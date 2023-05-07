from flask import Flask, render_template
import pandas as pd
import plotly.graph_objs as go
import plotly.figure_factory as ff
import plotly.graph_objs as go

app = Flask(__name__)

# Rota principal
@app.route("/")
def index():
    # Lê o arquivo excel
    df = pd.read_excel('Vendas.xlsx')

    # Agrupa os dados por 'ID Loja' e soma o 'Valor Final'
    df_resultado = df.groupby('ID Loja')['Valor Final'].sum().reset_index()
    # Ordena o dataframe por ordem decrescente do 'Valor Final'
    df_resultado = df_resultado.sort_values(by='Valor Final', ascending=False)


    
    # Cria a tabela
    fig1 = ff.create_table(df_resultado)

     # Cria o gráfico de barras
    color_map = {'Iguatemi Campinas': 'blue', 
             'Bourbon Shopping SP': 'red', 
             'Norte Shopping': 'green', 
             'Center Shopping Uberlândia': 'orange', 
             'Iguatemi Esplanada': 'purple'}

    colors = [color_map[val] for val in df_resultado['ID Loja']]
    fig2 = go.Figure(go.Bar(x=df_resultado['ID Loja'], y=df_resultado['Valor Final'], marker=dict(color=colors)))



    # Renderiza a página HTML e passa os gráficos como parâmetros
    return render_template('index.html', graph1=fig1.to_html(full_html=False), graph2=fig2.to_html(full_html=False))


# Executa a aplicação Flask
if __name__ == '__main__':
    app.run(debug=True)
