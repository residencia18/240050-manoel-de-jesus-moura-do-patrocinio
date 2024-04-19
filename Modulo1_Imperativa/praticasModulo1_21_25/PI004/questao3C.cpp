#include <iostream>
#include <string>

using namespace std;

int main(void){
    unsigned long int uli;
    long int li = 0;
    uli = 0xffffffff;


    cout << "Valor inicial da var unsigned long int é: " << uli<< endl; 
    cout << "Valor inicial da var long int é: " << li << endl; 
    cout << endl; 
    cout << endl; 

    li = uli;
    cout << "Valor final da var long int depois da atribuição: " << li<< endl; 
    uli = li;
    cout << "Valor final da var unsigned long int depois da atribuição: " << uli<< endl; 

    /* Considerações
         Tanto a variavel unsigned long int quanto  long int, utilizam 4 Bytes d memória, se diferenciando que o limit 
         do intervalo do tipo unsigned long int é maior em relação a outra;

         fontes: Vozes da minha cabeça e Microsoft: https://learn.microsoft.com/pt-br/cpp/cpp/data-type-ranges?view=msvc-170
    */
    
    return 0;
}