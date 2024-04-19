from . recursos import  limpaTela,pause
from . interface import menu
from . classes import Estacoes
import numpy as np



'''
para validar a requisição ao site das estações
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

requisicao = requests.get(link, headers=headers)
'''
def main():
 
    while True:
        estacoes = Estacoes()
        opcao = menu()
        
        match opcao:
           
            case 1:
                estacoes.requisicaoDeDados()
                
             

                pause()
                
                
            case 0:
                limpaTela()
                print("\n\tObrigado por usar o DataFruta!")
                pause()
                exit()  
            case _:
                limpaTela()
                print("\n\tOps, opção inválida! Tente novamente.")
                pause()
    
if __name__ == "__main__":
    main()
