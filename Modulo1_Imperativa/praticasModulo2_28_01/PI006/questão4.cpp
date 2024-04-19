#include <iostream>
#include <math.h>
#include <stdio.h>
#include <stdlib.h>

using namespace std;

int main(void){

  double x,y,z;
  printf("Informe um numero real: ");
  scanf("%lf",&x);
  
  printf("Informe outro numero real: ");
  scanf("%lf",&y);

  z = x + y; 
  printf("Valor da soma %lf\n",z);

  cout << endl;

  z = (x + y) / 2; 
  printf("Valor da media %lf\n",z);

  z = x * y; 
  printf("Valor do produto %lf\n",z);

  cout << endl;

  z =  x > y ? x : y; 
  printf("O maior valor %lf\n",z);

  cout << endl;

  z =  x < y ? x : y; 
  printf("O menor valor %lf\n",z);

  cout << endl;

    
    
    return 0;
}