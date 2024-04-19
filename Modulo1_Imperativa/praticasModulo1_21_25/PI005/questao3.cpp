#include <iostream>

using namespace std;

int main(void){
    int a = 0,b = 0,c = 0;

    cout << "Informe um numero inteiro:";
    cin >> a;
    cout << "Informe outro numero inteiro:";
    cin >> b;

    cout << endl;
    c = a + b;

    cout << "A soma dos valores em hexadecimal é: " << hex << c << endl;
   
    c = 0;
    c = a * b;

    cout << "O produto dos valores em octal é: " << oct << c << endl;
    c = 0;
    c = a - b;
    cout << "O valor absoluto dos valores  é: " << (float)c << endl;

    if(b == 0 ){
        cout << "Não é possivel realizar a divisão, pois o divisor é 0 " << endl;
    } else{
        c = 0;
        c = a / b;
        cout << "O quociente da divisão dos valores  é: " << (float)c << endl;
        
        c = 0;
        c = a % b;
        if(c == 0){
            cout << "É uma divisão exata, resto: " << (float)c << endl;
        }else{
            cout << "Não é uma divisão exata, resto: " << (float)c << endl;

        }
    }

    return 0;
}