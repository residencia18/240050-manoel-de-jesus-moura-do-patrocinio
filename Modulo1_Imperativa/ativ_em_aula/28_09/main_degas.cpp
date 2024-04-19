#include <iostream>
#include <string.h>
#include <vector>
#include <fstream>

using namespace std;

class Data
{
    int dia, mes, ano;

public:
    string geraString()
    {
        string dataStr = to_string(dia);
        dataStr.append("/");
        dataStr.append(to_string(mes));
        dataStr.append("/");
        dataStr.append(to_string(ano));
        return dataStr;
    }
    void setDia(int _dia)
    {
        dia = _dia;
    };
    void setMes(int _mes)
    {
        mes = _mes;
    };
    void setAno(int _ano)
    {
        ano = _ano;
    };
    int getDia(int _dia)
    {
        dia = _dia;
    };
    int getMes(int _mes)
    {
        mes = _mes;
    };
    int getAno(int _ano)
    {
        ano = _ano;
    };
};

class paciente
{
    string nome;
    Data dt_morte;
    int id;

public:
    static paciente leDados()
    {
        system("clear");
        paciente novoPaciente;
        Data dtMorte;
        string nome;

        int dia, mes, ano;

        cout << " --- Novo paciente ---" << endl;
        cout << "Digite o nome: ";
        getline(cin, nome);
        novoPaciente.setNome(nome);

        cout << "Digite a data (dia/mes/ano): ";
        cin >> dia >> mes >> ano;
        dtMorte.setDia(dia);
        dtMorte.setMes(mes);
        dtMorte.setAno(ano);
        novoPaciente.setDtMorte(dtMorte);
        cin.ignore();
        return novoPaciente;
    }
    void listaDados()
    {
        cout << endl
             << "--- Lista de Pacientes --" << endl;
        cout << "ID: " << getId() << endl;
        cout << "Paciente: " << getNome() << endl;
        cout << "Falecido em " << getdtMorte().geraString();
    }

    void setNome(string _nome)
    {
        nome = _nome;
    }
    void setDtMorte(Data _dataMorte)
    {
        dt_morte = _dataMorte;
    }
    int getId()
    {
        return id;
    }
    string getNome()
    {
        return nome;
    }

    Data getdtMorte()
    {
        return dt_morte;
    }
};

class mausoleu
{
    int id;
    string localizacao;
    vector<paciente> pacientes;

public:
    mausoleu()
    {
        id++;
    }
    static mausoleu leNovoMausoleu()
    {
        mausoleu novoMausoleu;
        string local;
        //system("clear");
        cout << "Digite a localicacao do mausoleu: ";
        getline(cin, local);

        novoMausoleu.setLocalizacao(local);
        return novoMausoleu;
    }
    void listaDados()
    {
        cout << endl
             << "ID: " << getId() << endl;
        cout << "Local: " << getLocalizacao() << endl;
        for (paciente p : pacientes)
        {
            p.listaDados();
        }
        cout << endl;
    }
    void recepciona(paciente _paciente)
    {
        pacientes.push_back(_paciente);
    }
    void setLocalizacao(string _localizacao)
    {
        localizacao = _localizacao;
    }
    void setId(string _id){
        this->id = stoi(_id);
    }
    int getId()
    {
        return id;
    }
    string getLocalizacao()
    {
        return localizacao;
    }

    void listaPacientes()
    {
        for (paciente p : pacientes)
        {
            p.listaDados();
        }
    }
};

int main()
{
    vector<mausoleu> mausoleus;
    int op;

    do
    {
        cout << "Opcoes" << endl;
        cout << "1. Incluir Mausoleu" << endl;
        cout << "2. Listar Mausoleus" << endl;
        cout << "3. Recepcionar paciente" << endl;
        cout << "0. Sair" << endl;
        cout << "Digite opcao: ";
        cin >> op;
        cin.ignore();
        if (op == 1)
        {

            mausoleu novoDoArquivo;
            int cont = 0;

            ifstream arquivo_saida;
            arquivo_saida.open("mausoleus.txt", ios_base::in);

            if (arquivo_saida.is_open())
            {
                string linha;
                while (arquivo_saida.eof() == false)
                {
                    getline(arquivo_saida, linha);
                    if((cont % 2) != 0 ){
                        novoDoArquivo.setLocalizacao(linha);
                        mausoleus.push_back(novoDoArquivo);

                    }

                    cont += 1;
                }
                arquivo_saida.close();
            }
            else
            {
                cout << "Error ao abrir o arquivo" << endl;
            }

            mausoleu novo = mausoleu::leNovoMausoleu();
            mausoleus.push_back(novo);

            ofstream outMausleos;
            outMausleos.open("mausoleus.txt", ios_base::app);
            if (outMausleos.is_open())
            {
                outMausleos << novo.getId() << endl;
                outMausleos << novo.getLocalizacao() << endl;
                outMausleos.close();
            }
        }
        if (op == 2)
        {
            system("clear");
            cout << endl
                 << " -- Lista de mausoleu --" << endl;
            for (mausoleu m : mausoleus)
            {
                m.listaDados();
            }
        }
        if (op == 3)
        {
            int idMausaoleu;
            paciente novoPac = paciente::leDados();

            for (mausoleu m : mausoleus)
            {
                m.listaDados();
            }
            cout << endl
                 << "Informe o ID do mausoleu para sepultar esse morto: ";
            cin >> idMausaoleu;
            for (mausoleu m : mausoleus)
            {
                if (m.getId() == idMausaoleu)
                {
                    m.recepciona(novoPac);
                    cout << endl
                         << "Relacinado com sucesso !" << endl;
                    m.listaDados();
                }
            }
            // localizar um mausoleu
            // inserir paciente no mausoleu
        }
    } while (op != 0);
    return 0;
}