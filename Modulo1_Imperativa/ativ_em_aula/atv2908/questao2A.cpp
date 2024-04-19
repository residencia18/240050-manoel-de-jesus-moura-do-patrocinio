#include <iostream>
#include <string>

using namespace std;

int main(void){
    int b; 
    b = 0x80000000;
    cout << "O menor valor é: " << b<< endl; 
    b--;
    cout << "o maior valor é " << b << endl;
    return 0;
}