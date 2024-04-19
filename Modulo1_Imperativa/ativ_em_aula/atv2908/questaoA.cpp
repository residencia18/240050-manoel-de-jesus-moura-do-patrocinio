#include <iostream>
#include <string>

using namespace std;

int main(void){



   char zero = 'a';
   int cont = 0;
   
   while (cont < 10 ){
    cout << "char:" << zero << " - " << "int:" << (int) zero << endl ;   
    zero++;
    cont ++;
   }

    return 0;
}