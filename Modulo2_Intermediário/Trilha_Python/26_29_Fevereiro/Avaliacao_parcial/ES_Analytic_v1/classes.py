from . recursos import  limpaTela,pause
from abc import ABC, abstractmethod

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from time import sleep
import pandas as pd
import numpy as np
  
class Estacoes():
    

    def requisicaoDeDados(self):
        url = 'https://portal.inmet.gov.br/dadoshistoricos'
        
        # navegador = webdriver.Chrome()
        # navegador = webdriver.Chrome(executable_path='./chromedriver_linux64/chromedriver')
        # navegador = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver_linux64')
        navegador = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver_linux64/chromedriver')
        # navegador = webdriver.Chrome(executable_path='/home/manoel/bin/chromedriver_linux64/chromedriver')
        

        # realiza a requisição e aguarda 3 segundos
        navegador.get(url)
        sleep(3)
        
        search = BeautifulSoup(navegador.page_source, 'html.parser')
        
        if search:
            print(search.prettify())
        else: 
            print('Nada encontrado')
                    
   

       

