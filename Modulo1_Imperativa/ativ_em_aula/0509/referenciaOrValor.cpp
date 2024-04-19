#include <iostream>

using namespace std;

int resto10(int &n){
    if (n > 10){
        return n % 10;
    }
}
int main(void){

    int a, resultado;

    cout << "diguite um valor inteiro: ";
    cin >> a;

    resultado = resto10(a);

    cout << " o resta da divisao por 10 e: " << resultado << endl ;

    return 0;
}