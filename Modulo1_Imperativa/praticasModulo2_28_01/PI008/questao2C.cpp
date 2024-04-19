#include <iostream>
#include <random>
#include <ctime>

using namespace std;

int main(void){
    int tamanho = 5;
    float notasP1[tamanho],notasP2[tamanho], medias[tamanho];
     srand(time(nullptr));

    cout << fixed;
    cout.precision(1);

    for (int i = 0; i < tamanho; i++) {
       notasP1[i] =  (float)(rand()) / (RAND_MAX) * 10;
       notasP2[i] =  (float)(rand()) / (RAND_MAX) * 10;

       medias[i] = (notasP1[i] + notasP2[i]) / 2;
    }

    for (int i = 0; i < tamanho; i++) {
      if ( notasP2[i] >  notasP1[i]){
         cout << "O aluno " << i + 1 << " melhorou" << endl;
         cout << "Notas:  " << notasP1[i] << " e " << notasP2[i] << endl;
         cout << "Media:  " <<medias[i]  << endl;
         cout << endl;
      }else if ( notasP2[i] <  notasP1[i]){
         cout << "O aluno " << i + 1 << " piorou" << endl;
         cout << "Notas:  " << notasP1[i] << " e " << notasP2[i] << endl;
         cout << "Media:  " <<medias[i]  << endl;
         cout << endl;
      }else{
         cout << "O aluno " << i + 1 << " manteve a nota" << endl;
         cout << "Notas:  " << notasP1[i] << " e " << notasP2[i] << endl;
         cout << "Media:  " <<medias[i]  << endl;
         cout << endl;
      }

    }

   
    
   return 0;
}