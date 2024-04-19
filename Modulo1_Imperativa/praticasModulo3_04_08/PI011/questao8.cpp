#include <iostream>

using namespace std;

int conta_primos(int vet[])
{
    int  divisores = 0,primos = 0;

    for (int i = 0; i < 6; i++)
    {
       divisores = 0;
        for ( int j = 1; j <= vet[i]; j ++){
            if( vet[i] % j == 0) {
                divisores++;
            }
        };

        if(divisores == 2){
            primos++;
        }
       
    }


    cout << "QTD numeros primos no array: " << primos << endl;
  
}
int main(void)
{
    int vetor[] = {1, 3, 5, 7, 9, 11};
    conta_primos(vetor);

    return 0;
}
