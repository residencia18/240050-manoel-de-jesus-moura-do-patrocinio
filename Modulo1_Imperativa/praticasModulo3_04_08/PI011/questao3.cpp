#include <iostream>

using namespace std;

void ordenCrecente (float &num1, float &num2, float &num3,float &num4){
   float vetor[] = {num1,num2,num3,num4};
   int aux;
    for (int i=0; i< 4; ++i){
        for (int j=i; j< 4; ++j){
            if (vetor[i]>vetor[j]){
                aux = vetor[i];
                vetor[i] = vetor[j];
                vetor[j] = aux;
            }
        }
    }
    for (int i=0; i<4; ++i)
        cout << vetor[i] << " ";
    cout << endl;    

}
int main(void){
    float n1 = 3.913f, n2 = 2.5f,n3 = 1E-5f,n4 = 7.5f;
    ordenCrecente(n1,n2,n3,n4);
    return 0 ;
}
