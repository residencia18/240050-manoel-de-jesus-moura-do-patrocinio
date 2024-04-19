import math 

# Execício 2 : Operadores Aritméticos em Python

print("\n\nOPERADORES ARITMÉTICOS EM PYTHON \n" ) 

print("Operador de Adição ( + ) -> 2 + 2 = ", 2 + 2)   
print("Operador de Subtração ( - ) -> 6 - 2 = ", 6 - 2)   
print("Operador de Multiplicação ( * ) -> 6 * 2 = ", 6 * 2)   
print("Operador de Divisão real ( / ) -> 6 / 2 = ", 6 / 2)   
print("Operador de Divisão truncada ( // ) -> 7 // 2 = ", 7 // 2)   
print("Operador de Módulo - Resto da Divisão - ( % ) -> 7 % 2 = ", 7 % 2)   
print("Operador de Módulo Exponenciação ( ** ) -> 2 ** 2 = ", 2 ** 2)   
print("Operador de Unário negativo ( - ) ->  o negativo de 2 é =",  -2)  


# Comparativo entre os operadores aritméticos em C/C++ e Python
'''
1. Em C/C++ a prioridade do operador de negação (!) é mais alta do que o perador (not) em Python .
2. Em C/C++ não tem o operador de exponenciação. Usa-se a função pow().
3. Em C/C++ tem dois operadores de incremento (++) e decremento (- -) pós-fixos, que equivalem a, (a + +)  e (a − −)  em Python. 

'''

#Execício 2 - 2º parte: Representação de grandes números inteiros;

print ("\n\nREPRESENTAÇÃO DE GRANDES NÚMEROS EM PYTHON \n ") 
print ("O fatorial de 30 é : ", end="") 
print (math.factorial(30)) 

print("\nO valor inteiro máximo em C/C++ é 2147483647, cerca de 2³¹ - 1 , mas também dependente do compilador.\n")
print("Já em Python um inteiro pode ter um valor tão grande quanto a máquina pode armazenar.")
print( "Como por exemplo 100 elevado a 100: ", 100**100, "\n")


#Execício 2 - 2º parte: Variáveis imutáveis ;

print("VARIÁVEIS IMUTÁVEIS EM PYTHON \n")
print("São aquelas cujo o conteúdo não pode ser alterados ex: str, bool, float, int, long, complex, tuple")

'''
O código a baixo dará erro, pois o objeto do tipo TUPLE é imutável  e estamos tentado realizar uma atribuição direta.
tuple1 = (0, 1, 2, 3) 
tuple1[0] = 4
print(tuple1)
'''

var1 = 1999        
var2 = var1       
print("\nExemplo Prático: \n")
print("o valor de var1 = ", var1)
print("o valor de var2 = ", var2)
print("\nApós incrementar o valor de var1 em 1 (+= 1):\n")
var1 += 1         # incrementando var1 em 1
print("o valor de var1 = ", var1)
print("o valor de var2 = ", var2)


print("\n\nVERIFICAR MÉTODOS DISPONÍVEIS \n")

print("Para verificar os métodos  disponíveis para uma variável inteiro basta usar a função dir(int)")
dir(int)
print("Já a função help(), nos fornece uma breve explicação de como implementa o método e informa qual a utilidade dele. Exemplo help(int.__sizeof__)")
