#include <iostream>
#include <math.h>

using namespace std;

int main(void){

    char ch1, ch2, ch3;

    cout << "Informe um caractere: ";
    cin >> ch1;
    cout << "Informe outro caractere: ";
    cin >> ch2;

    ch3 = --ch1;
    cout << "o caractere que antecede ao caractere: " << ch1 << endl;
    cout << "char:" << ch3  << " int:" << (int) ch3 << " hex:" << hex << (int)ch3 << " oct: " << oct << (int)ch3<< endl ;   

    cout << endl;
    
    ch3 = ++ch2;
    cout << "o caractere que precede ao caractere: " << ch2 << endl;
    cout << "char:" << ch3  << " int:" << (int) ch3 << " hex:" << hex << (int)ch3 << " oct: " << oct << (int)ch3<< endl ;   

    cout << endl;

    // questão  3.e
   
    isupper(ch1) ? ch3 = 'A' : ' ';
    cout << "valor de ch3 depois da verificação: " << ch3 << endl;

    // questão  3.f
   
    islower(ch1) ? ch3 = 'a' : ' ';
    cout << "valor de ch3 depois da segunda verificação: " << ch3 << endl;
    
    // questão  3.g
   
    isdigit(ch1) || isdigit(ch2) ? ch3 = '1' : ' ';
    cout << "valor de ch3 depois da segunda verificação: " << ch3 << endl;


    return 0;
}