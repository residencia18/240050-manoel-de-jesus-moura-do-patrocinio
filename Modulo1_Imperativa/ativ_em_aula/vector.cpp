#include <iostream>
#include <math.h>
#include <vector>

using namespace std;


int main(void){

    vector <string> alunos;
    string nome, alunoEncontrado, nomePbusca;
    int posicaoAluno;

    for(int i = 0; i < 3; i++){
        cout << "Informe o nome do aluno: ";
        getline(cin, nome);
        alunos.push_back(nome);
        
    }

    cout << endl;
    cout << "Alunos: " << endl;
    cout << endl;

    
    for(auto it = alunos.begin(); it != alunos.end(); it++){
        cout << *it << endl;
    }

    cout << "Qual a posição do alunos deseja buscar: ";
    cin >> posicaoAluno;

    vector<string>::iterator it;
    it = alunos.begin();
    advance(it,posicaoAluno);
    alunoEncontrado = *it;

    cout << "O aluno nessa posição é o(a): " << alunoEncontrado << endl;

    cout << "Busque pelo nome do aluno: ";
    cin >> nomePbusca;
    signed int posicao = -1;

    for(auto it = alunos.begin(); it != alunos.end(); it++){
        posicao ++;
        if(*it == nomePbusca){
            cout << "Este aluno esta na posição: " << posicao
            
             << endl;

        }
    }

    string novoNome;
    int posicaoNovoNome;

    cout << "informe o nome da pessoa que vc quer adiconar a lista: ";
    getline(cin, novoNome);
    cout << "informe a posicao: ";
    cin >> posicaoNovoNome;

    vector<string>::iterator it2;
    it2 = alunos.begin();
    advance(it2,posicaoNovoNome);
    alunos.insert(it2,novoNome );

    cout << endl;
    cout << "Nova lista alunos: " << endl;
    cout << endl;

    
    for(auto it = alunos.begin(); it != alunos.end(); it++){
        cout << *it << endl;
    }
    return 0 ;
}