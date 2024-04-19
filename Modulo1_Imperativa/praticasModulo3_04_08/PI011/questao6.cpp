#include <iostream>

using namespace std;

int intercala(int vet[], int tam, int vet2[], int tam2)
{
    int novo_vetor[tam + tam2], count = 0, count2 = 0;

    for (int i = 0; i < (tam + tam2); i++)
    {
        if (i % 2 != 0)
        {

            if (count < tam2)
            {
                novo_vetor[i] = vet2[count];
                count += 1;
            }
        }
        else
        {
            if (count < tam)
            {
                novo_vetor[i] = vet[count2];
                count2 += 1;
            }
        }
    }

    for (int i = 0; i < (tam + tam2); i++)
    {
        cout << novo_vetor[i] << "\t";
    }
}
int main(void)
{
    int vetor1[] = {1, 3, 5, 7, 9, 11}, tam = 6, vetor2[] = {2, 4, 6, 8, 10, 12}, tam2 = 6;
    intercala(vetor1, tam, vetor2, tam2);

    return 0;
}
