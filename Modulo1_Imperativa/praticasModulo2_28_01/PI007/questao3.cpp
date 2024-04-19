#include <stdio.h>
#include <iostream>

using namespace std;

int main() {
    int numero, divisores = 0;
    
    cout << "informe  o números para verificar os divisores: ";
    cin >> numero;

    cout << "Os divisores desse número são: " << endl;

    for ( int count = 1; count <= numero; count ++){
       if( numero % count == 0) {
        divisores ++;
         cout  << count << endl;

       }
    };
    cout << "O total de divisores é: " << divisores << endl;
    
    return 0 ;
}

//fonte: stackoverflow, faltou massa cinzenta pra resolver de cabeça kk