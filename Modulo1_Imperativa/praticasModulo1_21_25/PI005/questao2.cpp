#include <iostream>
#include <string>
#include <cstring>

using namespace std;

int main(void){

   char ch1,ch2,ch3;
   
   cout << "Diguite um caratere:";
   cin >> ch1;


//    cout << (ch1 >= 'A' && ch1 <= 'Z' ? "É um caractere maiusculo" : "") << endl;
//    cout << (ch1 >= 'a' && ch1 <= 'z' ? "É um caractere minusculo" : "") << endl;
//    cout << (ch1 >= 0 && ch1 <= 9 ? "É um Digito" : "") << endl;

   cout << endl;
   cout <<  "Resultado com funções prontas do C++:" << endl;

   if(isupper(ch1)){
    cout <<  "É um caractere maiusculo" << endl;

   }else if(islower(ch1)) {
    cout <<  "É um caractere minusculo" << endl;
   }else if(isdigit(ch1)){
    cout <<  "É um digito" << endl;
   }else{
    cout <<  "É outro tipo de caractere" << endl;

   }

   cout << endl;
   ch2 = 81;
   ch3 = tolower(ch2);
 
   cout << "ch2 no tipo: char: " << ch2  << " int: " << (int) ch2 << " hex: " << hex << (int)ch2 << " oct: " << oct << (int)ch2<< endl ;   
   cout << "ch3 no tipo: char: " << ch3  << " int: " << (int) ch3 << " hex: " << hex << (int)ch3 << " oct: " << oct << (int)ch3<< endl ;   
    

    return 0;
}