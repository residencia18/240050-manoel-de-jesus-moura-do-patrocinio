#include <iostream>
#include <string>
#include <climits>
using namespace std;

int main(void){
    unsigned  int ui;
    long int li = LONG_MAX;


    cout << "Valor inicial da var unsigned int é: " << ui<< endl; 
    cout << "Valor inicial da var long int é: " << li << endl; 
    cout << endl; 
    cout << endl; 

    ui = li;
    cout << "Valor final da var unsigned  int depois da atribuição: " << ui<< endl; 

    li = ui ;
    cout << "Valor final da var long int depois da atribuição: " << li<< endl; 

    /* Considerações
         Tanto a variavel unsigned long int quanto  long int, utilizam 4 Bytes d memória, se diferenciando que o limit 
         do intervalo do tipo  long int é maior em relação a unsigned  int;

         fontes: Vozes da minha cabeça e Microsoft: https://learn.microsoft.com/pt-br/cpp/cpp/data-type-ranges?view=msvc-170
    */
    
    return 0;
}