#include <iostream>
#include <string>
#include <vector>

using namespace std;


class Paciente{
    string nome;
    string data_morte;
 
    public:

        void set_nome(string p_nome){
            this->nome = p_nome;
        }
        void set_data_morte(string p_data_morte){
            this->data_morte = p_data_morte;
        }

        string getNome(){
            return nome;
        }
        string get_data_morte(){
            return data_morte;
        }
};

class Mausoleu{
    string  setor;
    vector <Paciente> ListPacientes;

    public:
        void set_setor(string m_setor){
            this->setor = m_setor;
        }
        
        void set_ListPacientes(Paciente m_paciente){
            ListPacientes.push_back(m_paciente);
        }
        string getSetor(){
            return setor;
        }
        void listar_pacientes(){
            cout << " Local: " << getSetor() <<endl;

            for( auto &paciente : ListPacientes){
                cout <<endl << paciente.getNome()<<endl;
            }
        }
};
int main(void){
    Paciente p1,p2;
    Mausoleu m1;

    p1.set_nome(" fulano de tal");
    p2.set_nome(" ze ninguem");

    cout << endl << "--- Lista de pacientes --- " << endl;

    cout << p1.getNome() << endl;
    cout << p2.getNome() << endl;

    m1.set_setor("A1");
    m1.set_ListPacientes(p1);
    m1.set_ListPacientes(p2);

    cout << endl << "--- Lista de pacientes no mausoleus --- " << endl;
    m1.listar_pacientes();

    return 0;
}