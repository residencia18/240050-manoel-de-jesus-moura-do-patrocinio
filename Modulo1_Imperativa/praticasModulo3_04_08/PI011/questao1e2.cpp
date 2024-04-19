#include <iostream>
#include <vector>
#include <string>

using namespace std;

void maxmin (int vetor[], int n, int &maximo, int &minimo){
    maximo = vetor[0];
    minimo = vetor[0];
    for(int i = 0; i < n; i++){
        if(maximo < vetor[i]){
            maximo = vetor[i];
        }
        if(minimo > vetor[i]){
            maximo = vetor[i];
        }
    }
}
int main(void){
   int vet[] = { 1,3,5,7,10},  maximo, minimo;
   
    maxmin(vet,5, maximo,minimo);
    cout << "Maior valor : " << maximo << " e Menor valor: "<< minimo << endl;
    return 0 ;
}

/*
Exercício 2:Qual o tipo de coesão e acoplamento da função do exercício 1?

Resposta: Coesão Funcional, Acoplamento de Dados.
*/