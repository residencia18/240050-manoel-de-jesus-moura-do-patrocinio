from . recursos import  formacao_tipos,formacao_especifica,formacao_geral,TrilhasNomes
import numpy as np
from datetime import datetime
import pandas as pd
import os
class Residente():
    

    def __init__(self,nome, trilha, cpf, ano_nascimento, idade, formacao, area_geral=None, area_especifica=None, andamento_graduacao=None, tempo_formado=None, experiencia_programacao=False):
        # Verificações de tipos
        if (not isinstance(cpf, str)
            or not isinstance(nome, str)
            or not isinstance(trilha, str)
            or not isinstance(ano_nascimento, str)
            or not isinstance(idade, (int, type(None)))
            or not isinstance(formacao, (int, type(None)))
            or not isinstance(area_geral, (int, type(None)))
            or not isinstance(area_especifica, (int, type(None)))
            or not isinstance(andamento_graduacao, (float, type(None)))
            or not isinstance(tempo_formado, (int, type(None)))
            or not isinstance(experiencia_programacao, bool)
        ):
            raise TypeError("Tipos de dados incorretos.")

        # Verificações de intervalos
        if (idade < 0 or idade > 100 
            or formacao not in [0, 1, 2, 3] 
            or (area_geral is not None and area_geral not in [0, 1])
            or (area_especifica is not None and area_especifica not in [0, 1, 2, 3])
            or trilha not in TrilhasNomes
            or (andamento_graduacao is not None and (andamento_graduacao < 0.0 or andamento_graduacao > 100.0))
            ):
            raise ValueError("Valores fora dos intervalos esperados.")
        
        
        self.nome = nome
        self.trilha = trilha
        self.cpf = cpf
        self.ano_nascimento = ano_nascimento
        self.idade = idade
        self.formacao =  formacao_tipos[formacao]
        self.area_geral = formacao_geral[area_geral] if area_geral is not None else None
        self.area_especifica =  formacao_especifica[area_especifica] if area_especifica is not None else None
        self.andamento_graduacao = andamento_graduacao if andamento_graduacao is not None else None
        self.tempo_formado = tempo_formado if tempo_formado is not None else None
        self.experiencia_programacao = experiencia_programacao
        
        # Verificar se a idade fornecida está correta
        if idade is not None:
            if self.calcular_idade() != idade:
                raise TypeError("A idade informada não coincide com o ano de nascimento.")

        self.identificador = self.gerar_identificador()

    def gerar_identificador(self):
        if self.trilha in TrilhasNomes:
            prefixo_trilha = f"tic18{self.trilha[:3]}"
        else:
            print(f"Trilha não reconhecida: {self.trilha}")
            return None

        identificador = f"{prefixo_trilha}{self.cpf[:3]}{self.ano_nascimento[-2:]}"

        return identificador
    
    def calcular_idade(self):
        data_atual = datetime.now()
        ano_atual = data_atual.year
        return ano_atual - int(self.ano_nascimento)
    
    def __str__(self):
        print( f"Identificador: {self.identificador}\nNome: {self.nome}\nIdade: {self.idade}\nFormação: {self.formacao}\nÁrea Geral: {self.area_geral}\nÁrea Específica: {self.area_especifica}\nAndamento Graduação: {self.andamento_graduacao}\nTempo Formado: {self.tempo_formado}\nExperiência em Programação: {self.experiencia_programacao}")

class Trilha:
    
    def __init__(self, nome_trilha):
        if nome_trilha not in TrilhasNomes :
            raise ValueError("Trilha inválida ou inexistente ")
        
        self.nome_trilha = nome_trilha
        self.dados_residentes = pd.DataFrame(columns=["Nome","Idade","Formacao", "Area_Geral", "Area_Especifica", "Andamento_Graduacao", "Tempo_Formado", "Experiencia_Programacao"])

    def adicionar_residente(self, residente):
        # Verificar pelo o identificador se o residente já existe na trilha
        if residente.identificador in self.dados_residentes.index:
            print(f" O residente {residente.nome}, de identificador {residente.identificador} já existe na trilha.")
            return

        # Adicionar residente ao DataFrame
        index = pd.Index([residente.identificador], name="ID")
        
        
        # cria um DataFrame temporário
        novo_residente = pd.DataFrame({
            "Nome": [residente.nome],
            "Idade": [residente.idade],
            "Formacao": [residente.formacao],
            "Area_Geral": [residente.area_geral],
            "Area_Especifica": [residente.area_especifica],
            "Andamento_Graduacao": [residente.andamento_graduacao],
            "Tempo_Formado": [residente.tempo_formado],
            "Experiencia_Programacao": [residente.experiencia_programacao],
            "Trilha": self.nome_trilha
        }, index=index)

        # Se estiver vazio, atribuí diretamente o novo DataFrame.
        if self.dados_residentes.empty:
            self.dados_residentes = novo_residente
        else:
            self.dados_residentes = pd.concat([self.dados_residentes, novo_residente])


    def __str__(self):
        print(f"\nDados na trilha {self.nome_trilha}:\n{self.dados_residentes}")

