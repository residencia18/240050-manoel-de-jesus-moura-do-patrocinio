#include <iostream>
#include <string>

using namespace std;

int main(void){

   char zero = '0';
   int cont = 0;
   
   while (cont < 10 ){
    cout << "char:" << zero  << " int:" << (int) zero << " hex:" << hex << (int)zero << " oct: " << oct << (int)zero<< endl ;   
    zero++;
    cont ++;
   }
    

    return 0;
}