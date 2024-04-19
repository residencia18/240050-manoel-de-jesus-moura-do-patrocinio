#include <iostream>
#include <string>

using namespace std;

/*
    Exercício 1: Criando um Projeto no MS-Code
        Crie uma pasta chamada Projeto1

    Exercício 2: Criando um programa básico
        Crie um arquivo chamado meuprog1.cpp contendo um programa em C++ que peça o
        nome_do_usuário e mostre a mensagem “Bom dia <nome_do_usuário>
    Exercício 3: Compilando o programa
        Compile e depura (tire os erros) do programa criado.

*/
int main(void){
    string nome_do_usuário ;

    cout << "Olá, Qual o seu nome: ";
    cin >> nome_do_usuário;

    cout << "Que bom te vê aqui " << nome_do_usuário << ". Seja bem vindo !" << endl;


    return 0;

}