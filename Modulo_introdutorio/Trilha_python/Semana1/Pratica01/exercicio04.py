def palindromo(nome):    
    size = len(nome)
    if size == 0:
        # Se a string é vazia, ela não é palíndromo
        return False
    for i in range(0, size // 2):
        if nome[i] != nome[size - i - 1]: # encontrei diferença, nem precisa continuar
            return False
    return True

nome = "Manoel Patrocinio"

namePerParts = nome.split(" ")

print('O primeiro nome é: ',namePerParts[0], "com ", len(namePerParts[0]), " caracteres")
print('O sobrenome nome é: ',namePerParts[1], "com ", len(namePerParts[1]), " caracteres")

namePerParts.sort()

print('\nO primeiro nome em ordem alfabética é: ',namePerParts[0])
print('O segundo  nome em ordem alfabética é: ',namePerParts[1])

 
if palindromo(namePerParts[0]):
    print("\nSeu primeiro nome é um palindromo")
else:
    print("\nSeu primeiro nome não é um palindromo")
        

