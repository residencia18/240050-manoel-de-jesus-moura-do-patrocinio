import random  
tentativas = 1
respostas_dadas =[]
intervaloInt = 1
intervaloFin = 100
user_respo = 0
print(" \nPense em um número entre 1 e 100, eu terei 8 tentativas para adivinhar \n")



while tentativas <= 3:
    
    valor = random.randint(intervaloInt, intervaloFin)
        
    print (f"\n O valor é : {valor} ?")
    
    print("\n1 - p/ Não o número é maior :-( ")
    print("2 - p/ Não o número é menor (:-O")
    print("3 - p/ Parabéns você acertou (:-)\n")
    user_respo = int (input(f"Digite aqui: "))

    if user_respo == 1 :
      respostas_dadas.append(valor)
      intervaloInt = valor + 1
    
    elif user_respo == 2:
        respostas_dadas.append(valor)
        intervaloFin  = valor - 1
    else: 
        break 
    tentativas += 1   
    

if tentativas > 3:
    print("\nLamento, minhas oportunidades acabaram  ;-)")
    resposta = int (input(f"Qual numero vc pensou: "))
    
    if resposta not in respostas_dadas:
        print(f"\nRealmente não pensei no valor {resposta} !")
        print(f"só nos valores {respostas_dadas} !")
    else:
        print("Você trapaceou (:-(")