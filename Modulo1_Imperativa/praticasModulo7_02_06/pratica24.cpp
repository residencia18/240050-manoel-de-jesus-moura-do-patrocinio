#include <iostream>
#include <string>
#include <vector>
#include <fstream>

using namespace std;


class Dependente{
    string nome;
    int cliente_id;


    public:

    Dependente (string _nome, int cli_id ){
        nome = _nome;
        cliente_id = cli_id;

    }
    void setNome(string _nome){
        nome = _nome;
    }
    string getNome(){
        return this->nome;
    }
    void setClienteId(int cli_id){
        cliente_id = cli_id;
    }
    int getClienteId(){
        return cliente_id;
    }
    void addDependenteOnFile(Dependente dep)
        {
            ofstream outDependent;
            outDependent.open("dependentes.txt", ios_base::app);
            if (outDependent.is_open())
            {
                outDependent << dep.getClienteId() << endl;
                outDependent << dep.getNome() << endl;
                outDependent.close();
            }else{
                cout <<"erro na abertura do arquivo clientes" <<endl;
            }
        }

};
int id = 0;

class Cliente
{
    string cpf, nome;
    vector<Dependente> listaDependente;


    public:
        Cliente (int _id, string _nome, string _cpf){
            nome = _nome;
            cpf = _cpf;

            if(_id > 0){
                id = _id;
            }else{
                id++;

            }

        }
      
        void setCPF(string CPF)
        {
            cpf = CPF;
        }
        void setNome(string Nome)
        {
            nome = Nome;
        }
        string getCPF()
        {
            return cpf;
        }
        string getNome()
        {
            return nome;
        }

        int getId(){
            return id;
        }
        void setId(int cli_id){
            id = cli_id;
        }

        void addDependenteOnArray( Dependente dep){
            listaDependente.push_back(dep);
        }

        void listarClientes(vector<Cliente> arrayClientes){

            for( auto cli : arrayClientes){
                cout << "Nome: " << cli.getNome() <<endl;
                cout << "CPF: " << cli.getCPF() <<endl<<endl;

                cout << endl << "--- dependentes ---" << endl;
                for( auto dep : listaDependente){
                    if(dep.getClienteId() == cli.getId()){
                        cout << "Nome: " << dep.getNome() <<endl;
                        cout << "cliente id: " << dep.getClienteId() <<endl<<endl;
                    }
                }
            }
          

        }
       

        // functions to manager file txt
        void addClientOnFile(Cliente cliente)
        {
            ofstream outClient;
            outClient.open("clientes.txt", ios_base::app);
            if (outClient.is_open())
            {
                outClient << cliente.getId() << endl;
                outClient << cliente.getNome() << endl;
                outClient << cliente.getCPF() << endl;
                outClient.close();
            }else{
                cout <<"erro na abertura do arquivo clientes" <<endl;
            }
        }
        vector<Cliente> resgatarDadosUsers()
        {
           
            vector <Cliente> arrayCliente;
            ifstream arquivo_saida;
            arquivo_saida.open("clientes.txt", ios_base::in);

            if (arquivo_saida.is_open())
            {
                string id, nome, cpf;
                while (arquivo_saida.eof() == false)
                {
                    getline(arquivo_saida, id);
                    getline(arquivo_saida, nome);
                    getline(arquivo_saida, cpf);


                    Cliente cliente (stoi(id),nome,cpf);
                    
                    arrayCliente.push_back(cliente);

                }
                arquivo_saida.close();
                return arrayCliente;
            }
            else
            {
                cout << "Error ao abrir o arquivo" << endl;
            }
        }

        
};

class Evento{
    string nome, duracao,data;

    public: 
    void setNome(string _nome) {
        this->nome = _nome;
    }
    void setDuracao(string _time){
        this ->duracao=_time;
    }
    string getNome() {
        this->nome ;
    }
    string getDuracao(){
        this ->duracao;
    }
};

class Roteito : public Evento{
    vector <string>  lista = {"primeira_parada","segunda_parada","terceira_parada"};
};
class Deslocamento : public Evento{
    string do_ponto, para_ponto;

    public:
        void setDoPonto(string valor){
            this->do_ponto = valor;
        }
        void setParaPonto(string valor){
            this->para_ponto = valor;
        }
        string getPartinda(){
            return this->do_ponto;
        }

        string getChegada(){
            return this->para_ponto;
        }
};

class Pernoite : Evento{
    int hora;

    public:
    void setHora(int _hora){
        this->hora= _hora;
    }
};




void gerenciarCliente(){
    int opcao, escolhaDep ;
    string cpf, nome;
    vector<Cliente> arrayClientes;



    do
    {
        cout << endl
             << " 1 - Adicionar Cliente" << endl;
        cout << " 2 - Listar Clientes" << endl;
        cout << " 3 - Buscar Usuário(CPF)" << endl;
        cout << " 4 - Excluir Usuário" << endl;
        cout << " 0 - Sair" << endl;
        cout << " Sua escolha: ";
        cin >> opcao;
        cin.ignore();

        if (opcao == 1)
        {
    
            system("clear");

            cout << "Informe o nome: ";
            getline(cin, nome);


            cout << "Informe o CPF: ";
            getline(cin, cpf);

            Cliente novoCliente(0, nome,cpf);
            arrayClientes.push_back(novoCliente);
            novoCliente.addClientOnFile(novoCliente);


            do{

                cout << "Deseja adicionar um dependente ?" <<endl;
                cout<< "1-Sim | 0-Nao : ";
                cin>>escolhaDep;
                cin.ignore();

                if(escolhaDep == 1){
                    nome = "";
                    cout << "Informe o nome do dependente: ";
                    getline(cin, nome);
                    Dependente dep (nome, novoCliente.getId());

                    novoCliente.addDependenteOnArray(dep);
                    dep.addDependenteOnFile(dep);


                }else{
                    break;
                }

            }while(escolhaDep != 0 );
        }
        else if(opcao == 2){
            system("clear");


            cout << endl << "--- Lista de Cliente ---" <<endl;
            Cliente novoCliente(0, "","");
            novoCliente.listarClientes(arrayClientes);

        }else{
            break;
        }
    } while (opcao != 0);

    
};
int main(){
    int opcao;
    vector<Cliente> arrayClientes;

    do
    {
        cout << endl
             << " 1 - Gerenciar Clientes" << endl;
        cout << " 2 - Gerenciar Eventos" << endl;
        cout << " 3 - Gerenciar Pacotes" << endl;
        cout << " 0 - Voltar" << endl;
        cout << " Sua escolha: ";
        cin >> opcao;
        cin.ignore();
    } while (opcao < 0 || opcao > 4);

    switch (opcao)
    {
    case 1:
        gerenciarCliente();
        break;
    
    default:
        break;
    }

    return 0;
}