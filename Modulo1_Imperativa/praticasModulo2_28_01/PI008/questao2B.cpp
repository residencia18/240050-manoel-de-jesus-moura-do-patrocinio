#include <iostream>
#include <random>
#include <ctime>

using namespace std;

int main(void){
    int tamanho = 250;
    float temperaturas[tamanho], tempMin,tempMax = 0,media, soma;
     srand(time(nullptr));
    for (int i = 0; i < tamanho; i++) {
       temperaturas[i] = 10.0 + (float)(rand()) / ((float)(RAND_MAX/(40 - 10)));
    }

    cout << fixed;
    cout.precision(2);
    
    tempMin = temperaturas[0];
    
    for (int i = 0; i < tamanho; i++) {
       cout << temperaturas[i] << endl;
       soma += temperaturas[i];
       if(tempMin > temperaturas[i]){
        tempMin = temperaturas[i];
       }
       if(tempMax < temperaturas[i]){
        tempMax = temperaturas[i];
       }
    }

    cout << endl;
    cout << endl;

    cout << "A temperatura maxima é: " << tempMax << endl;
    cout << "A temperatura minima é: " << tempMin << endl;
    cout << "A temperatura media é: " << soma / tamanho << endl;
    
    cout << endl;
    cout << endl;

    cout << "A temperatura atualizada de acordo com a previsao: " << endl;
    
    for (int i = 0; i < tamanho; i++) {
  
       if(temperaturas[i] > (soma / tamanho) ){
        temperaturas[i] += 1.0;
       }
       if(temperaturas[i] < (soma / tamanho) ){
        temperaturas[i] -= 2.0;
       }
    }
    for (int i = 0; i < tamanho; i++) 
       cout << temperaturas[i] << endl;
    
   return 0;
}