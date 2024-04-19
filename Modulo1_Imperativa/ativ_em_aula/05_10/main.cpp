#include <iostream>
#include <string>
#include <vector>
#include <fstream>

using namespace std;

class Date
{
    int dia, mes, ano;
};
class Usuario
{
    string cpf, nome, endereco, telefone;
    vector<Usuario> arrayUsers;

public:
    void setCPF(string CPF)
    {
        cpf = CPF;
    }
    void setNome(string Nome)
    {
        nome = Nome;
    }
    void setEndereco(string Endereco)
    {
        endereco = Endereco;
    }
    void setTelefone(string Telefone)
    {
        telefone = Telefone;
    }
    string getCPF()
    {
        return cpf;
    }
    string getNome()
    {
        return nome;
    }
    string getEndereco()
    {
        return endereco;
    }
    string getTelefone()
    {
        return telefone;
    }

    void addUser(Usuario novoUser)
    {
        arrayUsers.push_back(novoUser);
    }
    void buscaUser(string cpfUser)
    {
        for (auto &user : arrayUsers)
        {
            if (user.getCPF() == cpfUser)
            {
                cout << user.getNome() << endl;
                cout << user.getCPF() << endl;
                cout << user.getTelefone() << endl;
                cout << user.getEndereco() << endl
                     << endl;
            }
        }
    }

    void listaUser()
    {
        for (auto &user : arrayUsers)
        {
            cout << user.getNome() << endl;
            cout << user.getCPF() << endl;
            cout << user.getTelefone() << endl;
            cout << user.getEndereco() << endl
                 << endl;
        }
    }

    void removeUsuariosOnFile(Usuario user)
    {

        ofstream outuser;
        outuser.open("usuarios.txt", ios_base::out);
        if (outuser.is_open())
        {
            outuser << endl;
            outuser.close();
        }
    }

    void deleteUser(string cpfUser)
    {
        int cont = -1;

        for (auto &user : arrayUsers)
        {
            cont += 1;
            if (user.getCPF() == cpfUser)
            {
                buscaUser(cpfUser);
            }
        }
    }

    void addUsuarioOnFile(Usuario user)
    {
        ofstream outuser;
        outuser.open("usuarios.txt", ios_base::app);
        if (outuser.is_open())
        {
            outuser << user.getNome() << endl;
            outuser << user.getCPF() << endl;
            outuser << user.getEndereco() << endl;
            outuser << user.getTelefone() << endl;
            outuser.close();
        }
    }

    void resgatarDadosUsers()
    {
        Usuario user;
        ifstream arquivo_saida;
        arquivo_saida.open("usuarios.txt", ios_base::in);

        if (arquivo_saida.is_open())
        {
            string linha1, linha2, linha3, linha4;
            while (arquivo_saida.eof() == false)
            {
                getline(arquivo_saida, linha1);
                getline(arquivo_saida, linha2);
                getline(arquivo_saida, linha3);
                getline(arquivo_saida, linha4);

                user.setNome(linha1);
                user.setCPF(linha2);
                user.setEndereco(linha3);
                user.setTelefone(linha4);

                arrayUsers.push_back(user);
            }
            arquivo_saida.close();
        }
        else
        {
            cout << "Error ao abrir o arquivo" << endl;
        }
    }

