import os
import platform


formacao_tipos = {
    0: 'Formação técnica',
    1: 'Formação técnica graduação em andamento',
    2: 'Graduação em andamento',
    3: 'Graduação concluída'
} 
formacao_geral ={
    0: 'Engenharia',
    1: 'Computação'
} 
formacao_especifica = {
    0: 'Engenharia Elétrica',
    1: 'Engenharia Civil',
    2: 'ADS',
    3: 'Ciência da computação'
} 

TrilhasNomes = ['Python','.NET','Java']
def pause():
  input("\t\nPressione Enter para continuar...\n")
  
def limpaTela():
  sistema_operacional = platform.system().lower()

  if sistema_operacional == "windows":
    os.system("cls")
  elif sistema_operacional == "linux":
    os.system("clear")
  else:
    print("Sistema operacional não suportado para limpar a tela.")

from datetime import datetime

def calcular_idade():
    # Solicitar a data de aniversário do usuário
    data_aniversario_str = input("Digite sua data de aniversário (no formato DD/MM/AAAA): ")

    # Converter a string para um objeto datetime
    try:
        data_aniversario = datetime.strptime(data_aniversario_str, "%d/%m/%Y")
    except ValueError:
        print("Formato inválido. Certifique-se de digitar a data no formato DD/MM/AAAA.")
        return

    # Obter a data atual
    data_atual = datetime.now()

    # Calcular a diferença entre a data atual e a data de aniversário
    diferenca = data_atual - data_aniversario

    # Calcular a idade em anos
    idade = diferenca.days // 365
    ano_nascimento = data_aniversario.year
    return (idade,ano_nascimento)
