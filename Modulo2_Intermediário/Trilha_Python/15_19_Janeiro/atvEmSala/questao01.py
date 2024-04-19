import random  
tentativas = 1


print(" \nEstou pensando em um número entre 1 e 100, vc terá 8 tentativas para adivinhar \n")

valor = random.randint(1, 100)

while tentativas <= 8:
    
    chute = int (input(f"Sua {tentativas }º tentativa é: "))
    
    if chute < valor :
        print("R: Não o número é maior :-( \n")
    elif chute > valor:
        print("R: Não o número é menor (:-O\n")
    else: 
        print("R: Parabéns você acertou (:-)\n")
        break 
    tentativas += 1   
    

if tentativas > 3:
    print("Lamento, acabaram suas oportunidades ;-)")
    print(f"o número que pensei foi {valor} !")