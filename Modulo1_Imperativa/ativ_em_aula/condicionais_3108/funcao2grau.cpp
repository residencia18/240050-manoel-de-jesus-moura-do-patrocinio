#include <iostream>
#include <math.h>

using namespace std;


int main(void){
    int a,b,c,delta,x1,x2;

    cout << "informe o valor de A: ";
    cin >> a;

    cout << "informe o valor de B: ";
    cin >> b;

    cout << "informe o valor de C: ";
    cin >> c;

    delta =  pow(b,2) - 4 * a * c;

    if(delta > 0){
        x1  = (-b  + sqrt(delta)) / (2 * a) ;
        x2  = (-b  - sqrt(delta)) / (2 * a) ;

        cout << "o Valor de x1: " << x1 << endl;
        cout << "o Valor de x2: " << x1 << endl;
    }else if(delta == 0){
        x1 = -b / (2 * a);
    }else{
        cout << "Não exite raiz real" << endl;
    }

    return 0;
}