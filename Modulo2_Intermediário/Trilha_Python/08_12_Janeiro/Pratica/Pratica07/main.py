import pandas as pd
import numpy as np


# QUESTAO 1 IMPORTANDO DADOS

print("\n DADOS BRUTOS DO DATASET\n")

df_Belem_2003 = pd.read_csv("datasets/BELEM_2003.csv", sep=';', decimal=',' , encoding='latin-1') 
df_Belem_2013 = pd.read_csv("datasets/BELEM_2013.csv", sep=';', decimal=',' , encoding='latin-1') 
df_Belem_2023 = pd.read_csv("datasets/BELEM_2023.csv", sep=';', decimal=',' , encoding='latin-1') 



df_Belem_2003 = df_Belem_2003.where(pd.notna(df_Belem_2003), np.NaN)
df_Belem_2013 = df_Belem_2013.where(pd.notna(df_Belem_2013), np.NaN)
df_Belem_2023 = df_Belem_2023.where(pd.notna(df_Belem_2023), np.NaN)

df_Belem_2003 = df_Belem_2003.replace(-9999.0,np.NaN)
df_Belem_2013 = df_Belem_2013.replace(-9999.0,np.NaN)
df_Belem_2023 = df_Belem_2023.replace(-9999.0,np.NaN)

# Exibindo os primeiros registros do DataFrame
print("DADOS BELEM 2003 \n")
print(df_Belem_2003.head)

print("\nDADOS BELEM 2013 \n")
print(df_Belem_2013.head)

print("\nDADOS BELEM 2023 \n")
print(df_Belem_2023.head)


# Exercício 2: Juntando os datasets

print("\nEXERCÍCIO 2: JUNTANDO OS DATASETS\n")


df_Belem_2003['DATA (YYYY-MM-DD)'] = pd.to_datetime(df_Belem_2003['DATA (YYYY-MM-DD)'], format='%Y-%m-%d', errors='coerce')
df_Belem_2013['DATA (YYYY-MM-DD)'] = pd.to_datetime(df_Belem_2013['DATA (YYYY-MM-DD)'], format='%Y-%m-%d', errors='coerce')
df_Belem_2023['DATA (YYYY-MM-DD)'] = pd.to_datetime(df_Belem_2023['DATA (YYYY-MM-DD)'], format='%Y-%m-%d', errors='coerce')


df_combined = pd.concat([df_Belem_2003, df_Belem_2013, df_Belem_2023], ignore_index=True)

df_combined.set_index(['DATA (YYYY-MM-DD)'], inplace=True)
df_combined.sort_index(inplace=True)

# Converte o índice para um MultiIndex com anos, meses e dias
df_combined.index = pd.MultiIndex.from_tuples([(d.year, d.month, d.day) for d in df_combined.index], names=['Ano', 'Mês', 'Dia'])




print("\nDADOS DE BELEM COMBINADOS 2003,2013,2023 \n")
print(df_combined)

# Exercício 3: Analisando os DataFrame

# 3.1

print("\nCOMPARAÇÃO  DOS DADOS\n")
print("ANÁLISE DE 2003\n")


df_colunas = ['PRECIPITAï¿½ï¿½O TOTAL, HORï¿½RIO (mm)', 'TEMPERATURA DO AR - BULBO SECO, HORARIA (ï¿½C)', 'TEMPERATURA DO PONTO DE ORVALHO (ï¿½C)','TEMPERATURA Mï¿½XIMA NA HORA ANT. (AUT) (ï¿½C)','TEMPERATURA Mï¿½NIMA NA HORA ANT. (AUT) (ï¿½C)','TEMPERATURA ORVALHO MAX. NA HORA ANT. (AUT) (ï¿½C)','TEMPERATURA ORVALHO MIN. NA HORA ANT. (AUT) (ï¿½C)']
media_colunas = df_Belem_2003[df_colunas].mean()
max_colunas = df_Belem_2003[df_colunas].max()
min_colunas = df_Belem_2003[df_colunas].min()

dados_2003 = {'Média': media_colunas, 'Valor Max':max_colunas, 'Valor Min':min_colunas}
df_dados_2003 = pd.DataFrame(dados_2003)
print(df_dados_2003)


print("\nANÁLISE DE 2013\n")

media_colunas = df_Belem_2013[df_colunas].mean()
max_colunas = df_Belem_2013[df_colunas].max()
min_colunas = df_Belem_2013[df_colunas].min()

dados_2013 = {'Média': media_colunas, 'Valor Max':max_colunas, 'Valor Min':min_colunas}
df_dados_2013 = pd.DataFrame(dados_2013)

print(df_dados_2013.head(15))



print("\nANÁLISE DE 2023\n")

media_colunas = df_Belem_2023[df_colunas].mean()
max_colunas = df_Belem_2023[df_colunas].max()
min_colunas = df_Belem_2023[df_colunas].min()

dados_2023 = {'Média': media_colunas, 'Valor Max':max_colunas, 'Valor Min':min_colunas}
df_dados_2023 = pd.DataFrame(dados_2023)

print(df_dados_2023)


