#include <iostream>


using namespace std;

void insere_meio(int vet[], int tam, int novoElemento){
    int novo_vetor[tam + 1];

    for(int i = 0; i <= tam / 2; i++ ){
        if( i == (tam / 2)){
            novo_vetor[i] = novoElemento;
        }else  {
            novo_vetor[i] = vet[i];
        }
    }
    for(int i = (tam / 2) + 1; i < tam + 1; i++ ){
        novo_vetor[i] = vet[i - 1];
    
    }
    for(int i =0; i < sizeof(novo_vetor)/sizeof(novo_vetor[0]); i++ ){
        cout << novo_vetor[i] << "\t";
    }
    cout << endl;
}
int main(void){
    int vetor[] = {1,2,3,4,5,6}, tam = 6;
    insere_meio(vetor,tam,100);

    return 0 ;
}
