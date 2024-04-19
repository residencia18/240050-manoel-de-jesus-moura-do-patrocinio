#include <iostream>

using namespace std;

int main(void){
    unsigned long int uli;
    uli = 0xffffffff;


    cout << "O maior valor do tipo unsigned long int é: " << uli<< endl; 
    
    cout << "o menor valor do tipo unsigned long int é: " << uli - uli << endl;
    return 0;
}