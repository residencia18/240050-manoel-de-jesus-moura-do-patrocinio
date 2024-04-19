#include <iostream>
#include <string>

using namespace std;

int main(void){
    int b; 
    b = 0x80000000;
    cout << "O menor valor do tipo int é: " << b<< endl; 
    b--;
    cout << "O maior valor do tipo int é " << b << endl;
    return 0;
}