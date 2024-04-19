#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;


float calcularMedia(float nota1, float nota2) {
    return (nota1 + nota2) / 2.0f;
}

void ordenarNomes(vector<string>& nomes) {
    bool trocou;
    do {
        trocou = false;
        for (size_t i = 0; i < nomes.size() - 1; i++) {
            if (nomes[i] > nomes[i + 1]) {
                swap(nomes[i], nomes[i + 1]);
                trocou = true;
            }
        }
    } while (trocou);
}

int main() {
    int limiteAlunos,opcao; 
    vector<string> nomes;
    vector<float> notas;
    char incluirAlunos,excluirAluno, alterarNota;  
    string nome,nomeExcluir,nomeAlterar;
    float nota1, nota2;

    cout << "Quantos alunos deseja informar: ";
    cin >> limiteAlunos;

   
    do {
        if (nomes.size() >= static_cast<size_t>(limiteAlunos)) {
            cout << "O limite de alunos foi atingido !" << endl;
            break;
        }

        cout << "Digite o nome do aluno: ";
        cin >> nome;
        cout << "Digite a primeira nota do aluno: ";
        cin >> nota1;
        cout << "Digite a segunda nota do aluno: ";
        cin >> nota2;

        nomes.push_back(nome);
        notas.push_back(nota1);
        notas.push_back(nota2);

        ordenarNomes(nomes);

        cout << "Deseja incluir mais alunos (s/n) ? ";
        cin >> incluirAlunos;
    } while (incluirAlunos == 's' || incluirAlunos == 'S');

    do {
        cout << "Deseja excluir algum aluno (s/n) ? ";
        cin >> excluirAluno;

        if (excluirAluno == 's' || excluirAluno == 'S') {
            cout << "Informe o nome do aluno que deseja excluído: ";
            cin >> nomeExcluir;

            auto it = find(nomes.begin(), nomes.end(), nomeExcluir);
            if (it != nomes.end()) {
                // se encontrou o aluno vai exclui-o
                size_t pos = distance(nomes.begin(), it);
                nomes.erase(nomes.begin() + pos);
                notas.erase(notas.begin() + pos * 2, notas.begin() + pos * 2 + 2);
                cout << "Aluno excluido !" << endl;
            } else {
                cout << "Não encontramos o aluno informado !" << endl;
            }
        }
    } while (excluirAluno == 's' || excluirAluno == 'S');

 
    do {
        cout << "Deseja alterar alguma nota (s/n)? ";
        cin >> alterarNota;
        if (alterarNota == 's' || alterarNota == 'S') {
            cout << "Digite o nome do aluno cuja nota será alterada: ";
            cin >> nomeAlterar;

            auto it = find(nomes.begin(), nomes.end(), nomeAlterar);
            if (it != nomes.end()) {
                
                cout << endl;
                size_t pos = distance(nomes.begin(), it);
                cout << "Notas do aluno " << nomes[pos] << ": " << notas[pos * 2] << " e " << notas[pos * 2 + 1] << endl;
              
                do {
                    cout << "Digite: 1 - p/ alterar a primeira nota" << endl;
                    cout << "Digite: 2 - p/ alterar a segunda nota " << endl;
                    cout << "Digite: 0 - P/ Continuia " << endl;
                    cout << "Sua escolha: ";
                    cin >> opcao;

                    if (opcao == 1) {
                        cout << "Digite a nova primeira nota: ";
                        cin >> notas[pos * 2];
                    } else if (opcao == 2) {
                        cout << "Digite a nova segunda nota: ";
                        cin >> notas[pos * 2 + 1];
                    }
                } while (opcao != 0);
            } else {
                cout << "Aluno não encontrado." << endl;
            }
        }
    } while (alterarNota == 's' || alterarNota == 'S');

    cout << endl;
    cout << "Lista de alunos e notas:" << endl;
    for (size_t i = 0; i < nomes.size(); i++) {
        float media = calcularMedia(notas[i * 2], notas[i * 2 + 1]);
        cout << nomes[i] << ": Nota 1 = " << notas[i * 2] << ", Nota 2 = " << notas[i * 2 + 1]
                  << ", Média = " << media << " (" << (media >= 7.0f ? "Aprovado" : "Reprovado") << ")" << endl;
    }

    return 0;
}