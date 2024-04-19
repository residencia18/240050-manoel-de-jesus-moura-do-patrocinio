#include <iostream>
#include <fstream>
#include <string>

using namespace std;

void inputOnFile()
{
    ofstream arquivo_entrada;
    arquivo_entrada.open("exemplo.txt", ios_base::out);

    if (arquivo_entrada.is_open())
    {
        arquivo_entrada << "Escrevendo no arquivo 222. " << endl;
        arquivo_entrada << 20 + 20 << endl;
        arquivo_entrada.close();
    }
    else
    {
        cout << "Error ao abrir o arquivo" << endl;
    }
}

void readOnFile()
{
    ifstream arquivo_saida;
    arquivo_saida.open("exemplo.txt", ios_base::in);

    if (arquivo_saida.is_open())
    {
        string linha;
        while (arquivo_saida.eof() == false)
        {
            getline(arquivo_saida, linha);
            cout << linha << endl;
        }
        arquivo_saida.close();
    }
    else
    {
        cout << "Error ao abrir o arquivo" << endl;
    }
}

int menu()
{
    int op;

    do
    {
        cout << " 1 - Escrever no Arquivo " << endl;
        cout << " 2 - Ler o Arquivo " << endl;
        cout << " 0 - Sair " << endl;
        cout << " Sua escolha:  ";
        cin >> op;
    } while (op < 0 || op > 2);
    return op;
}
int main()
{

    int op;

    do
    {
        op = menu();

        switch (op)
        {
        case 1:
            system("clear");
            inputOnFile();
            break;
        case 2:
            system("clear");
            readOnFile();
            break;

        default:
            break;
        }
    } while (op != 0);

    return 0;
}