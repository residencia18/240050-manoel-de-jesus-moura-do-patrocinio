#include <iostream>
#include <math.h>

using namespace std;

int main(void){

     int n1, n2, maior;

    cout << "Informe um inteiro: ";
    cin >> n1;
    cout << "Informe outro inteiro: ";
    cin >> n2;

    
    cout << endl;
    maior = n1 > n2 ? n1 : n2;
    cout << "O  maior numero e: " << maior << endl;
    n1 == n2  ? (cout << "estes numero sao iguais"): (cout << "estes numero nao sao iguais") << endl;
    maior % 2 == 0  ? (cout << "O maior numero é par") << endl : (cout << "O maior numero é impar") << endl;

    return 0;
}