class Residencia:
    def __init__(self, nome_turma, quantidade_alunos):
        if not isinstance(nome_turma, str) or not isinstance(quantidade_alunos, int):
            raise TypeError("Tipos de dados incorretos.")
        
        if quantidade_alunos < 1 or quantidade_alunos > 31:
            raise ValueError("Quantidade de alunos inválida. A turma precisar ter entre 1 a 31 residentes")

        self.nome_turma = nome_turma
        self.quantidade_alunos = quantidade_alunos
        self.trilhas = []  # Lista para armazenar objetos da classe Trilha

    
    def adicionar_trilha(self, nome_trilha):
        nova_trilha = Trilha(nome_trilha)
        self.trilhas.append(nova_trilha)

    def adicionar_residente(self, nome_trilha, residente):
        # Procura a trilha pelo nome
        for trilha in self.trilhas:
            if trilha.nome_trilha == nome_trilha:
                trilha.adicionar_residente(residente)
                return
        print(f"Trilha {nome_trilha} não encontrada na turma {self.nome_turma}.")

    def mostrar_info_turma(self):
        print(f"\nInformações da turma: {self.nome_turma} \n")
        for trilha in self.trilhas:
            trilha.__str__()
    
    def salvar_dados_turma_csv(self):
        # criar um objeto(dicionário) para agrupa od dados
        dados_turma = {"Nome da Turma": [], "Quantidade de Alunos": [], "Nome da Trilha": [], "Dados dos Residentes": []}

        for trilha in self.trilhas:
            dados_turma["Nome da Turma"].append(self.nome_turma)
            dados_turma["Quantidade de Alunos"].append(self.quantidade_alunos)
            dados_turma["Nome da Trilha"].append(trilha.nome_trilha)
            dados_turma["Dados dos Residentes"].append(trilha.dados_residentes)

        df_turma = pd.DataFrame(dados_turma)

        # Cria um diretório para salvar os arquivos CSV, se não existir
        if not os.path.exists("dados_turmas_csv"):
            os.makedirs("dados_turmas_csv")

        # Salva o DataFrame em um arquivo CSV
        arquivo_csv = f"dados_turmas_csv/{self.nome_turma}_dados.csv"
        df_turma.to_csv(arquivo_csv, index=False)

        print(f"\nDados da turma {self.nome_turma} salvos em {arquivo_csv}.")
    # @staticmethod porque não faz referência a instâncias específicas da classe Residencia. 
    @staticmethod
    def carregar_dados_turma_csv(nome_turma):
        arquivo_csv = f"dados_turmas_csv/{nome_turma}_dados.csv"
        
        try:
            # Carrega o arquivo CSV em um DataFrame
            df_turma = pd.read_csv(arquivo_csv)

            # Exibe os dados carregado            print(df_turma)

            print(f"Dados da turma {nome_turma} carregados:")
            print(df_turma)
            print(f"\n\nDetalhes da turma {nome_turma}:")
            print(df_turma.describe())
            
            

            return df_turma
        except FileNotFoundError:
            print(f"Arquivo CSV {arquivo_csv} não encontrado.")
            return None




# def salvar_dados_turma_csv(self):
#         # criar um objeto(dicionário) para agrupa od dados
#         dados_turma = {"Nome da Turma": [], "Quantidade de Alunos": [], "Nome da Trilha": [], "Nome do Residente": [], "Idade": [], "Formacao": [], "Area_Geral": [], "Area_Especifica": [], "Andamento_Graduacao": [], "Tempo_Formado": [], "Experiencia_Programacao": []}

#         for trilha in self.trilhas:
#             for idx, residente in trilha.dados_residentes.iterrows():
#                 dados_turma["Nome da Turma"].append(self.nome_turma)
#                 dados_turma["Quantidade de Alunos"].append(self.quantidade_alunos)
#                 dados_turma["Nome da Trilha"].append(trilha.nome_trilha)
#                 dados_turma["Nome do Residente"].append(residente["Nome"])
#                 dados_turma["Idade"].append(residente["Idade"])
#                 dados_turma["Formacao"].append(residente["Formacao"])
#                 dados_turma["Area_Geral"].append(residente["Area_Geral"])
#                 dados_turma["Area_Especifica"].append(residente["Area_Especifica"])
#                 dados_turma["Andamento_Graduacao"].append(residente["Andamento_Graduacao"])
#                 dados_turma["Tempo_Formado"].append(residente["Tempo_Formado"])
#                 dados_turma["Experiencia_Programacao"].append(residente["Experiencia_Programacao"])

#         df_turma = pd.DataFrame(dados_turma)

#         # Cria um diretório para salvar os arquivos CSV, se não existir
#         if not os.path.exists("dados_turmas_csv"):
#             os.makedirs("dados_turmas_csv")

#         # Salva o DataFrame em um arquivo CSV
#         arquivo_csv = f"dados_turmas_csv/{self.nome_turma}_dados.csv"
#         df_turma.to_csv(arquivo_csv, index=False)

#         print(f"Dados da turma {self.nome_turma} salvos em {arquivo_csv}.")

    