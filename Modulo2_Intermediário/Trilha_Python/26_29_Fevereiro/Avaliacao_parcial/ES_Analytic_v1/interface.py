from . recursos import  limpaTela,pause
from datetime import datetime
import locale

from tkinter import *
from tkinter.ttk import *

locale.setlocale(locale.LC_TIME, 'pt_BR.UTF-8')
data_e_hora_atual = datetime.now()
def menu():
    
    while True:
        
        opcao = -1
        limpaTela()
        formato_personalizado = "\n\t%A, %d de %B de %Y %H:%M:%S"
        data_e_hora_formatada = data_e_hora_atual.strftime(formato_personalizado)
        print(data_e_hora_formatada)
        print("\tFalta", (datetime(data_e_hora_atual.year, 12, 31) - data_e_hora_atual).days + 1, "dias para o fim do ano")
    
        print("\n\t======= STATION ANALYTIC =======\n\n")
        print("\t[1] - INICIAR INTERFACE DO SISTEMA")
        print("\t[0] - SAIR")
         
        try:
           opcao = int(input("\tENTRADA -> "))
        except:
            limpaTela()
            print("\n\tOps, valor inválido! Informe apenas as opções disponíveis...")
            pause()
            
  
        if(opcao < 0 or opcao > 1):
            limpaTela()
            print("\n\tOps, opção inválida! Tente novamente...")
            pause()
        else:
            return opcao
            
            
def telaPrincipal():
    # Dados de exemplo: lista de estações meteorológicas e anos de medições
    estacoes_meteorologicas = {
        '2003': ["Salvador", "Ilhéus", "São Paulo", "Rio de Janeiro"],
        '2013': ["Salvador", "Ilhéus", "São Paulo", "Rio de Janeiro"],
        '2023': ["Salvador", "Ilhéus", "São Paulo", "Rio de Janeiro"]
    }

    def selecionar_estacao(event):
        # Limpa a lista de anos antes de adicionar novos itens
        lista_estacoes.delete(0, END)
        
        # Obtém o nome da estação selecionada
        ano_estacao_selecionada = anos_estacoes_combobox.get()
        
        # Obtém a lista das estação do ano selecionado
        estacoes = estacoes_meteorologicas.get(ano_estacao_selecionada, [])
        
        # Adiciona os anos à lista de anos
        for estacao in estacoes:
            lista_estacoes.insert(END, estacao)

    # Define a janela principal
    root = Tk()
    root.title("Estações Meteorológicas")

    # Frame para conter os widgets
    frame = Frame(root)
    frame.grid(row=0, column=0, sticky=(W,E,N,S))

    messageMain = Label(frame, text="Interface de consulta de dados as estações meteorológicas brasileiras")
    messageMain.grid(row=0,column=1, pady=10, sticky=W)
    
    # Label da combobox
    labelComboboxAnos = Label(frame, text=" Selecione o ano:")
    labelComboboxAnos.grid(row=1, column=0)
    
    # Combobox para selecionar o ano
    anos_estacoes_combobox = Combobox(frame, values=list(estacoes_meteorologicas.keys()))
    anos_estacoes_combobox.grid(row=2, column=0, padx=5, pady=5)
    anos_estacoes_combobox.bind("<<ComboboxSelected>>", selecionar_estacao)

    
    # Label da Listbox
    labelListboxEstacoes = Label(frame, text=" Selecione a estação:")
    labelListboxEstacoes.grid(row=1, column=1)
    
    # Lista para exibir as estações de medições
    lista_estacoes = Listbox(frame)
    lista_estacoes.grid(row=2, column=1, padx=5, pady=5)

    # Roda o loop principal da aplicação
    root.mainloop()