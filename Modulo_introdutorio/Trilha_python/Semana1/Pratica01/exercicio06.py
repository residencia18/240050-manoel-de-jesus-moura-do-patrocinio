L = [1,2,3,4,5,6,7,8,9]

print("Lista original:")
print(L)


print("\nLista usando slicing:")

print(L[::2])
print(L[-1::])
print(L[:-1:])
print(L[::-2])
print(L[-2::])
print(L[:-2:])

signo = ["Macaco","Galo","Cão","Porco","Rato","Boi","Tigre","Coelho","Dragão","Serpente","Cavalo","Carneiro"]

ano = input("Informe seu ano de nascimento: ")

try:
    resto = int(ano) % 12
    if resto >= 0 & resto < 12: 
        print("seu animal no zodiaco chines é:", signo[resto])
    
except Exception as inst:
    print ("Ocorreu um erro!",inst)
