#Estudo sobre funções


def fibonacci(N):
    L = [0]
    a, b = 0, 1
    while len(L) < N:
        a, b = b, a + b
        L.append(a)
    return L
def main():
    qtd = int(input("Informe a quantidade de numeros da sequencia fibonacci: ")) 
    print(fibonacci(qtd))
    
    def divNum(a, b):
        try:
            return a/b
        except:
            return 1E100 # Um número muito grande pode ser uma aproximação para infinito

    print("4/2 = ", divNum(4, 2))
    print("4/0 = ", divNum(4, 0))
        
main()