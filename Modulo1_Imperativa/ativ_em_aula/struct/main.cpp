#include <iostream>
#include <string>

using namespace std;

struct str_data{
    int dia,mes,ano;
};

struct titulo_eleitor
{
    string nome,ti_numero,zona,secao,municipio,UF;
    str_data data_nasc;
    str_data data_emissao;
};

void ler_data(str_data *Data){
    cin >> Data->dia >> Data->mes >> Data->ano;

}
void mostra_data (str_data Data){
    cout << "Nascido em : " << Data.dia << " " << Data.mes << " " << Data.ano << endl;
}
void mostra_titulo (titulo_eleitor titulo){
    cout << "------ ELEITOR -----" << endl;
    cout << "Nome: " << titulo.nome << endl;
    cout << "Titulo: " << titulo.ti_numero << " Zona: " <<  titulo.zona << " Seção: " << titulo.secao << endl;
    mostra_data(titulo.data_nasc);
}


int main(void){

    titulo_eleitor titulo;

    cout << "Informe seu nome: ";
    getline(cin, titulo.nome);

    cout << "Dia mes e ano de nascimento: ";
    ler_data(&titulo.data_nasc);
    
    cin.ignore();
    cout << endl;

    cout << "Nº do titulo: ";
    getline(cin, titulo.ti_numero);

    cout << "Nº da zona eleitoral: ";
    getline(cin, titulo.zona);

    cout << "Nº da seção eleitoral: ";
    getline(cin, titulo.secao);


    cout << endl;

    mostra_titulo(titulo);

    return 0;
}