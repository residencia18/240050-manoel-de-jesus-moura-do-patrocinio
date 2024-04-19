import pandas as pd
import numpy as ny
import re


def removeNumberAndHifem(palavra):
    nome_limpo = re.sub(r'[^a-zA-Z\s]', '', palavra)
    return nome_limpo
    
df_lista_municipios = pd.read_csv("./datasets/arq_municipios_fronteiricos.csv")


# substituir todos os caracteres que não são letras ou espaços em branco por uma string vazia
# df_lista_municipios['Município'] = df_lista_municipios['Município'].replace(to_replace='[^a-zA-Z\s]', value='', regex=True)

df_lista_municipios['Município'] = df_lista_municipios['Município'].apply(removeNumberAndHifem)

# verifica o tipo de dados de cada coluna
print(df_lista_municipios.info)    
print(df_lista_municipios.dtypes)


# Converter dados numéricos para tipos numéricos
df_lista_municipios['Área territorial'] = pd.to_numeric(df_lista_municipios['Área territorial'], errors='coerce')
df_lista_municipios['PIB (IBGE/2005'] = pd.to_numeric(df_lista_municipios['PIB (IBGE/2005'], errors='coerce')
df_lista_municipios['Densidade demográfica (hab/km2)'] = pd.to_numeric(df_lista_municipios['Densidade demográfica (hab/km2)'], errors='coerce')
df_lista_municipios['PIB per capita (R$)'] = pd.to_numeric(df_lista_municipios['PIB per capita (R$)'], errors='coerce')


print(df_lista_municipios.dtypes)

# Criar um set a partir da coluna Estados
nomes_estados = set(df_lista_municipios['Estado'])

# dicionário de estados (nome completo -> sigla)
dic_estados = {
    'Acre': 'AC',
    'Alagoas': 'AL',
    'Amapá': 'AP',
    'Amazonas': 'AM',
    'Bahia': 'BA',
    'Ceará': 'CE',
    'Distrito Federal': 'DF',
    'Espírito Santo': 'ES',
    'Goiás': 'GO',
    'Maranhão': 'MA',
    'Mato Grosso': 'MT',
    'Mato Grosso do Sul': 'MS',
    'Minas Gerais': 'MG',
    'Pará': 'PA',
    'Paraíba': 'PB',
    'Paraná': 'PR',
    'Pernambuco': 'PE',
    'Piauí': 'PI',
    'Rio de Janeiro': 'RJ',
    'Rio Grande do Norte': 'RN',
    'Rio Grande do Sul': 'RS',
    'Rondônia': 'RO',
    'Roraima': 'RR',
    'Santa Catarina': 'SC',
    'São Paulo': 'SP',
    'Sergipe': 'SE',
    'Tocantins': 'TO'
}


coluna_siglas_uf = df_lista_municipios['Estado'].map(dic_estados)

df_lista_municipios['UF'] = coluna_siglas_uf
print(df_lista_municipios)