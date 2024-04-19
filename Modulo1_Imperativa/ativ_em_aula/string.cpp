#include <iostream>
#include <string>

using namespace std;


int main(void){
    string nome, sobrenome;
    cout << "diguite seu nome: ";
    getline(cin, nome);
    
    cout << "diguite seu sobrenome: ";
    getline(cin, sobrenome);

    cout << nome << " " << sobrenome <<endl;


}