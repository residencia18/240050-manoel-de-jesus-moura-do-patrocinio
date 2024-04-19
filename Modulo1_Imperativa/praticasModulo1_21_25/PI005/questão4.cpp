#include <iostream>
#include <cmath>
#include <math.h>

using namespace std;

int main(void){

    double x,y,z;

    cout << "Informe o primerio numero real: ";
    cin >> x;

    cout << "Informe o segundo numero real: ";
    cin >> y;

    cout << endl;
    z = (5 * x) + 2;

    if(z == 0 ){
      cout << "o ponto "<< z << " se enconta na curva " << endl;
    }else if( z > 0){
      cout << "o ponto "<< z << " se enconta a direira " << endl;

    }else{
      cout << "o ponto "<< z << " se enconta a esquerda " << endl;

    }

    z = 0;
    double raiz = pow(x,2) + pow(y,2);
    z = sqrt(raiz);

    cout << "o valor da distância euclidiana do ponto (x, y) é: " << z << endl;
    
    z = 0;
    z = x * y;
    cout << "O produto de x e y é: " << z << endl;




    return 0;
}