#include <iostream>
#include <math.h>

using namespace std;

int main(void){

    int a,b,c;

    cout << "Informe um numero inteiro: ";
    cin >> a;
    cout << "Informe outro numero inteiro: ";
    cin >> b;

    c = (4 * a) + (b / 3) - 5;
    cout << "O resultado da expressão (4 * 𝑎 + 𝑏 / 3 − 5) com os valores informados é: " << c << endl;

    cout << endl;
    c = 4 * (a + b) / (3 - 5);
    cout << "O resultado da expressão 4 * (𝑎 + 𝑏) / (3 − 5) com os valores informados é: " << c << endl;

/* Em C++ as expressões que envolvem vários operadores aritméticos, são resolvidos em uma
    seqüência determinada pelas regras de precedência. Então como a expressão e a prececedência mudou, o resultado também muda; */


    cout << "O resultado da expressão 𝑎 + 2 * 𝑏 + 𝑐 com os valores informados é: " << pow(a,2) +  (2  * b)  + c << endl;

 

    return 0;
}