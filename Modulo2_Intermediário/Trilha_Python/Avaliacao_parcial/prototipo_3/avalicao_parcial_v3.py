# import para web scraping
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
from time import sleep
import pandas as pd
import numpy as np

import requests
import zipfile
# imports para módulos de interface

from datetime import datetime

from tkinter import *
from tkinter.ttk import *

# imports para módulos de recursos
import os
import sys

class Estacoes():
    
    
    def requisicaoDeDados(self):
        url = 'https://portal.inmet.gov.br/dadoshistoricos'
        navegador = webdriver.Chrome()
        # navegador = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver_linux64/chromedriver')

        # realiza a requisição e aguarda 3 segundos
        navegador.get(url)
        sleep(3)
        
        search = BeautifulSoup(navegador.page_source, 'html.parser')
        search_years_results = search.find_all('article', class_='post-preview')
        
        if search_years_results:
            # dicionário para armazenar os anos e seus links
            anos_links_Dodos_disponiveis = {}
            
            # Iterando sobre as tags 'article' encontradas
            for article in search_years_results:
                tag_a = article.find('a')
                if tag_a:
                    href_value = tag_a['href']
                    # Acessando o conteúdo da tag 'a'
                    content_text = tag_a.text.strip()
                    anos_links_Dodos_disponiveis[content_text] = href_value

            return anos_links_Dodos_disponiveis
        else: 
            print('Nada encontrado')
            return None
    
    def downloadDataFrame(self,url) :
        try:
     
            # Baixar o arquivo usando requests
            resposta = requests.get(url)
            
            # Obter o diretório atual
            diretorio_atual = os.getcwd()
            
            nome_arquivo = url.split("/")[-1]
            # Remover a extensão .zip do nome do arquivo
            nome_arquivo = nome_arquivo.split(".")[0]
        
            # Criar a pasta de destino no diretório atual
            pasta_destino = os.path.join(diretorio_atual, "Avaliacao_parcial/prototipo_3/datasets")
            
            if not os.path.exists(pasta_destino):
                os.makedirs(pasta_destino)
            
            # Caminho completo para o arquivo ZIP
            caminho_arquivo_zip = os.path.join(pasta_destino, nome_arquivo + ".zip")
            
            # Salvar o arquivo ZIP
            with open(caminho_arquivo_zip, "wb") as arquivo_zip:
                arquivo_zip.write(resposta.content)

            # Extrair o conteúdo do arquivo ZIP para a pasta de destino
            with zipfile.ZipFile(caminho_arquivo_zip, 'r') as zip_ref:
                zip_ref.extractall(pasta_destino)
            
            # Remover o arquivo ZIP após a extração
            os.remove(caminho_arquivo_zip)           
            print("Download concluído com sucesso! O arquivo foi salvo em:", caminho_arquivo_zip)
            
            # gera uma lista com o nome dos arquivos descompactados (csv)
            arquivos_descompactados = os.listdir(pasta_destino + "/" + nome_arquivo)
            
            # Construir o dicionário com o nome do arquivo e o caminho completo
            resultado = {}
            for arquivo in arquivos_descompactados:
                nome_arquivo_formatado = arquivo.split("_")[4]
                caminho_arquivo = os.path.join(pasta_destino + "/" + nome_arquivo, arquivo)
                resultado[nome_arquivo_formatado] = caminho_arquivo
            return resultado
            
        except Exception as e:
            print("Ocorreu um erro durante o download:", e)
            return None
        
    def CalcTempMediaCSV(self, arquivoURL):
    
        try:
            # Ler o arquivo CSV em um DataFrame do pandas, pulando as 8 primeiras linhas
            df = pd.read_csv(arquivoURL, sep=';', decimal=',', parse_dates=['DATA (YYYY-MM-DD)'], skiprows=8, encoding='latin-1')
        
            
            # Tratando valores ausentes ou nulos
            df = df.where(pd.notna(df), np.NaN)
            df = df.replace(-9999.0,np.NaN)

            print("\nDataroot Tratado\n")
            print(df.head())
            
            # Calcular a média de temperatura máxima por mês
            df['DATA (YYYY-MM-DD)'] = pd.to_datetime(df['DATA (YYYY-MM-DD)'])
            df['Mês'] = df['DATA (YYYY-MM-DD)'].dt.month
            media_temp_max_por_mes = df.groupby('Mês')['TEMPERATURA MÁXIMA NA HORA ANT. (AUT) (°C)'].mean()
            
            # return media_temp_max_por_mes
            return media_temp_max_por_mes
        
        except Exception as e:
            print("Ocorreu um erro ao processar o arquivo CSV:", e)
            return None   
      
    def CalcMediaPreciptacaoCSV(self, arquivoURL):
    
        try:
            # Ler o arquivo CSV em um DataFrame do pandas, pulando as 8 primeiras linhas
            df = pd.read_csv(arquivoURL, sep=';', decimal=',', parse_dates=['DATA (YYYY-MM-DD)'], skiprows=8, encoding='latin-1')
        
            
            # Tratando valores ausentes ou nulos
            df = df.where(pd.notna(df), np.NaN)
            df = df.replace(-9999.0,np.NaN)

            print("\nDataroot Tratado\n")
            print(df.head())
            print(df.info())
            
            # Calcular a média de temperatura máxima por mês
            df['DATA (YYYY-MM-DD)'] = pd.to_datetime(df['DATA (YYYY-MM-DD)'])
            df['Mês'] = df['DATA (YYYY-MM-DD)'].dt.month
            media_temp_max_por_mes = df.groupby('Mês')['PRECIPITAÇÃO TOTAL, HORÁRIO (mm)'].sum()
            
            # return media_temp_max_por_mes
            return media_temp_max_por_mes
        
        except Exception as e:
            print("Ocorreu um erro ao processar o arquivo CSV:", e)
            return None   
      
        
    def exclusaoDeDados(self):
        pass

            
