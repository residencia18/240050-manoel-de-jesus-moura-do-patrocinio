from . recursos import  limpaTela,pause
from abc import ABC, abstractmethod
import copy
import random
import numpy as np
from datetime import date


class Data:
    
    def __init__(self, dia = 1, mes = 1, ano = 2000):
        if dia < 1 or dia > 31:
            raise ValueError("Dia inválido")
        if mes < 1 or mes > 12:
            raise ValueError("Mês inválido")
        if ano < 1950 or ano > 2100:
            raise ValueError("Ano inválido")
        self.__dia = dia
        self.__mes = mes
        self.__ano = ano
        
    @property
    def year(self):
        return self.__ano
    
    @year.setter
    def year(self, ano):
        if ano < 1950 or ano > 2100:
            raise ValueError("Ano inválido")
        self.__ano = ano

    @property
    def dia(self):
        return self.__dia
    
    @dia.setter
    def dia(self, dia):
        if dia < 1 or dia > 31:
            raise ValueError("Dia inválido")
        self.__dia = dia

    @property
    def mes(self):
        return self.__mes
    
    @mes.setter
    def mes(self, mes):
        if mes < 1 or mes > 12:
            raise ValueError("Mês inválido")
        self.__mes = mes

    @property
    def ano(self):
        return self.__ano
    
    @ano.setter
    def ano(self, ano):
        if ano < 1950 or ano > 2100:
            raise ValueError("Ano inválido")
        self.__ano = ano
    
    def __str__(self):
        return "{}/{}/{}".format(self.__dia, self.__mes, self.__ano)

    def __eq__(self, outraData):
        return  self.__dia == outraData.__dia and \
                self.__mes == outraData.__mes and \
                self.__ano == outraData.__ano
    
    def __lt__(self, outraData):
        if self.__ano < outraData.__ano:
            return True
        elif self.__ano == outraData.__ano:
            if self.__mes < outraData.__mes:
                return True
            elif self.__mes == outraData.__mes:
                if self.__dia < outraData.__dia:
                    return True
        return False
    
    def __gt__(self, outraData):
        if self.__ano > outraData.__ano:
            return True
        elif self.__ano == outraData.__ano:
            if self.__mes > outraData.__mes:
                return True
            elif self.__mes == outraData.__mes:
                if self.__dia > outraData.__dia:
                    return True
        return False

class AnaliseDados(ABC): 

    @abstractmethod
    def __init__(self, tipoDeDados):
        self.__tipoDeDados = tipoDeDados

    @abstractmethod
    def entradaDeDados(self):
        pass

    @abstractmethod
    def mostraMediana(self):
        pass
    
    @abstractmethod
    def mostraMedianaSuperior(self):
        pass
    
    @abstractmethod
    def mostraMedianaInferior(self):
        pass
    
    @abstractmethod
    def mostraMenor(self):
        pass

    @abstractmethod
    def mostraMaior(self):
        pass
    
    @abstractmethod
    def listarEmOrdem(self):
        pass

