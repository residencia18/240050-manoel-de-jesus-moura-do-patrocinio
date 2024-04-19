#include <iostream>

using namespace std;


int main(void){
    int a;

    cout << "informe um número inteiro: ";
    cin >> a;

    if(a % 2 == 0){
        cout << a << " é um número par:" << endl;

    }else{
        cout << a << " é  um número impar:" << endl;
    }

    return 0;
}