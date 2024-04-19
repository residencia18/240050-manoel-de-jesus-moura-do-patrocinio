
lista_numero = []
qtd_votos = 0
melhor_jogador = (0,0,0)
print("\nEnquete: Quem foi o melhor jogador\n ")

while  True:
    opcao = int(input("\nNúmero do jogador (0=fim): "))
   
    if(opcao < 0 or opcao > 23):
        print("\nOps, opção inválida! Tente novamente...\n")
    if opcao == 0:
        break
    lista_numero.append(opcao)

        
print("Resultado da votação:\n")

print(f"Total de votos computados: {len(lista_numero)}\n")

list_valor_unico = list(set(lista_numero))

for nJogador in list_valor_unico:
    qtd = lista_numero.count(nJogador)
    porcentagem = (qtd / len(lista_numero)) * 100
    
    print(f"O jogador: {nJogador}\t Nº Votos:{qtd}\t {porcentagem:.1f}%")

    if qtd_votos < qtd:
        qtd_votos = qtd
        melhor_jogador = (nJogador,qtd_votos,porcentagem)
    

print(f"O melhor jogador foi o número {melhor_jogador[0]}, com {melhor_jogador[1]} votos, correspondendo a {melhor_jogador[2]}% do total de votos.")