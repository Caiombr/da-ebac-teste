import pandas as pd
import seaborn as sns

gasolina_df = pd.read_csv('./da-ebac-teste/gasolina.csv')
gasolina_df

grafico = sns.barplot(data=gasolina_df,x='dia',y='venda', palette='Greens')
grafico = grafico.set(title='Venda de gasolina por dia')
