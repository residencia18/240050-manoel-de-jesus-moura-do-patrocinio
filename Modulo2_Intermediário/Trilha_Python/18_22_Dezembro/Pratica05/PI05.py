import numpy as np
import pandas as pd

def main():
    # Questão 1
    
    identificador = ["tic18Py07999","tic18Py07497","tic18Py08196","tic18Py07900"]
    idade = [24,25,28,24]
    formacao = [1,1,3,0]
    formaçãoGeral = [1,0,1,None]
    formacaoEspecifica = ["Computação","Engenharia","Computação",None]
    andamentoGraduacao = [99.9,88.5,None,None]
    tempoFormacao = [None,None,4,None]
    experienciaPrevia = [True,False,True,False]

    # Questão 2
    index = pd.Index(identificador, name="ID")
    alunos_idade = pd.Series(idade, index=index, name="idades")
    alunos_formacao = pd.Series(formacao, index=index, name="formação")
    alunos_formaçãoGeral = pd.Series(formaçãoGeral, index=index, name="F. Geral")
    alunos_formacaoEspecifica = pd.Series(formacaoEspecifica, index=index, name="F. Especifica")
    alunos_andamentoGraduacao = pd.Series(andamentoGraduacao, index=index, name="A. Graduação")
    alunos_tempoFormacao = pd.Series(tempoFormacao, index=index, name="T. Formação")
    alunos_experienciaPrevia = pd.Series(experienciaPrevia, index=index, name="Exp. Previa")

    # Questão 2.1
    
    idade_media = alunos_idade.mean()
    
    membros_mais_jovens = alunos_idade[alunos_idade == alunos_idade.min()]

    membros_mais_velhos = alunos_idade[alunos_idade == alunos_idade.max()]
    
    print("\n\nA média das idades: ", idade_media)
    print("\nMembro(s) mais jovem(s): ")
    print(membros_mais_jovens)
    print("\nMembro(s) mais velho(s): ")
    print(membros_mais_velhos)
   
    # Questão 2.2
   
    formacao_descricao = {
        0: 'Formação técnica',
        1: 'Formação técnica graduação em andamento',
        2: 'Graduação em andamento',
        3: 'Graduação concluída'
    } 
    # conta a ocorrência dos valores referente a formação
    contagem_formacao = alunos_formacao.value_counts()

    # Exibindo a contagem
    print("\n\nOs membros são predominantemente do tipo de formação: ", formacao_descricao[contagem_formacao.index[0]])

    # Questão 2.3

    contagem_formacaoGeral = alunos_formaçãoGeral.value_counts()
    print("\n\nOs membros da equipe são predominantemente da categoria Geral: ", "Engenharia" if contagem_formacaoGeral[contagem_formacaoGeral.index[0]] == 0 else "Computação")


    # Questão 3
    alunos_python_dataFrames = pd.DataFrame({
        'idades':alunos_idade,
        'formação':alunos_formacao,
        'F. Geral':alunos_formaçãoGeral,
        'F. Especifica':alunos_formacaoEspecifica,
        'A. Graduação':alunos_andamentoGraduacao,
        'T. Formação':alunos_tempoFormacao,
        'Exp. Previa':alunos_experienciaPrevia,
    },index=index)
    
    print("\n\n***** QUESTÃO 3: PRATICA COM DATAFRAMES *****\n\n")
    print(alunos_python_dataFrames)
    
    idade_media_2 = alunos_python_dataFrames['idades'].mean()
    
    membros_mais_jovens_2 = alunos_python_dataFrames[alunos_python_dataFrames['idades'] == alunos_python_dataFrames['idades'].min()]

    membros_mais_velhos_2 = alunos_python_dataFrames[alunos_python_dataFrames['idades'] == alunos_python_dataFrames['idades'].max()]
    
    print("\n\nA média das idades: ", idade_media_2)
    print("\nMembro(s) mais jovem(s): ")
    print(membros_mais_jovens_2)
    print("\nMembro(s) mais velho(s): ")
    print(membros_mais_velhos_2)
    
    #Questão 04
    print("\n\n***** QUESTÃO 4: PRATICA COM MultiIndex *****\n\n")
    
    # Dados para a trilha DotNet
    identificador_t2 = ["tic18Dot07989","tic18Dot07487","tic18Dot08186","tic18Dot07902"]
    idade_t2 = [35,37,38,20]
    formacao_t2 = [1,1,3,0]
    formaçãoGeral_t2 = [1,0,1,None]
    formacaoEspecifica_t2 = ["Computação","Engenharia","Computação",None]
    andamentoGraduacao_t2 = [99.9,88.5,None,None]
    tempoFormacao_t2 = [None,None,4,None]
    experienciaPrevia_t2 = [True,False,True,False]
    
    index_t2 = pd.Index(identificador_t2, name="ID")
    alunos_Dotnet_dataFrames = pd.DataFrame({
        'idades':idade_t2,
        'formação':formacao_t2,
        'F. Geral':formaçãoGeral_t2,
        'F. Especifica':formacaoEspecifica_t2,
        'A. Graduação':andamentoGraduacao_t2,
        'T. Formação':tempoFormacao_t2,
        'Exp. Previa':experienciaPrevia_t2,
    },index=index_t2)
    
    # Combinando ambos os DataFrames em um único DataFrame com MultiIndex
    alunos_multiIndex = pd.concat({'Python': alunos_python_dataFrames, 'DotNet': alunos_Dotnet_dataFrames})

    # Exibindo o DataFrame final
    print(alunos_multiIndex)
if __name__ == "__main__":
    main()