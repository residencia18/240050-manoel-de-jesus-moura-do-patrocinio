import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df_Belem_2003 = pd.read_csv("datasets/BELEM_2003.csv", sep=';', decimal=',' , encoding='latin-1') 
df_Belem_2013 = pd.read_csv("datasets/BELEM_2013.csv", sep=';', decimal=',' , encoding='latin-1') 
df_Belem_2023 = pd.read_csv("datasets/BELEM_2023.csv", sep=';', decimal=',' , encoding='latin-1') 


# removendo valores nulos e campos vazios
df_Belem_2003 = df_Belem_2003.where(pd.notna(df_Belem_2003), np.NaN)
df_Belem_2013 = df_Belem_2013.where(pd.notna(df_Belem_2013), np.NaN)
df_Belem_2023 = df_Belem_2023.where(pd.notna(df_Belem_2023), np.NaN)

# removendo campos com dados inválidos(-9999)
df_Belem_2003 = df_Belem_2003.replace(-9999.0,np.NaN)
df_Belem_2013 = df_Belem_2013.replace(-9999.0,np.NaN)
df_Belem_2023 = df_Belem_2023.replace(-9999.0,np.NaN)

# corrigindo  formato de data no dataset BELEM_2023 de (ano/mês/dia) para (ano-mês-dia).
df_Belem_2023['DATA (YYYY-MM-DD)'] = df_Belem_2023['DATA (YYYY-MM-DD)'].str.replace('/', '-')

# corrigindo  formato de hora no dataset BELEM_2023 e Converter para o formato datetime
df_Belem_2023['HORA (UTC)'] = pd.to_datetime(df_Belem_2023['HORA (UTC)'], format='%H%M UTC')
df_Belem_2023['HORA (UTC)'] = df_Belem_2023['HORA (UTC)'].dt.strftime('%H:%M')


# Concatenando os dataframes em um único dataframe
# Convertendo a coluna 'DATA (YYYY-MM-DD)' para o formato datetime
df_concatenado_datetime = pd.concat([df_Belem_2003, df_Belem_2013,df_Belem_2023])
df_concatenado_datetime['DATA (YYYY-MM-DD)'] = pd.to_datetime(df_concatenado_datetime['DATA (YYYY-MM-DD)'] + ' ' + df_concatenado_datetime['HORA (UTC)'])

# Definindo a coluna 'DATA (YYYY-MM-DD)' como o índice do tipo DateTimeIndex
df_concatenado_datetime.set_index(['DATA (YYYY-MM-DD)'], inplace=True)
df_concatenado_datetime.sort_index(inplace=True)

# Removendo a coluna 'HORA (UTC)', pois já não é mais necessária
df_concatenado_datetime.drop(columns=['HORA (UTC)'], inplace=True)

# Definindo as estações do ano com base no calendário brasileiro
estacoes_do_ano = {
    'Verão': [1, 2, 3],
    'Outono': [4, 5, 6],
    'Inverno': [7, 8, 9],
    'Primavera': [10, 11, 12]
}

df_concatenado_datetime['Estacao'] = None

# Atribuindo a estação do ano a cada registro
for estacao, meses in estacoes_do_ano.items():
    for mes in meses:
        df_concatenado_datetime.loc[df_concatenado_datetime.index.month == mes, 'Estacao'] = estacao

# Agrupando os dados por estação do ano e calculando as médias das temperaturas e precipitações para cada estação
df_estacoes = df_concatenado_datetime.groupby(['Estacao', df_concatenado_datetime.index.year]).agg({
    'PRECIPITAï¿½ï¿½O TOTAL, HORï¿½RIO (mm)': 'mean',
    'TEMPERATURA Mï¿½XIMA NA HORA ANT. (AUT) (ï¿½C)': 'mean'
})

# Reordenando as estações do ano para começar com o Verão
df_estacoes = df_estacoes.reindex(['Verão', 'Outono', 'Inverno', 'Primavera'], level=0)

# Resetando o índice para tornar as colunas de índice em colunas e renomeando as colunas
df_estacoes.reset_index(inplace=True)
df_estacoes.rename(columns={'level_1': 'Ano'}, inplace=True)

# Cada linha do DataFrame representará uma combinação de estação do ano e ano, com as respectivas médias de temperatura e precipitação.
print("RELATÓRIO DAS ESTAÇÕES POR ANO")
print(df_estacoes.head())


# QUESTÃO 1: Analisando os dados e gerando subplot 


# Filtrando os dados para os anos desejados
anos_selecionados = [2003, 2013, 2023]
df_filtrado = df_estacoes[df_estacoes['DATA (YYYY-MM-DD)'].isin(anos_selecionados)]

# Criando o gráfico de linhas
fig, ax1 = plt.subplots(figsize=(10, 6))

# Linha para a temperatura
ax1.plot(df_filtrado[df_filtrado['DATA (YYYY-MM-DD)'] == 2003]['Estacao'], df_filtrado[df_filtrado['DATA (YYYY-MM-DD)'] == 2003]['TEMPERATURA Mï¿½XIMA NA HORA ANT. (AUT) (ï¿½C)'], label='2003 - Temp', color='blue', marker='o')
ax1.plot(df_filtrado[df_filtrado['DATA (YYYY-MM-DD)'] == 2013]['Estacao'], df_filtrado[df_filtrado['DATA (YYYY-MM-DD)'] == 2013]['TEMPERATURA Mï¿½XIMA NA HORA ANT. (AUT) (ï¿½C)'], label='2013 - Temp', color='green', marker='o')
ax1.plot(df_filtrado[df_filtrado['DATA (YYYY-MM-DD)'] == 2023]['Estacao'], df_filtrado[df_filtrado['DATA (YYYY-MM-DD)'] == 2023]['TEMPERATURA Mï¿½XIMA NA HORA ANT. (AUT) (ï¿½C)'], label='2023 - Temp', color='red', marker='o')
ax1.set_xlabel('Estação do Ano')
ax1.set_ylabel('Temperatura Média (°C)')
ax1.set_title('Evolução Média da Temperatura ao Longo dos Anos')
ax1.tick_params(axis='x', rotation=45)
ax1.legend(loc='upper left')

# Criando o segundo eixo y para a precipitação
ax2 = ax1.twinx()
ax2.plot(df_filtrado[df_filtrado['DATA (YYYY-MM-DD)'] == 2003]['Estacao'], df_filtrado[df_filtrado['DATA (YYYY-MM-DD)'] == 2003]['PRECIPITAï¿½ï¿½O TOTAL, HORï¿½RIO (mm)'], label='2003 - Precip', color='cyan', marker='s')
ax2.plot(df_filtrado[df_filtrado['DATA (YYYY-MM-DD)'] == 2013]['Estacao'], df_filtrado[df_filtrado['DATA (YYYY-MM-DD)'] == 2013]['PRECIPITAï¿½ï¿½O TOTAL, HORï¿½RIO (mm)'], label='2013 - Precip', color='magenta', marker='s')
ax2.plot(df_filtrado[df_filtrado['DATA (YYYY-MM-DD)'] == 2023]['Estacao'], df_filtrado[df_filtrado['DATA (YYYY-MM-DD)'] == 2023]['PRECIPITAï¿½ï¿½O TOTAL, HORï¿½RIO (mm)'], label='2023 - Precip', color='yellow', marker='s')
ax2.set_ylabel('Precipitação Média (mm)')
ax2.legend(loc='upper right')

plt.tight_layout()
plt.show()
