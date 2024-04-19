import sys

expo2 = 2.0
print("EXPONENCIAÇÃO COM VARIAVEIS FLUTUANTES  EM PYTHON \n")
print("Menor valor da  potencia de 2 : ", expo2 ** sys.float_info.min)
print("Maior valor da  potencia de 2 : ", expo2 ** sys.float_info.max)

print("\nVARIÁVEIS FLOATS IMUTÁVEIS EM PYTHON \n")

var1 = 19.99        
var2 = var1    
print("\nExemplo Pratico: \n")
print("o valor de var1 = ", var1)
print("o valor de var2 = ", var2)
print("\nApós incrementar o valor de var1 em 1 (+= 1):\n")
var1 += 1         # incrementando var1 em 1
print("o valor de var1 = ", var1)
print("o valor de var2 = ", var2)