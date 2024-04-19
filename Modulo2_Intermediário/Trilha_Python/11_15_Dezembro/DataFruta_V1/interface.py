from . recursos import  limpaTela,pause
from datetime import datetime
import locale

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
    
        print("\n\t======= DATAFRUTA =======\n\n")
        print("\t[1] - INCLUIR UM NOME DA LISTA DE NOMES")
        print("\t[2] - INCLUIR SALÁRIO NA LISTA DE SALÁRIOS")
        print("\t[3] - INCLUIR DATA NA LISTA DE DATAS")
        print("\t[4] - INCLUIR IDADE NA LISTA DE IDADES")
        print("\t[5] - PERCORRER AS LISTAS DE NOME E SALÁRIOS")
        print("\t[6] - CALCULAR O VALOR DA FOLHA COM UM REAJUSTE DE 10%")
        print("\t[7] - MODIFICAR OS DIAS DE DATAS ANTERIORES A 2019")
        print("\t[8] - MOSTRAR RELATÓRIO (MEDIANA, MAIOR E MENOR)")
        print("\t[9] - MOSTRAR RELATÓRIO COM SALÁRIOS ALEATÓRIOS (MEDIANA, MAIOR E MENOR)")
        print("\t[10] - MOSTRAR RELATÓRIO COM IDADES ALEATÓRIAS(MEDIANA, MAIOR E MENOR)")
        print("\t[11] - INCLUIR NOTAS")
        print("\t[0] - SAIR")
         
        try:
           opcao = int(input("\tENTRADA -> "))
        except:
            limpaTela()
            print("\n\tOps, valor inválido! Informe apenas as opções disponíveis...")
            pause()
            
  
        if(opcao < 0 or opcao > 11):
            limpaTela()
            print("\n\tOps, opção inválida! Tente novamente...")
            pause()
        else:
            return opcao
            
            
