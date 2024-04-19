#include <iostream>
#include <string>
#include <stdlib.h>
#include <string.h>

using namespace std;

// strtok - quebra uma string em tokens, dado um delimitador específico (use /).

// strtol - converte uma string para um inteiro longo.

// strstr - localiza a primeira ocorrência de uma substring específica em uma string (use //).

// isdigit - verifica se o caractere passado como argumento é um dígito.

int verificarData(char *entrada)
{
   char substring[3] = "//", delimitador[2] = "/";
   char *token = strtok(entrada, delimitador); 
   char smes[12][11] = {"janeiro", "fevereiro", "marco", "abril", "maio", "junho","julho", "agosto", "setembro", "outubro", "novembro", "dezembro"}; 
   
   int i = 0;
   long data[3];

   if (strstr(entrada, substring) != NULL)
   {
      return 0;
   }

   while (token != NULL)
   {
      data[i++] = strtol(token, NULL, 10);
      token = strtok(NULL, delimitador);
   }

   if (data[1] > 12 || data[1] <= 0 ){
      cout << "Voce informou um mes invalido !" << endl;
   }else if(data[0] < 1 || data[0] > 31){
      cout << "Voce informou um dia invalido !" << endl;
   }else if(data[1] == 2 && data[0] > 29){
      cout << "Voce informou um dia invalido !" << endl;
   }else if(data[2] < 1500 || data[2] > 3000){
      cout << "Voce informou um ano invalido !" << endl;

   }
   else {
      cout << data[0] << " de " << smes[data[1] - 1 ] << " de " << data[2] << endl;
   }

   return 1;
}

int main(void)
{
   char data[12];

   cout << "Informe uma data no formato dd/mm/aa: ";
   cin.getline(data, 12);

   verificarData(data);


   return 0;
}