    void alterarUser(string cpfUser)
    {
        string cpf, nome, endereco, telefone, cpfbusca;
        cout << "--- Resultado da busca ---" << endl
             << endl;
        for (auto &user : arrayUsers)
        {

            if (user.getCPF() == cpfUser)
            {
                buscaUser(cpfUser);

                cout << endl;
                cout << "Informe o nome: ";
                getline(cin, nome);

                user.nome = nome;

                cout << "Informe o CPF: ";
                getline(cin, cpf);

                user.setCPF(cpf);

                cout << "Informe o endereco: ";
                getline(cin, endereco);

                user.setEndereco(endereco);

                cout << "Informe o telefone: ";
                getline(cin, telefone);
            }
        }

        for (Usuario user : arrayUsers)
        {
            removeUsuariosOnFile(user);
        }
        for (Usuario user : arrayUsers)
        {
            addUsuarioOnFile(user);
        }
        arrayUsers.clear();
    }
};
void GerenciaUsuario()
{
    int escolha;

    Usuario user;
    user.resgatarDadosUsers();
    string cpf, nome, endereco, telefone, cpfbusca;

    do
    {
        cout << endl
             << " 1 - Adicionar Usuário" << endl;
        cout << " 2 - Listar Usuário" << endl;
        cout << " 3 - Buscar Usuário(CPF)" << endl;
        cout << " 4 - Alterar Usuário(CPF)" << endl;
        cout << " 5 - Excluir Usuário" << endl;
        cout << " 0 - Sair" << endl;
        cout << " Sua escolha: ";
        cin >> escolha;
        cin.ignore();
    } while (escolha < 0 || escolha > 5);

    switch (escolha)
    {
    case 1:
        system("clear");

        cout << "Informe o nome: ";
        getline(cin, nome);

        user.setNome(nome);

        cout << "Informe o CPF: ";
        getline(cin, cpf);

        user.setCPF(cpf);

        cout << "Informe o endereco: ";
        getline(cin, endereco);

        user.setEndereco(endereco);

        cout << "Informe o telefone: ";
        getline(cin, telefone);

        user.setTelefone(telefone);
        user.addUser(user);
        user.addUsuarioOnFile(user);
        break;

    case 2:

        system("clear");
        cout << "--- Lista de Usuario ---" << endl;

        user.listaUser();
        break;
    case 3:
        system("clear");

        cout << "Informe o CPF de busca: ";
        getline(cin, cpfbusca);

        cout << "--- Resultado da Busca ---" << endl;
        user.buscaUser(cpfbusca);

        break;
    case 4:
        cpfbusca = "";

        system("clear");
        cout << "Digite o CPF do usuário que deseja alterar: ";
        getline(cin, cpfbusca);

        user.alterarUser(cpfbusca);

        break;
    case 5:
        cpfbusca = "";

        system("clear");
        user.listaUser();
        cout << "Digite o CPF do usuário que deseja excluir: ";
        getline(cin, cpfbusca);

        user.alterarUser(cpfbusca);

        break;
    default:
        break;
    }
}

class Funcionario : public Usuario
{
};
class Cliente : public Usuario
{
    string habilitacao;
    vector<Cliente> arrayClient;

public:
    void setHabilitacao(string hablit)
    {
        habilitacao = hablit;
    }
    string getHabilitacao()
    {
        return habilitacao;
    }
    void addCliente(Cliente novoCliente)
    {
        arrayClient.push_back(novoCliente);
    }
    void buscaCliente(string cpfCliente)
    {
        for (auto &cliente : arrayClient)
        {
            if (cliente.getCPF() == cpfCliente)
            {
                cout << cliente.getNome() << endl;
                cout << cliente.getCPF() << endl;
                cout << cliente.getTelefone() << endl;
                cout << cliente.getEndereco() << endl
                     << endl;
            }
        }
    }

    void listaCientes()
    {
        for (auto &cliente : arrayClient)
        {
            cout << cliente.getNome() << endl;
            cout << cliente.getCPF() << endl;
            cout << cliente.getTelefone() << endl;
            cout << cliente.getEndereco() << endl
                 << endl;
        }
    }

    void alterarCliente(string cpfCliente)
    {
        int cont = -1;

        for (auto &cliente : arrayClient)
        {
            cont += 1;
            if (cliente.getCPF() == cpfCliente)
            {
                buscaCliente(cpfCliente);
            }
        }
    }
    void addClientOnFile(Cliente cliente)
    {
        ofstream outCliente;
        outCliente.open("clientes.txt", ios_base::app);
        if (outCliente.is_open())
        {
            outCliente << cliente.getNome() << endl;
            outCliente << cliente.getHabilitacao() << endl;
            outCliente << cliente.getCPF() << endl;
            outCliente << cliente.getTelefone() << endl;
            outCliente << cliente.getEndereco() << endl;
            outCliente << " " << endl;

            outCliente.close();
        }
        else
        {
            cout << "Error ao abrir o arquivo clientes.txt" << endl;
        }
    }
};

class Aluguel
{
    int id;
    Cliente *cliente;
    Funcionario *funcionario;
    Date dataInicio;
    Date dataTermino;
    Date dataDevolucao;
    float desconto, adicional;
};

vector<Funcionario> arrayFuncio;

int MenuGeral()
{
    int escolha;

    do
    {
        cout << " 1 - Gerenciar Usuário" << endl;
        cout << " 2 - Gerenciar Fucionário" << endl;
        cout << " 3 - Gerenciar Cliente" << endl;
        cout << " 0 - Sair" << endl;
        cout << " Sua escolha: ";
        cin >> escolha;
        cin.ignore();
    } while (escolha < 0 || escolha > 3);
}

int main()
{
    int escolha;

    do
    {
        escolha = MenuGeral();

        switch (escolha)
        {
        case 1:

            GerenciaUsuario();
            break;

        case 2:

            break;
        case 3:

            break;
        default:
            break;
        }

    } while (escolha != 0);

    return 0;
}