#include <stdio.h>
#include <iostream>

using namespace std;

int main() {
   int numero = 3333,num = 0 ,palindromo = 0;      

    cout << "Informe um numero:";
    cin >> numero;

   num = numero;                           //É feita uma cópia para manipulação do valor de numero. 

  if (num < 0) num = -num;                    //Testa se num é negativo, caso seja obtenha seu valor absoluto.
  
  //Enquanto num for maior que palindromo...
  while(num > palindromo) {
    int digito = num % 10;                    //...obtém o dígito da unidade de num.
    palindromo =  palindromo * 10 + digito;   //...multiplica palíndromo por 10 e adiciona o dígito anteriormente obtido.
    //...caso num seja igual palindromo ou caso num extirpado das unidades seja igual palindromo sai do laço.
    if (num == palindromo || (num /= 10) == palindromo) break;
  }

  printf(" O numero %d %s é um palíndromo.\n", numero, palindromo == num ? "" : "não "
  );

  return 0;
}

//fonte: stackoverflow, faltou massa cinzenta pra resolver de cabeça kk