lista_salario = []
lista_abono = []
qtd_valor_minimo = 0
opcao = 0

while True:
    opcao = float( input("Informe o salario ou digite 0 p/ sair: "))
    
    if(opcao == 0 or opcao == 0.0):
        print("\nAté mais\n")
        break
    lista_salario.append(opcao)


print("Salario \t-\tAbono")

for salario in lista_salario:

    abono = float(salario * 0.2)    
    if abono <= float(100):
        abono = 100.0
        qtd_valor_minimo += 1




    lista_abono.append(abono)
    print(f"R$ {salario}\t-\tR$ {abono}")


print("\n---- RELATÓRIO ---- \n")
print(f"Foram processados {len(lista_salario)} colaboradores")
print(f"Total gasto com abonos: R$ {sum(lista_abono)}")
print(f"Valor mínimo pago a {qtd_valor_minimo} colaboradores")
print(f"Maior valor de abono pago: R$ {max(lista_abono)}")
