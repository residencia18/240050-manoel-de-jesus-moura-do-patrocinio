#include <iostream>

using namespace std;

int fatorial (int n) {
    int fatorial = 1;
    for (int i=1; i<=n; i++)
        fatorial*=i;
    return fatorial; 
}

int main()
{
  int numero, escolha;


  do
  {
    cout << "Informe um numero inteiro para calcular o fatorial: ";
    cin >> numero;
    cout << endl;
    cout << endl;

    cout << "O fatorial do número " << numero << " é: " << fatorial(numero) << endl;

    cout << endl;

    cout << "Deseja repetir o calculo com outro numero ?" << endl;
    cout << "1 - Sim  | 2 - Não " << endl;
    cin >> escolha;

  } while ( escolha == 1);
  
}