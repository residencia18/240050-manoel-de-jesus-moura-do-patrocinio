#include <iostream>

using namespace std;


int main(void){
    char aluno1[30],aluno2[30],aluno3[30];
    float notal1[3],notal2[3], notal3[3],soma, media = 0;

    cout << "Informe seu nome: ";
    cin.getline(aluno1,30);

    for(int i = 0; i < 3; i++){
        cout << "Informe a nota " << i + 1 << " : ";
        cin >> notal1[i]; 
        soma += notal1[i];
    }

    media = 0;    
    media += soma;

    cout << "A media do aluno " << aluno1 << " é: " << media / 3 << endl;

    cout << endl;

    cout << "Informe seu nome: ";
    cin.getline(aluno2,30);

    media = 0;    
    soma = 0;
    for(int i = 0; i < 3; i++){
        cout << "Informe a nota " << i + 1 << " : ";
        cin >> notal2[i]; 
        soma += notal2[i];
    }
        
    media += soma;

    cout << "A media do aluno " << aluno1 << " é: " << media / 3 << endl;


    cout << endl;

    cout << "Informe seu nome: ";
    cin.getline(aluno3,30);

    media = 0;    
    soma = 0;
    for(int i = 0; i < 3; i++){
        cout << "Informe a nota " << i + 1 << " : ";
        cin >> notal3[i]; 
        soma += notal3[i];
    }
        
    media += soma;

    cout << "A media do aluno " << aluno1 << " é: " << media / 3 << endl;

    return 0;
}