import pandas as pd
import matplotlib.pyplot as plt
import mpltable

dados = pd.read_excel("Vendas.xlsx")

resultado = dados.groupby('ID Loja')['Valor Final'].sum()
df_resultado = pd.DataFrame(resultado)

titulo = 'Soma do Valor Final por ID Loja'
cores = ('#F5F5F5', '#D3D3D3')
table = mpltable.table(df_resultado, titulo=titulo, colWidths=[0.2, 0.2], cellColours=[cores]*len(df_resultado), cellLoc='center')

# Exibir a tabela na tela
fig, ax = plt.subplots()
ax.axis('off')
table.auto_set_font_size(False)
table.set_fontsize(14)
plt.show()

# resultado.plot(kind='bar', figsize=(6,4))
# plt.xlabel('ID Loja')
# plt.ylabel('Valor Final')
# plt.title('Soma do Valor Final por ID Loja')
# plt.show()

print(resultado)