class ListaNomes(AnaliseDados):
    
    def __init__(self):
        super().__init__(type("String"))
        self.__lista = []
         

    def entradaDeDados(self):

        limpaTela() 
        print("\n\t=========== CADASTRO DE NOMES ===========\n")
        
        while True:
            try:
                quantElementos = int(input("\n\tQuantos elementos vão existir na lista: "))
                break  # Se a conversão para int for bem-sucedida, sai do loop
            except ValueError:
                print("\tPor favor, digite um número inteiro válido.")
                pause() 
                limpaTela() 
        
        for i in range(quantElementos):
            while True:
                limpaTela()
                elemento = input("\n\tDigite o elemento {}: ".format(i + 1))
                if elemento.isalpha():
                    self.__lista.append(elemento)
                    break
                else:
                    limpaTela()
                    print("\tPor favor, digite apenas letras.")
                    pause() 
                    limpaTela() 
        pass

    def mostraMediana(self):
       
        if not self.__lista:
            print("A lista está vazia. Não é possível calcular a mediana.")
            return

        lista_ordenada = sorted(self.__lista)
        tamanho = len(lista_ordenada)
        
        if tamanho % 2 == 0:
            meio1 = lista_ordenada[tamanho // 2 - 1]
            meio2 = lista_ordenada[tamanho // 2]
            mediana = meio1
        else:
            mediana = lista_ordenada[tamanho // 2]

        return mediana  # retorna o primeiro valor na mediana
       
    def mostraMedianaSuperior(self):
        if not self.__lista:
            print("A lista está vazia. Não é possível calcular a mediana superior.")
            return

        lista_ordenada = sorted(self.__lista)
        tamanho = len(lista_ordenada)
        
        if tamanho % 2 == 0:
            meio1 = lista_ordenada[tamanho // 2 - 1]
            meio2 = lista_ordenada[tamanho // 2]
            mediana_superior = meio2
        else:
            mediana_superior = lista_ordenada[tamanho // 2]

        return mediana_superior  # retorna o segundo valor na mediana
    def mostraMedianaInferior(self):
        if not self.__lista:
            print("A lista está vazia. Não é possível calcular a mediana inferior.")
            return

        lista_ordenada = sorted(self.__lista)
        tamanho = len(lista_ordenada)
        
        if tamanho % 2 == 0:
            meio1 = lista_ordenada[tamanho // 2 - 1]
            meio2 = lista_ordenada[tamanho // 2]
            mediana_inferior = meio1
        else:
            mediana_inferior = lista_ordenada[tamanho // 2]

        return mediana_inferior  # retorna o primeiro valor na mediana
        

    def mostraMenor(self):

        if not self.__lista:
            print("A lista está vazia. Não é possível calcular o menor elemento.")
            return
        
        menor = self.__lista[0]
        for elemento in self.__lista:
            if elemento < menor:
                menor = elemento
        return menor

    def mostraMaior(self):
       
        
        if not self.__lista:
            print("A lista está vazia. Não é possível calcular o maior elemento.")
            return
        
        maior = self.__lista[0] 
        for elemento in self.__lista:
            if elemento > maior:
                maior = elemento
        return maior 

    def listarEmOrdem(self):
    
        limpaTela()
        if not self.__lista:
            print("A lista está vazia. Não é possível ordenar.")
            return

        lista_ordenada = sorted(self.__lista)
        print("\n\t=========== LISTA DE NOMES EM ORDEM ALFABÉTICA ===========\n")
        for elemento in lista_ordenada:
            print(f"\tNome: {elemento}")
        pause()
        
        pass
    
    def percorreListaDeNomesESalarios(self, outras_nomes, outras_salarios):
        
        if not self.__lista:
            limpaTela() 
            print("\n\tA lista está vazia. Não é possível percorrer a lista de nomes e salários.")
            pause()
            return
        
        limpaTela()
        print("\n\t=========== LISTA DE NOMES E SALÁRIOS ===========\n")
        for nome, salario in zip(self.__lista, outras_salarios._ListaSalarios__lista):
            print("\tNome: {}, Salário: {:.2f}".format(nome, salario))
        pause()
    
    def __str__(self):
        pass
	
class ListaDatas(AnaliseDados):
        
    def __init__(self):
        super().__init__(type(Data))
        self.__lista = []        
    
    def entradaDeDados(self):

        limpaTela()
        print("\n\t=========== CADASTRO DE DATAS ===========\n")
        
        while True:
            try:
                quantElementos = int(input("\n\tQuantos elementos vão existir na lista: "))
                break  # Se a conversão para int for bem-sucedida, sai do loop
            except ValueError:
                limpaTela()
                print("\tPor favor, digite um número inteiro válido.")
                pause() 
                limpaTela() 
        
        for i in range(quantElementos):    
            while True:
                try:
                    print("\n\tDigite o elemento {}:".format(i + 1))
                    dia =  random.randint(1, 10)
                    mes = int(input("\tMês: "))
                    ano = int(input("\tAno: "))
            
                    # Verifica se a data é válida
                    data = Data(dia, mes, ano)
            
                    # Se chegou aqui, a data é válida, então podemos adicionar à lista
                    self.__lista.append(data)
                    print(f"\n\tData válida: {data}")
            
                    # Sai do loop se a entrada foi válida
                    break

                except ValueError as e:
                    limpaTela() 
                    print("\n\tOps, data invalida!\n\tPor favor, digite uma data válida.")
                    pause()
                    limpaTela() 
        pass
    
    
    def geraListaDatas(self, n , iMin = 18, iMax = 65):
        novaLista = []
        for i in range(n):    
            while True:
                try:
                    dia =  random.randint(1, 31)
                    mes =  random.randint(1, 12)                    
                    LiMin = date.today().year - iMin
                    LiMax = date.today().year - iMax
                    ano =  random.randint(LiMax,LiMin )
                    # Verifica se a data é válida
                    data = Data(dia, mes, ano)
            
                    # Se chegou aqui, a data é válida, então podemos adicionar à lista
                    novaLista.append(data)
                    print(f"\n\tData válida: {data}")
            
                    # Sai do loop se a entrada foi válida
                    break

                except ValueError as e:
                    # limpaTela() 
                    print("\n\tOps, foi gerada uma data invalida!\n\t")
                    pause()
                    limpaTela() 
        return novaLista
        
    def mostraMediana(self):
    
        mediana = self.calcula_data_mediana()
        
        return mediana    
     
    def mostraMedianaSuperior(self):
        
        if not self.__lista:
            print("A lista de datas está vazia. Não é possível calcular a mediana superior.")
            return None

        lista_ordenada = sorted(self.__lista)
        tamanho = len(lista_ordenada)

        if tamanho % 2 != 0:
            mediana_superior = lista_ordenada[tamanho // 2]
            print(f"\n\tA lista de datas tem um número ímpar de elementos. A mediana superior é: {mediana_superior}")
        else:
            meio1 = lista_ordenada[tamanho // 2 - 1]
            meio2 = lista_ordenada[tamanho // 2]
            mediana_superior = Data()  # Criar uma nova instância de Data para armazenar a mediana
            mediana_superior = meio2
        return mediana_superior
    def mostraMedianaInferior(self):
        
        if not self.__lista:
            print("A lista de datas está vazia. Não é possível calcular a mediana superior.")
            return None

        lista_ordenada = sorted(self.__lista)
        tamanho = len(lista_ordenada)

        if tamanho % 2 != 0:
            mediana_inferior = lista_ordenada[tamanho // 2]
            print(f"\n\tA lista de datas tem um número ímpar de elementos. A mediana inferior é: {mediana_inferior}")
        else:
            meio1 = lista_ordenada[tamanho // 2 - 1]
            meio2 = lista_ordenada[tamanho // 2]
            mediana_inferior = Data()  # Criar uma nova instância de Data para armazenar a mediana
            mediana_inferior = meio1
        return mediana_inferior
     
    def mostraMenor(self):
    
        if not self.__lista:
            print("A lista está vazia. Não é possível calcular o menor elemento.")
            return
        
        menor = self.__lista[0]
        for elemento in self.__lista:
            if elemento < menor:
                menor = elemento
        return menor
        
        
    
    def mostraMaior(self):
  
        if not self.__lista:
            print("A lista está vazia. Não é possível calcular o maior elemento.")
            return
        
        maior = self.__lista[0]
        for elemento in self.__lista:
            if elemento > maior:
                maior = elemento
        return maior
    
    def calcula_data_mediana(self):
        
        if not self.__lista:
            print("A lista de datas está vazia. Não é possível calcular a mediana.")
            return None

        lista_ordenada = sorted(self.__lista)
        tamanho = len(lista_ordenada)

        if tamanho % 2 != 0:
            mediana = lista_ordenada[tamanho // 2]
            print(f"\n\tA lista de datas tem um número ímpar de elementos. A mediana é: {mediana}")
        else:
            meio1 = lista_ordenada[tamanho // 2 - 1]
            meio2 = lista_ordenada[tamanho // 2]
            mediana = Data()  # Criar uma nova instância de Data para armazenar a mediana
            if meio1 < meio2:
                mediana = meio1
            else:
                mediana = meio2
                print(f"\n\tA lista de datas tem um número par de elementos. A mediana é: {mediana}")

        return mediana
    
    def listarEmOrdem(self):
  
        lista_ordenada = sorted(self.__lista)
    
        limpaTela()
        print("\n\t=========== LISTA DE DATAS ===========\n")
    
        for i, data in enumerate(lista_ordenada, start=1):
            print(f"\tData {i}: {data}")
        pause()
    
    def modificar_datas_anteriores_2019(self):
        
        if not self.__lista:
            limpaTela()
            print("\n\tA lista está vazia. Não é possível modificar as datas.")
            pause()
            return
        
        datas_modificadas = list(filter(lambda x: x is not None, map(lambda data: self.modificar_data(data), self.__lista.copy())))
        return datas_modificadas    

    def modificar_data(self, data):
        if data.ano < 2019:
            # Criar uma cópia do objeto Data para evitar modificar a lista original
            data = copy.copy(data)
            data.dia = 1
        return data

    def __str__(self):
        pass

class ListaSalarios(AnaliseDados):
 
    def __init__(self, lista_floats=None):
        super().__init__(type(float))

        if lista_floats is None:
            self.__lista = []
        else:
            self.__lista = lista_floats[:]      

    def entradaDeDados(self):

        limpaTela()
        print("\n\t=========== CADASTRO DE SALÁRIOS ===========\n")
        
        while True:
            try:
                quantElementos = int(input("\n\tQuantos elementos vão existir na lista: "))
                break  # Se a conversão para int for bem-sucedida, sai do loop
            except ValueError:
                print("\tPor favor, digite um número inteiro válido.")
                pause() 
                limpaTela()
        
        for i in range(quantElementos):
            while True:
                try:
                    print("\n\tDigite o elemento {}:".format(i + 1))
                    elemento = float(input("\tNúmero: "))
            
                    # Se chegou aqui, o número é válido, então podemos adicionar à lista
                    self.__lista.append(elemento)
                    print(f"\n\tNúmero válido: {elemento}")
            
                    # Sai do loop se a entrada foi válida
                    break

                except ValueError:
                    limpaTela()
                    print("\n\tOps, entrada invalida! Por favor, digite um número válido.")
                    pause()
                    limpaTela()
        pass
            
    def mostraMediana(self):
     
        
        mediana = self.calcula_salario()
        return mediana
    def mostraMedianaSuperior(self):
        if not self.__lista:
            print("A lista está vazia. Não é possível calcular a mediana superior dos salários.")
            return None

        lista_ordenada = sorted(self.__lista)
        tamanho = len(lista_ordenada)

        if tamanho % 2 != 0:
            mediana_superior = lista_ordenada[tamanho // 2]
            print(f"\n\tA lista de salários tem um número ímpar de elementos. A mediana é: {mediana_superior:.2f}")
        else:
            meio1 = lista_ordenada[tamanho // 2 - 1]
            meio2 = lista_ordenada[tamanho // 2]
            mediana_superior =  meio2

        return mediana_superior
    
    def mostraMedianaInferior(self):
        if not self.__lista:
            print("A lista está vazia. Não é possível calcular a mediana inferior dos salários.")
            return None

        lista_ordenada = sorted(self.__lista)
        tamanho = len(lista_ordenada)

        if tamanho % 2 != 0:
            mediana_inferior = lista_ordenada[tamanho // 2]
            print(f"\n\tA lista de salários tem um número ímpar de elementos. A mediana é: {mediana_inferior:.2f}")
        else:
            meio1 = lista_ordenada[tamanho // 2 - 1]
            meio2 = lista_ordenada[tamanho // 2]
            mediana_inferior =  meio1

        return mediana_inferior
    
            

    def mostraMenor(self):
      
        if not self.__lista:
            print("A lista está vazia. Não é possível calcular o menor elemento.")
            return
        
        menor = self.__lista[0]
        for elemento in self.__lista:
            if elemento < menor:
                menor = elemento
        return menor

    def mostraMaior(self):

        if not self.__lista:
            print("A lista está vazia. Não é possível calcular o maior elemento.")
            return
        
        maior = self.__lista[0]
        for elemento in self.__lista:
            if elemento > maior:
                maior = elemento
        return maior
    
    def calcula_salario(self):
    
        if not self.__lista:
            print("A lista está vazia. Não é possível calcular a mediana dos salários.")
            return None

        lista_ordenada = sorted(self.__lista)
        tamanho = len(lista_ordenada)

        if tamanho % 2 != 0:
            mediana = lista_ordenada[tamanho // 2]
            print(f"\n\tA lista de salários tem um número ímpar de elementos. A mediana é: {mediana:.2f}")
        else:
            meio1 = lista_ordenada[tamanho // 2 - 1]
            meio2 = lista_ordenada[tamanho // 2]
            mediana = (meio1 + meio2) / 2
            print(f"\n\tA lista de salários tem um número par de elementos. A mediana é: {mediana:.2f}")

        return mediana
    
    def listarEmOrdem(self):
   
        limpaTela()
        if not self.__lista:
            print("A lista está vazia. Não é possível ordenar.")
            return

        lista_ordenada = sorted(self.__lista)
        print("\n\t=========== LISTA DE SALÁRIOS EM ORDEM CRESCENTE ===========\n")
        for elemento in lista_ordenada:
            print(f"\tSalário: {elemento:.2f}")
        pause()
        
        pass
    
    def reajustar_Salarios(self):
        
        limpaTela()
        if not self._ListaSalarios__lista:
            limpaTela()
            print("\n\tA lista de salários está vazia, não é possível reajustar os salários")
            pause()
            return None

        
        def calcular_novo_salario(salario):
            return salario * 1.1  # Reajuste de 10%

        # Aplicar a função de reajuste a todos os salários usando o iterador map
        salarios_reajustados = list(map(calcular_novo_salario, self._ListaSalarios__lista))

        print("\n\t=========== SALÁRIOS ANTES E DEPOIS DO REAJUSTE ===========\n")
        
        for salario_original, salario_reajustado in zip(self._ListaSalarios__lista, salarios_reajustados):
            print("\tSalário antes: {:.2f}, Salário reajustado: {:.2f}".format(salario_original, salario_reajustado))

        # Calcular e exibir o custo total da folha de pagamento antes e depois do reajuste
        custo_folha_anterior = sum(self._ListaSalarios__lista)
        custo_folha_atual = sum(salarios_reajustados)

        # print("\n\tCusto total da folha de pagamento antes do reajuste: {:.2f}".format(custo_folha_anterior))
   
        return custo_folha_atual 
   
    @classmethod
    def geraListaSalario(self, quantElementos, salarioMinimo=None, salarioMaximo=None):
        novaLista = []

    
        if salarioMinimo is None or salarioMaximo is None:
            salarioMinimo = 1320
            salarioMaximo = 13200

        for i in range(quantElementos):
            while True:
                try:
                    elemento = random.uniform(salarioMinimo, salarioMaximo)
                    novaLista.append(elemento)
                    break

                except ValueError:
                    print("\n\tOps, entrada inválida! Por favor, digite um número válido.")
                    pause()
                    limpaTela()
        return novaLista
    @classmethod
    def geraListaSalarioNumpy(self, quantElementos, salarioMinimo=None, salarioMaximo=None):
        arraySalarios_aleatorio = []

        if salarioMinimo is None or salarioMaximo is None:
            salarioMinimo = 1320
            salarioMaximo = 13200

        try:
            arraySalarios_aleatorio = np.random.uniform(salarioMinimo, salarioMaximo + 1, quantElementos)
        except ValueError as e:
            print("\n\tOps, foi gerado um salário invalido!\n\t")
            pause()
            limpaTela() 
               
        return np.array(arraySalarios_aleatorio)
         
class ListaIdades(AnaliseDados):
       
    def __init__(self, lista_inteiros=None):
        super().__init__(type(int))
        
        if lista_inteiros is None:
            self.__lista = []
        else:
            self.__lista = lista_inteiros[:]
    
    def entradaDeDados(self):
  
        limpaTela()
        print("\n\t=========== CADASTRO DE IDADES ===========\n")
        try:
            quantElementos = int(input("\n\tDigite a quantidade de elementos da lista: "))
            self.__lista = []

            for i in range(quantElementos):
                while True:
                    elemento_str = input("\n\tDigite o elemento {}: ".format(i + 1))

                    # Verifica se a entrada não está vazia
                    if elemento_str.strip():
                        try:
                            elemento = int(elemento_str)
                            self.__lista.append(elemento)
                            break  # Sai do loop se a entrada for válida
                        except ValueError:
                            limpaTela()
                            print("\n\tOps, idade inválida. Tente novamente.")
                            pause()
                    else:
                        limpaTela()
                        print("\n\tOps, idade inválida. Tente novamente.")
                        pause()
        except ValueError:
            print("\n\tOps, digite um valor numérico válido.")
            pause()
            self.entradaDeDados()
        pass
 
    def geraListaIdade(self, n , iMin = 18, iMax = 65):
        novaListaIdade = []
        for i in range(n):    
            while True:
                try:
                    idade =  random.randint(iMin,iMax )  
                    # Se chegou aqui, a idade é válida, então podemos adicionar à lista
                    novaListaIdade.append(idade)            
                    # Sai do loop se a entrada foi válida
                    break

                except ValueError as e:
                    # limpaTela() 
                    print("\n\tOps, foi gerada uma idade invalida!\n\t")
                    pause()
                    limpaTela() 
        return novaListaIdade
    def geraListaIdadeNumpy(self, n , iMin = 18, iMax = 65):
        arrayIdade_aleatorio = []
        try:
            arrayIdade_aleatorio = np.random.randint(iMin, iMax + 1, n)
        except ValueError as e:
            # limpaTela() 
            print("\n\tOps, foi gerada uma idade invalida!\n\t")
            pause()
            limpaTela() 
               
        return np.array(arrayIdade_aleatorio)
        
    def mostraMediana(self):

        mediana = self.calcula_mediana()
        
        return mediana    
    def mostraMedianaSuperior(self):
        if not self.__lista:
            print("A lista está vazia. Não é possível calcular a mediana superior dos salários.")
            return None

        lista_ordenada = sorted(self.__lista)
        tamanho = len(lista_ordenada)

        if tamanho % 2 != 0:
            mediana_superior = lista_ordenada[tamanho // 2]
            print(f"\n\tA lista de salários tem um número ímpar de elementos. A mediana é: {mediana_superior:.2f}")
        else:
            meio1 = lista_ordenada[tamanho // 2 - 1]
            meio2 = lista_ordenada[tamanho // 2]
            mediana_superior =  meio2

        return mediana_superior
    
    def mostraMedianaInferior(self):
        if not self.__lista:
            print("A lista está vazia. Não é possível calcular a mediana inferior dos salários.")
            return None

        lista_ordenada = sorted(self.__lista)
        tamanho = len(lista_ordenada)

        if tamanho % 2 != 0:
            mediana_inferior = lista_ordenada[tamanho // 2]
            print(f"\n\tA lista de salários tem um número ímpar de elementos. A mediana é: {mediana_inferior:.2f}")
        else:
            meio1 = lista_ordenada[tamanho // 2 - 1]
            meio2 = lista_ordenada[tamanho // 2]
            mediana_inferior =  meio1

        return mediana_inferior
    
    
    def mostraMenor(self):

        if not self.__lista:
            print("A lista está vazia. Não é possível calcular o menor elemento.")
            return
        
        menor = self.__lista[0]
        for elemento in self.__lista:
            if elemento < menor:
                menor = elemento
        return menor
    
    def mostraMaior(self):
       
        
        if not self.__lista:
            print("A lista está vazia. Não é possível calcular o maior elemento.")
            return
        
        maior = self.__lista[0]
        for elemento in self.__lista:
            if elemento > maior:
                maior = elemento
        return maior
    
    def calcula_mediana(self):
        if not self.__lista:
            print("A lista está vazia. Não é possível calcular a mediana.")
            return None

        lista_ordenada = sorted(self.__lista)
        tamanho = len(lista_ordenada)

        if tamanho % 2 != 0:
            mediana = lista_ordenada[tamanho // 2]
            print(f"\n\tA lista tem um número ímpar de elementos. A mediana é: {mediana}")
        else:
            meio1 = lista_ordenada[tamanho // 2 - 1]
            meio2 = lista_ordenada[tamanho // 2]
            mediana = (meio1 + meio2) / 2
            print(f"\n\tA lista tem um número par de elementos. A mediana é: {mediana}")

        return mediana
    
    def listarEmOrdem(self):
  
        limpaTela()     
        print("\n\t=========== LISTA DE IDADES EM ORDEM CRESCENTE ===========\n")

        lista_ordenada = sorted(self.__lista)
        
        for elemento in lista_ordenada:
            print(f"\tIdade: {elemento}")
        pause()
        pass

class ListaNotas(AnaliseDados):
    def __init__(self):
        super().__init__(type(float))
        self.__lista = []

    def entradaDeDados(self):
        limpaTela()
        print("\n\t=========== CADASTRO DE NOTAS ===========\n")

        while True:
            try:
                quantElementos = int(input("\n\tQuantas notas vão existir na lista: "))
                break  # Se a conversão para int for bem-sucedida, sai do loop
            except ValueError:
                limpaTela()
                print("\tPor favor, digite um número inteiro válido.")
                pause()
                limpaTela()

        for i in range(quantElementos):
            while True:
                limpaTela()
                try:
                    elemento = float(input("\n\tDigite a nota {}: ".format(i + 1)))
                    if 0 <= elemento <= 10:
                        self.__lista.append(elemento)
                        break
                    else:
                        limpaTela()
                        print("\tPor favor, digite uma nota entre 0 e 10.")
                        pause()
                except ValueError:
                    limpaTela()
                    print("\tPor favor, digite uma nota válida.")
                    pause()

    def mostraMediana(self):
        if not self.__lista:
            print("A lista de notas está vazia. Não é possível calcular a mediana.")
            return None

        lista_ordenada = sorted(self.__lista)
        tamanho = len(lista_ordenada)

        if tamanho % 2 != 0:
            mediana = lista_ordenada[tamanho // 2]
            print(f"\n\tA lista de notas tem um número ímpar de elementos. A mediana é: {mediana:.2f}")
        else:
            meio1 = lista_ordenada[tamanho // 2 - 1]
            meio2 = lista_ordenada[tamanho // 2]
            mediana = (meio1 + meio2) / 2
            print(f"\n\tA lista de notas tem um número par de elementos. A mediana é: {mediana:.2f}")

        return mediana
    def mostraMedianaSuperior(self):
        if not self.__lista:
            print("A lista está vazia. Não é possível calcular a mediana superior das notas.")
            return None

        lista_ordenada = sorted(self.__lista)
        tamanho = len(lista_ordenada)

        if tamanho % 2 != 0:
            mediana_superior = lista_ordenada[tamanho // 2]
            print(f"\n\tA lista de salários tem um número ímpar de elementos. A mediana é: {mediana_superior:.2f}")
        else:
            meio1 = lista_ordenada[tamanho // 2 - 1]
            meio2 = lista_ordenada[tamanho // 2]
            mediana_superior =  meio2

        return mediana_superior
    
    def mostraMedianaInferior(self):
        if not self.__lista:
            print("A lista está vazia. Não é possível calcular a mediana inferior  das notas.")
            return None

        lista_ordenada = sorted(self.__lista)
        tamanho = len(lista_ordenada)

        if tamanho % 2 != 0:
            mediana_inferior = lista_ordenada[tamanho // 2]
            print(f"\n\tA lista de salários tem um número ímpar de elementos. A mediana é: {mediana_inferior:.2f}")
        else:
            meio1 = lista_ordenada[tamanho // 2 - 1]
            meio2 = lista_ordenada[tamanho // 2]
            mediana_inferior =  meio1

        return mediana_inferior
    
    def mostraMenor(self):
        if not self.__lista:
            print("A lista de notas está vazia. Não é possível calcular a menor nota.")
            return None

        menor = min(self.__lista)
        print(f"\n\tA menor nota é: {menor:.2f}")
        return menor

    def mostraMaior(self):
        if not self.__lista:
            print("A lista de notas está vazia. Não é possível calcular a maior nota.")
            return None

        maior = max(self.__lista)
        print(f"\n\tA maior nota é: {maior:.2f}")
        return maior

    def listarEmOrdem(self):
        limpaTela()
        if not self.__lista:
            print("A lista de notas está vazia. Não é possível ordenar.")
            return

        lista_ordenada = sorted(self.__lista)
        print("\n\t=========== LISTA DE NOTAS EM ORDEM CRESCENTE ===========\n")
        for nota in lista_ordenada:
            print(f"\tNota: {nota:.2f}")
        pause()

  