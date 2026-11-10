from dash import Dash, dcc, html
import pandas as pd
import plotly.express as px

# 1. Carregar o arquivo CSV
df = pd.read_csv('ecommerce_estatistica.csv')

# Usando as colunas corretas que aparecem no seu ficheiro ('Marca' e 'Preço')
fig = px.bar(
    df.head(10),
    x='Marca',
    y='Preço',
    title='Painel de E-commerce - Preço por Marca',
    template='plotly_white',
)

# 2. Criar a aplicação Dash
app = Dash(__name__)

app.layout = html.Div(
    [
        html.H1(
            'Painel de Análise de E-commerce',
            style={'textAlign': 'center', 'color': '#333'},
        ),
        html.P(
            'Visualização gerada com sucesso através de Dash.',
            style={'textAlign': 'center'},
        ),
        dcc.Graph(id='grafico-principal', figure=fig),
    ],
    style={'padding': '20px', 'fontFamily': 'Arial'},
)

# Executar a aplicação
if __name__ == '__main__':
  app.run(debug=True)