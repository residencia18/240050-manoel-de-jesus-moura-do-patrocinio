#include <iostream>
#include <string>

using namespace std;

int main(void){
    string nome;
    int anoNascimento;
    cout << "Diguite o seu nome: ";
    cin >> nome;

    cout << "Bom dia, " << nome << ". Tenha um bom curso !";
    cout << endl;

    cout << nome  << " você nasceu em que ano ?";
    cout << endl;

    cin >> anoNascimento;

    cout << "Considerando que estamos em 2023, ou você tem "
        << 2023 - anoNascimento
        << " anos, ou está próximo a fazer.";
        cout << endl;

    return 0;

}