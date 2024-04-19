#include <iostream>
#include <string>

using namespace std;
/*
    Exercício 4: Criando outro programa básico
        Crie um arquivo chamado meuprog2.cpp contendo um programa que peça ao
        usuário 2 números inteiros, A e B, e mostre na tela a soma, subtração, multiplicação,
        divisão e resto da divisão desses números.

*/

/*
Exercício 4: 

int main(void){
    string nome_do_usuário ;
    int numero1, numero2;

    cout << "Olá, Bem-vindo ao Result Operation " << endl;
    cout << "Vamos começar ... " << endl;
    cout << endl;

    cout << "Informe um número inteiro, ou sejá, sem ponto ou vingulas: ";
    cin >> numero1;

    cout << "Agora informe outro número inteiro: ";
    cin >> numero2;
    cout << endl;

    cout << "O resultado das 5 operações  usando os números " << numero1 << " e " << numero2 << " são:" << endl;
    cout << endl;

    cout << "   Soma: " << numero1 + numero2 << endl;
    cout << "   Subtração: " << numero1 - numero2 << endl;
    cout << "   Multiplicação: " << numero1 * numero2 << endl;
    cout << "   Divisão: " << numero1 / numero2 << endl;
    cout << "   Resto: " << numero1 % numero2 << endl;


    return 0;
}
*/


/* Exercício 5:  Utilize o comando search do MS-Code para trocar todas as variáveis do tipo int para
float, exceto o retorno da função main() que deve continuar como int.


Exercício 6: Transforme o programa do exercício 4 para trabalhar com números do
tipo float. Deverá ser o mesmo programa do exercício 4, mas as entradas e saídas devem ser
conforme o exemplo abaixo:
*/

int main(void){
    string nome_do_usuário ;
    float numero1, numero2, re;

    cout << "Olá, Bem-vindo ao Result Operation " << endl;
    cout << "Vamos começar ... " << endl;
    cout << endl;

    cout << "Informe um número inteiro, ou sejá, sem ponto ou vingulas: ";
    cin >> numero1;

    cout << "Agora informe outro número inteiro: ";
    cin >> numero2;
    cout << endl;

    cout << "O resultado das 5 operações  usando os números " << numero1 << " e " << numero2 << " são:" << endl;
    cout << endl;
    cout << fixed;
    cout.precision(1);
    re = numero1 + numero2; 
    cout << "   Soma: " << re << endl;
    cout << "   Subtração: " << numero1 - numero2 << endl;
    cout << "   Multiplicação: " << numero1 * numero2 << endl;
    cout << "   Divisão: " << numero1 / numero2 << endl;

    return 0;
}

/*
Exercício 7:Verificando Extensões Instaladas
Anote quais extensões existem instaladas atualmente na sua IDE.

Resposta:

    - C/C++ Estension Pack
    - C/C++ 
    - C/C++ Themes
    - C/C++ Compile Run
    - Material Icon Theme


*************** ********* ****************** ************** ***************** ********************** ****************

Exercício 8: Instalando Extensões
Instale duas extensões de sua preferência. Explique para que servem as extensões
instaladas e o que mudou na sua IDE após a instalação.

Resposta:

    - Live Serve: Inicie um servidor de desenvolvimento local com recurso de recarga ao vivo 
    para páginas estáticas e dinâmicas. Foi adicionado um icone "Go Live" na bordar inferior direita do vsCode para
     iniciar o serviço.

    - Bracket Pair Color DLW: Adiciona uma cor unica para cada chave e colchetes no código, para facilitar a 
        identificação do inicio e fim do escopo de uma função, principalmete quando trabalhamos como funções aninhadas.


*************** ********* ****************** ************** ***************** ********************** ****************

Exercício 9: Customizando a IDE - Temas
Instale o Tema Drácula na sua IDE. Escolha qual o melhor tema de sua preferência.
Descreva como você fez para configurar o tema da sua IDE.

Resposta: O tema escolhido foi Dracula Soft. Após perquisar pelo nome do tema no campo Extensions do vsCode e clicar em instalar
é aberto uma caixa de opções no topo do vscode para que você escolha entre o tema Dracula padrão ou Dracula Soft,
 logo após selecionar o tema é automaticamente aplicado ao vccode.



*/

