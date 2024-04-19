from . classes import ListaNomes,ListaSalarios, ListaDatas, ListaIdades, ListaNotas
from . recursos import  limpaTela,pause
from . interface import menu
import timeit
import numpy as np


def main():
    nomes = ListaNomes()
    salarios = ListaSalarios()
    datas = ListaDatas()
    idades = ListaIdades()
    notas = ListaNotas()
    listaDeLista = []
    while True:
        
        opcao = menu()
        
        match opcao:
           
            case 1:
                nomes.entradaDeDados()  
                listaDeLista.append(nomes)
                
                nomes.listarEmOrdem()
                
            case 2:
                salarios.entradaDeDados()
                listaDeLista.append(salarios)
                
                salarios.listarEmOrdem()    
            case 3:
                datas.entradaDeDados()
                listaDeLista.append(datas)
                
                datas.listarEmOrdem()
            case 4:
                idades.entradaDeDados()
                listaDeLista.append(idades)
                
                idades.listarEmOrdem()
                pass   
            case 5:
                nomes.percorreListaDeNomesESalarios(nomes, salarios)
            case 6:
                custo_folha_atual = salarios.reajustar_Salarios()
                print("\tCusto total da folha de pagamento após o reajuste: {:.2f}".format(custo_folha_atual))
                pause()
            case 7:
                datas_modificadas = datas.modificar_datas_anteriores_2019() 
                
                limpaTela()
                print("\n\t=========== DATAS DEPOIS DA MODIFICAÇÃO ===========\n")  

                for data_modificada in datas_modificadas:
                    print("\tData modificada: {}".format(data_modificada))
                
                pause()
            case 8:
                limpaTela()
                if not listaDeLista:
                    print("\nA lista de lista está vazia. Não é possível exibir os relatórios no memento.\n")
                    pause()
                else:                             
                    print("\n\t=========== RELATÓRIO DOS DADOS ===========\n")  

                    for lista in listaDeLista:
        
                        menor = lista.mostraMenor()
                        maior = lista.mostraMaior()
                        mediana = lista.mostraMediana()
                    
                        print("\tMENOR VALOR:\t{}".format(menor))
                        print("\tMAIOR VALOR:\t{}".format(maior))
                        print("\tA MEDIANA :\t{}".format(mediana))
                        print("\t___________________\n") 
                    pause()
            case 9:
              print("\n\t=========== RELATÓRIO DE SALÁRIO COM DADOS ALEATÓRIOS ===========\n")  
                
            
              lista = salarios.geraListaSalario(5000)
              salariosAleatorios = ListaSalarios(lista)  

              tempoMediana = timeit.timeit(lambda:salariosAleatorios.mostraMediana(),number=1)
              print(f"\tTempo de execução do calculo da mediana: {tempoMediana}\n")

              print(f"\tMaior: {salariosAleatorios.mostraMaior():.2f}")              
              tempoMaior = timeit.timeit(lambda:salariosAleatorios.mostraMaior(),number=1)
              print(f"\tTempo de execução do calculo do maior : {tempoMaior}\n")
              
              print(f"\tMenor: {salariosAleatorios.mostraMenor():.2f}")              
              tempoMenor = timeit.timeit(lambda:salariosAleatorios.mostraMenor(),number=1)
              print(f"\tTempo de execução do calculo do menor : {tempoMenor}")
              
              print("\n\tRELATÓRIO USANDO NUMPY ===========\n")  
              
              novoObjetoSalario = ListaSalarios()
              ndarray = novoObjetoSalario.geraListaSalarioNumpy(5000)

              print(f"\tMediana: {np.median(ndarray):.2f}")
              tempoMediana = timeit.timeit(lambda:np.median(ndarray),number=1)
              print(f"\tTempo de execução do calculo da mediana: {tempoMediana}\n")
              
              print(f"\tMaior: {np.max(ndarray):.2f}")              
              tempoMaior = timeit.timeit(lambda:np.max(ndarray),number=1)
              print(f"\tTempo de execução do calculo do maior : {tempoMaior}\n")
              
              print(f"\tMenor: {np.min(ndarray):.2f}")              
              tempoMenor = timeit.timeit(lambda:np.min(ndarray),number=1)
              print(f"\tTempo de execução do calculo do menor : {tempoMenor}")
              
              pause()
            case 10:
              print("\n\t=========== RELATÓRIO DE IDADES COM DADOS ALEATÓRIOS ===========\n")  
                
              listaRandomIdades = idades.geraListaIdade(5000,18,70)
              idadesAleatorias = ListaIdades(listaRandomIdades)  
            
              
              tempoMediana = timeit.timeit(lambda:idadesAleatorias.mostraMediana(),number=1)
              print(f"\tTempo de execução do calculo da mediana: {tempoMediana}\n")
              
              print(f"\tMaior: {idadesAleatorias.mostraMaior():.2f}")              
              tempoMaior = timeit.timeit(lambda:idadesAleatorias.mostraMaior(),number=1)
              print(f"\tTempo de execução do calculo do maior : {tempoMaior}\n")
              
              print(f"\tMenor: {idadesAleatorias.mostraMenor():.2f}")              
              tempoMenor = timeit.timeit(lambda:idadesAleatorias.mostraMenor(),number=1)
              print(f"\tTempo de execução do calculo do menor : {tempoMenor}\n")
              
              
              print("\n\tRELATÓRIO USANDO NUMPY ===========\n")  
            
              novoObjetoIdade = ListaIdades()
              ndarrayIdades = novoObjetoIdade.geraListaIdadeNumpy(5000,18,70)
            #   ndarrayIdades = np.array(listaRandomIdades)

              print(f"\tMediana: {np.median(ndarrayIdades):.2f}")
              tempoMediana = timeit.timeit(lambda:np.median(ndarrayIdades),number=1)
              print(f"\tTempo de execução do calculo da mediana: {tempoMediana}\n")
              
              print(f"\tMaior: {np.max(ndarrayIdades):.2f}")              
              tempoMaior = timeit.timeit(lambda:np.max(ndarrayIdades),number=1)
              print(f"\tTempo de execução do calculo do maior : {tempoMaior}\n")
              
              print(f"\tMenor: {np.min(ndarrayIdades):.2f}")              
              tempoMenor = timeit.timeit(lambda:np.min(ndarrayIdades),number=1)
              print(f"\tTempo de execução do calculo do menor : {tempoMenor}")
              
              pause()

            case 11:
                notas.entradaDeDados()  
                listaDeLista.append(notas)
                
                notas.listarEmOrdem()
                
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
