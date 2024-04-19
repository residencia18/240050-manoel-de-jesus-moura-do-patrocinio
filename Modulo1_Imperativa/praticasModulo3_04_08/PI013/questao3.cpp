#include <iostream>
#include <iomanip>
#include <string>
using namespace std;


struct Produto {
    string codigo;
    string nome;
    double preco;
};

const int MAX_PRODUTOS = 300;
Produto produtos[MAX_PRODUTOS];
int totalProdutos = 0;


void inserirProduto() {
    if (totalProdutos >= MAX_PRODUTOS) {
        cout << "Limite de produtos cadastrados atingido." << endl;
        return;
    }

    Produto novoProduto;
    cout << "Informe um código de 13 caracteres numéricos para o produto: ";
    cin >> novoProduto.codigo;


    for (int i = 0; i < totalProdutos; i++) {
        if (produtos[i].codigo == novoProduto.codigo) {
            cout << "Já foi cadastrado um produto com o mesmo código, insira outro código." << endl;
            return;
        }
    }

    cout << "Digite o nome do produto (máximo 20 caracteres): ";
    cin.ignore();
    getline(cin, novoProduto.nome);

    cout << "Informe o preço do produto com duas casas decimais: ";
    cin >> novoProduto.preco;

    produtos[totalProdutos++] = novoProduto;
    cout << "Produto cadastrado com sucesso!" << endl;
}


void excluirProduto() {
    string codigo;
    cout << endl;
    cout << "Digite o código do produto a ser excluído: ";
    cin >> codigo;

    for (int i = 0; i < totalProdutos; i++) {
        if (produtos[i].codigo == codigo) {
            
            for (int j = i; j < totalProdutos - 1; j++) {
                produtos[j] = produtos[j + 1];
            }
            totalProdutos--;
            cout << "Produto excluído com sucesso!" << endl;
            return;
        }
    }

    cout << "Produto não encontrado." << endl;
}


void listarProdutos() {
    if (totalProdutos == 0) {
        cout << "Nenhum produto cadastrado." << endl;
        return;
    }

    cout << "Lista de produtos cadastrados:" << endl;
    cout << setw(15) << "Código" << setw(25) << "Nome" << setw(15) << "Preço" << endl;
    for (int i = 0; i < totalProdutos; i++) {
        cout << setw(15) << produtos[i].codigo << setw(25) << produtos[i].nome << setw(15) << fixed << setprecision(2) << produtos[i].preco << endl;
    }
}


void consultarPreco() {
    string codigo;
    cout << "Digite o código do produto para consultar o preço: ";
    cin >> codigo;

    for (int i = 0; i < totalProdutos; i++) {
        if (produtos[i].codigo == codigo) {
            cout << "Preço do produto '" << produtos[i].nome << "': R$ " << fixed << setprecision(2) << produtos[i].preco << endl;
            return;
        }
    }

    cout << "Produto não encontrado." << endl;
}

int main() {
    int escolha;

    do {
        cout << "\nMenu de Opções:" << endl;
        cout << "1. Inserir um novo produto" << endl;
        cout << "2. Excluir um produto cadastrado" << endl;
        cout << "3. Listar todos os produtos" << endl;
        cout << "4. Consultar o preço de um produto" << endl;
        cout << "0. Sair" << endl;
        cout << "Escolha uma opção: ";
        cin >> escolha;

        switch (escolha) {
            case 1:
                inserirProduto();
                break;
            case 2:
                excluirProduto();
                break;
            case 3:
                listarProdutos();
                break;
            case 4:
                consultarPreco();
                break;
            case 0:
                cout << "Saindo do programa." << endl;
                break;
            default:
                cout << "Opção inválida. Tente novamente." << endl;
        }
    } while (escolha != 0);

    return 0;
}
