# RESOLUÇÃO REV 01
# Aluno: Manoel Patrocínio

Nlado = 1;
try :
    Nlado = int(input("\n\tInforme o valor do lado do quadrado entre 1 e 20 : "));
    
except:
    print("\n\tOps, valor inválido! Informe apenas as um valor numérico entre 1 e 20 disponíveis...")
           

try :
    if 1 <= Nlado <= 20:
        for i in range(Nlado):
            print('* ' * Nlado)
    else:
        print("\n\tOps, valor inválido! Informe apenas as um valor numérico entre 1 e 20 disponíveis...")
        
                          
except:
    print("\n\tOps, Não foi possível desenhar o quadrado, tente novamente...")
           


