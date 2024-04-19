#include <iostream>
#include <string>

using namespace std;

struct Empregado {
    string nome;
    string sobrenome;
    int ano_nascimento;
    string RG;
    int ano_admissao;
    double salario;
};

void Reajusta_dez_porcento(Empregado empregados[], int tamanho) {
    for (int i = 0; i < tamanho; i++) {
        empregados[i].salario *= 1.10;  
    }
}

int main() {
    const int MAX_EMPREGADOS = 50;
    Empregado empregados[MAX_EMPREGADOS];

    
    empregados[0] = {"Manoel", "Patrocinio", 1999, "7487569524", 2020, 7600.0};
    empregados[1] = {"Degas", "Coelho", 1980, "2158669875", 2012, 21000.0};

    
    int numero_empregados = 2;

    cout << "Salários antes do reajuste:" << endl;
    for (int i = 0; i < numero_empregados; i++) {
        cout << empregados[i].nome << " " << empregados[i].sobrenome << ": R$" << empregados[i].salario << endl;
    }

    
    Reajusta_dez_porcento(empregados, numero_empregados);

    cout << endl;
    cout << "Salários depois o reajuste:" << endl;
    for (int i = 0; i < numero_empregados; i++) {
        cout << empregados[i].nome << " " << empregados[i].sobrenome << ": R$" << empregados[i].salario << endl;
    }

    return 0;
}
