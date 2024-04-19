#include <iostream>
#include <string>
#include <vector>
#include <stdio.h>

using namespace std;

struct Data
{
    int dia, mes, ano;
    int anosEntre(Data dataInit, Data dataFinal)
    {

        if (dataInit.ano < dataFinal.ano || dataInit.ano == dataFinal.ano)
        {
            if (dataInit.mes < dataFinal.mes || dataInit.mes == dataFinal.mes)
            {
                if (dataInit.dia < dataFinal.dia)
                {
                    return dataFinal.ano - dataInit.ano;

                }
            }
        }

        return 1;
    }
};

struct Veiculo
{
    string nome;
    string placa;
    string cpf_cliente;
    Data dataEmissao;
};
struct clientes
{
    string nome;
    string cpf;
    Data dataNascimento;
};

vector<clientes> listaClientes;
vector<Veiculo> listaVeiculo;

void lerCliente(clientes *clienteDados)
{
    system("clear");
    cout << "Digite seu nome completo: ";
    getline(cin, clienteDados->nome);

    cout << "Digite seu cpf: ";
    getline(cin, clienteDados->cpf);

    cout << endl;
    cin.ignore();
}

void lerVeiculo(Veiculo *veiculoDados)
{
    system("clear");
    cout << "Digite o nome do veículo: ";
    getline(cin, veiculoDados->nome);
    cout << "Digite a placa do veículo: ";
    getline(cin, veiculoDados->placa);
    cout << "Digite CPF do cliente deste veiculo: ";
    getline(cin, veiculoDados->cpf_cliente);

    cout << endl;
    cin.ignore();
}

void ListaClientes(vector<clientes> listaClientes1)
{
    system("clear");
    cout << endl;
    cout << " ----- Lista de CLientes -----" << endl;
    cout << endl;

    for (auto it = listaClientes1.begin(); it != listaClientes1.end(); it++)
    {
        cout << "Nome: " << it->nome << endl;
        cout << "CPF: " << it->cpf << endl;

        cout << endl;
        cout << "Veículos do cliente: " << endl;
        cout << endl;

        for (auto i = listaVeiculo.begin(); i != listaVeiculo.end(); i++)
        {
            if (it->cpf == i->cpf_cliente)
            {

                cout << "Nome do veículo: " << i->nome << endl;
                cout << "Placa do veículo: " << i->placa << endl;

                cout << endl;
            }
        }

        cout << endl;
        cout << "-----------------------" << endl;
        cout << endl;
        cout << endl;
    }
};

void mostraVeiculo(vector<Veiculo> listaVeiculo)
{
    system("clear");
    cout << endl;

    if (listaVeiculo.size() > 1)
    {
        cout << " ----- Lista de Veículos -----" << endl;
        cout << endl;
        for (auto it = listaVeiculo.begin(); it != listaVeiculo.end(); it++)
        {

            cout << "nome do veículo: " << it->nome << endl;
            cout << "placa do veículo: " << it->placa << endl;

            cout << endl;
            cout << "-----------------------" << endl;
            cout << endl;
            cout << endl;
        }
    }
    else
    {
        cout << " ----- Esse Cliente  Não Tem Veículos -----" << endl;
    }
};

void BuscaCPF()
{
    string cpf;

    system("clear");
    cout << "Digite o CPF do cliente para  a busca: ";
    getline(cin, cpf);
    for (auto it = listaClientes.begin(); it != listaClientes.end(); it++)
    {
        if (cpf == it->cpf)
        {
            cout << endl;
            cout << endl;
            cout << " ----- Resultado da Busca" << endl;

            cout << "Nome: " << it->nome << endl;
            cout << "CPF: " << it->cpf << endl;

            cout << endl;
            cout << endl;
        }
    }
};

void excluir_Client()
{
    string cpf;
    int cont = -1;

    system("clear");

    cout << "Digite o CPF do cliente que deseja excluir: ";
    getline(cin, cpf);

    vector<clientes>::iterator i;
    i = listaClientes.begin();

    for (auto it = listaClientes.begin(); it != listaClientes.end(); it++)
    {
        cont += 1;
        if (cpf == it->cpf)
        {

            advance(i, cont);
            listaClientes.erase(i);
            cout << "Excluído com sucesso !" << endl;
        }
    }
}

int MenuOpcao(void)
{
    int escolha;
    do
    {
        cout << "Escolha um serviço: " << endl;
        cout << endl;

        cout << "1 - p/ Novo cliente" << endl;
        cout << "2 - p/ Encontrar um cliente" << endl;
        cout << "3 - p/ Excluir cliente" << endl;
        cout << "4 - p/ Listar cliente" << endl;
        cout << "5 - p/ Cadastrar veículo" << endl;
        cout << "0 - p/ Encerrar programa " << endl;
        cout << "Sua escolha: ";
        cin >> escolha;
        cin.ignore();

    } while (escolha < 0 || escolha > 5);

    return escolha;
};
int main()
{
    clientes clienteDados;
    Veiculo veiculoDados;

    int opcao;

    do
    {
        opcao = MenuOpcao();

        switch (opcao)
        {
        case 1:
            lerCliente(&clienteDados);
            listaClientes.push_back(clienteDados);
            break;
        case 2:
            BuscaCPF();
            break;
        case 3:
            excluir_Client();
            break;
        case 4:
            ListaClientes(listaClientes);
            break;
        case 5:
            cout << "es 5" << endl;
            lerVeiculo(&veiculoDados);
            listaVeiculo.push_back(veiculoDados);
            break;
        }

    } while (opcao != 0);

    return 0;
}