#include <iostream>
#include <string>
#include <vector>

using namespace std;

class Estado{
    string nome, UF;

    public:
     Estado(string e_nome, string e_uf){
        this->nome = e_nome ;
        this->UF = e_uf;
     }

    void setEstadoNome(string e_nome){
        this->nome=e_nome;
    }
    void setEstadoUf(string e_UF ){
        this->UF = e_UF;
    }
    string getEstadoNome(){
        return nome;
    }

    string getEstadoUF(){
        return UF;
    }

};

class Cidade{
    string nome;
    Estado *do_Estado;
    public :

    Cidade (string cit_nome, Estado e_nome){
        this->nome = cit_nome; 
        this->do_Estado = &e_nome;
    }

    void listaCidade(){
        cout << "Cidade " << nome << " do estado " << do_Estado->getEstadoNome() << " UF: " << do_Estado->getEstadoUF() <<endl;
    }
    string getEstadoNome(){
        return do_Estado->getEstadoNome();
    }
    string getestadoUF(){
        return do_Estado->getEstadoUF();
    }
};
int main(){

    string e_nome, e_uf, c_nome;
    vector<Estado> vetorEstado;
    vector<Cidade> vetorCidade;

    for(int i = 0; i < 2; i++  ){
        cout << endl << "Digite o Nome do Estado: "; 
        getline(cin, e_nome);
        cout << endl << "Digite o UF do Estado: "; 
        getline(cin, e_uf);
        
        Estado estado(e_nome, e_uf);

        vetorEstado.push_back(estado);
    }

    cout << "--- Estados Cadastrados" << endl;
    for(auto &estado : vetorEstado  ){
        cout << estado.getEstadoNome() << " - " << estado.getEstadoUF() << endl;
    }

    for(auto &cit_objeto : vetorEstado  ){
        cout << endl << "Digite o Nome do Cidade: "; 
        getline(cin, c_nome);
       
        Cidade cidade(c_nome, cit_objeto);
        cidade.listaCidade() ;

        vetorCidade.push_back(cidade);
    }

    for(auto &cidade : vetorCidade  ){
        cidade.listaCidade();
    }
    

    return 0 ;
}