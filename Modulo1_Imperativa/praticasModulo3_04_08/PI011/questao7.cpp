#include <iostream>

using namespace std;

int multiplica_por_n(int vet[], int tam, int multiplicador)
{
    for (int i = 0; i < tam; i++)
    {
     vet[i] = vet[i] * multiplicador;
    }

    for (int i = 0; i < tam ; i++)
    {
        cout << vet[i] << "\t";
    }

    cout << endl;
}
int main(void)
{
    int vetor1[] = {1, 3, 5, 7, 9, 11}, tam = 6,  multiplicador = 6;
    multiplica_por_n(vetor1, tam, multiplicador);

    return 0;
}
