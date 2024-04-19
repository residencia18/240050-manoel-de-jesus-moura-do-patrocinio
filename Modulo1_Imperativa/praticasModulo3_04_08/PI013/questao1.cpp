#include <iostream>
#include <vector>
#include <string>
#include <ctime>
#include <iomanip>

using namespace std;

class Passageiro
{
public:
    string numero_assento;
    string data_hora;
    string cpf;
    string nome;
    int idade;

    Passageiro(string assento, string data_hora, string cpf, string nome, int idade)
        : numero_assento(assento), data_hora(data_hora), cpf(cpf), nome(nome), idade(idade) {}
};

class Viagem
{
public:
    string numero_viagem;
    string horario;
    vector<Passageiro> passagens_vendidas;

    Viagem(string numero, string horario)
        : numero_viagem(numero), horario(horario) {}

    void venderPassagem(Passageiro passageiro)
    {
        passagens_vendidas.push_back(passageiro);
    }

    double totalArrecadado()
    {
        return passagens_vendidas.size() * 80.0;
    }

    string nomePassageiroPorAssento(string assento)
    {
        for (const Passageiro &passageiro : passagens_vendidas)
        {
            if (passageiro.numero_assento == assento)
            {
                return passageiro.nome;
            }
        }
        return "Assento vazio";
    }

    double mediaIdadePassageiros()
    {
        int total_idade = 0;
        for (const Passageiro &passageiro : passagens_vendidas)
        {
            total_idade += passageiro.idade;
        }
        if (passagens_vendidas.size() == 0)
        {
            return 0.0;
        }
        return static_cast<double>(total_idade) / passagens_vendidas.size();
    }
};

class EmpresaOnibus
{
public:
    vector<Viagem> viagens;

    void criarViagens()
    {
        string horarios_ida[] = {"08:00", "10:00", "12:00", "14:00", "16:00"};
        string horarios_volta[] = {"09:00", "11:00", "13:00", "15:00", "17:00"};

        for (int i = 0; i < 5; i++)
        {
            viagens.push_back(Viagem("Ida " + to_string(i + 1), horarios_ida[i]));
            viagens.push_back(Viagem("Volta " + to_string(i + 1), horarios_volta[i]));
        }
    }

    Viagem *viagemMaisRentavel()
    {
        Viagem *viagem_rentavel = nullptr;
        double maior_arrecadacao = 0;

        for (Viagem &viagem : viagens)
        {
            double arrecadacao = viagem.totalArrecadado();
            if (arrecadacao > maior_arrecadacao)
            {
                maior_arrecadacao = arrecadacao;
                viagem_rentavel = &viagem;
            }
        }
        return viagem_rentavel;
    }
};

int main()
{
    EmpresaOnibus empresa;
    empresa.criarViagens();

    empresa.viagens[0].venderPassagem(Passageiro("A1", "2023-09-08 08:00", "59852196536", "Manoel", 24));
    empresa.viagens[1].venderPassagem(Passageiro("A2", "2023-09-08 16:00", "07958265236", "John", 25));
    empresa.viagens[0].venderPassagem(Passageiro("A2", "2023-09-08 08:00", "98566920545", "Marcela", 26));
    empresa.viagens[1].venderPassagem(Passageiro("B3", "2023-09-08 18:00", "07917857506", "Catarina", 56));
    empresa.viagens[2].venderPassagem(Passageiro("C1", "2023-09-08 14:00", "98633258892", "Livia", 22));

    cout << "Total arrecadado para a viagem 1: R$" << fixed << setprecision(2) << empresa.viagens[0].totalArrecadado() << endl;
    cout << "Media da idade dos passageiros da viagem 1: " << empresa.viagens[0].mediaIdadePassageiros() << endl;
    cout << "Passageiro no poltrona A2 da viagem 1: " << empresa.viagens[0].nomePassageiroPorAssento("A2") << endl;
    cout << "A viagem mais rentavel é no orário: " << empresa.viagemMaisRentavel()->horario << endl;

    return 0;
}