def telaError():
    
    def quit():
        print('Hello, I must be going...') 
        sys.exit()
        
    root = Tk()
    root.title("Estações Meteorológicas")

    # Frame para conter os widgets
    root = Frame(root)
    root.grid(row=0, column=0, sticky=(W,E,N,S))

    # Mensagem de titulo
    messageError = Label(root, text="Houve um error na aplicação, por favor volte mais tarde ")
    messageError.grid(row=0,column=1, pady=20, padx=20)
    messageError.config(font=('Helvetica', 12, 'bold')) 
    
    
  
    botaoSair = Button(root, text='Sair', command=quit) 
    botaoSair.grid(row=1,column=1, pady=20, padx=20)
    root.mainloop()        
def widget_lista_estacoes(root,datas):
    estacoes = Estacoes() 
       
    def estacao_selecionada(event):
        
        index = lista_estacoes.curselection()[0]
        item_selecionado = lista_estacoes.get(index)
        print("estação selecionada:", item_selecionado)       
        
        if datas[item_selecionado]:
            serie_mediaTemp = estacoes.CalcTempMediaCSV(datas[item_selecionado])
            serie_mediaPreciptacao = estacoes.CalcMediaPreciptacaoCSV(datas[item_selecionado])
            
            if serie_mediaTemp is not None:
                widget_grafico_temperatura(root,serie_mediaTemp)
                
            if serie_mediaPreciptacao is not None:
                widget_grafico_precipitação(root,serie_mediaPreciptacao)
     
        
    # Label da Listbox
    labelListboxEstacoes = Label(root, text="Selecione a estação:")
    labelListboxEstacoes.grid(row=2, column=1,padx=10, pady=5)
    labelListboxEstacoes.config(font=('Helvetica', 12, 'bold'),foreground='white',background="#242424") 
    
    
    # Lista para exibir as estações de medições
    list_estacoes = Variable(value = list(datas.keys()))
    
    lista_estacoes = Listbox(
        root,
        height=12,
        selectmode=BROWSE,
        width= 0,
        listvariable=list_estacoes
    )
    lista_estacoes.grid(row=3, column=1, padx=10, pady=5)
    lista_estacoes.config(foreground="#242424", background="#cecece",font=('Helvetica', 10, 'bold'))
    lista_estacoes.bind("<<ListboxSelect>>", estacao_selecionada)
    
