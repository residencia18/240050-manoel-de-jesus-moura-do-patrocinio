i = '0'

contador = 0

for x in "0123456789":
    print("Em caractere: ", x , "| inteiro: ",ord(x), "| hexadecimal: ", hex(ord(x)), "| octal: ",oct(ord(x)))


caractere = input("\n informe um caractere: ")

print("Em caractere: ", caractere , "| inteiro: ",ord(caractere), "| hexadecimal: ", hex(ord(caractere)), "| octal: ",oct(ord(caractere)))

if(ord(caractere) >= 128):
    print("Para as letras acentuadas, bem como para outros caracteres usados num determinado idioma, que não \
    pertencem à tabela ASCII, são atribuídos códigos numéricos entre 128 e 255." )