def widget_grafico_temperatura(root, dadosTempMedia):
   
    # dados do gráfico
    meses = dadosTempMedia.index
    valores = dadosTempMedia.values

    # Criar o gráfico de linhas
    fig, ax = plt.subplots(figsize=(5, 4))
    ax.plot(meses, valores, marker='o', color='blue', linestyle='-')
    ax.set_xlabel('Mês')
    ax.set_ylabel('Temperatura Média Máxima (°C)')
    ax.set_title(' MÉDIA TEMPERATURA MÁXIMA NA HORA ANT. (AUT)')

    # Integrar o gráfico ao Tkinter
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.draw()
    canvas.get_tk_widget().grid(row=4, column=0, padx=5, pady=5)


def widget_grafico_precipitação(root, dadosTempMedia):
   
    # dados do gráfico
    meses = dadosTempMedia.index
    valores = dadosTempMedia.values

    # Criar o gráfico de linhas
    fig, ax = plt.subplots(figsize=(5, 4))
    ax.plot(meses, valores, marker='o', color='red', linestyle='-')
    ax.set_xlabel('Mês')
    ax.set_ylabel('Precipitação Total')
    ax.set_title('Acumulado Precipitação Total')

    # Integrar o gráfico ao Tkinter
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.draw()
    canvas.get_tk_widget().grid(row=4, column=1, padx=5, pady=5)


def widget_Label_AnoSelecionado(root, anoSelecinado):  
    LabelAnoSelecinado = Label(root, text=anoSelecinado)
    LabelAnoSelecinado.grid(row=1,column=1, pady=10)
    LabelAnoSelecinado.config(font=('Helvetica', 12, 'bold'),foreground='white',background="#242424") 
  
def telaPrincipal(anos_disponiveis):
    estacoes = Estacoes()
    # Define a janela principal
    root = Tk()
    root.title("Estações Meteorológicas")
    root.configure(bg="#242424")
    
    # Mensagem de titulo
    messageMain = Label(root, text="Dados das estações meteorológicas brasileiras")
    messageMain.grid(row=0,column=1, pady=10)
    messageMain.config(font=('Helvetica', 16, 'bold'),foreground="green", background="#242424") 
    
    def ano_selecionado(event):
        index = listbox_anos_disponiveis.curselection()[0]
        item_selecionado = listbox_anos_disponiveis.get(index)
        
        print("ano selecionado:", item_selecionado)
        widget_Label_AnoSelecionado(root,item_selecionado)
        
        disc_estacoes = estacoes.downloadDataFrame(anos_disponiveis[item_selecionado])
        widget_lista_estacoes(root,disc_estacoes)
    
    def quit():
        print('Hello, I must be going...') 
        sys.exit()
        
      
   
    # Label da Listbox p/ anos
    labelListboxAnos = Label(root, text=" Selecione o ano:")
    labelListboxAnos.grid(row=2, column=0,padx=10, pady=5)
    labelListboxAnos.config(font=('Helvetica', 12, 'bold'), foreground='white',background="#242424") 
    
    
    # Listbox para selecionar o ano

    list_anos = Variable(value = list(anos_disponiveis.keys()))
    listbox_anos_disponiveis = Listbox(
        root,
        height=12,
        listvariable=list_anos,
        selectmode=BROWSE,
        width= 0
        
    )

    listbox_anos_disponiveis.grid(row=3, column=0, padx=10, pady=10)
    listbox_anos_disponiveis.config(foreground="#242424", background="#cecece",font=('Helvetica', 10, 'bold'))
    listbox_anos_disponiveis.bind("<<ListboxSelect>>", ano_selecionado)


    # Botão p/ fecha janela principal
    button = Button(root, text="Fechar", command=quit)
    button.grid(row=2, column=2, padx=10, pady=10)



    root.mainloop()
def main():

    estacoes = Estacoes()
    dados_anos_disponiveis  =  estacoes.requisicaoDeDados()
    if dados_anos_disponiveis != None :
        telaPrincipal(dados_anos_disponiveis)
               
    
if __name__ == "__main__":
    main()
