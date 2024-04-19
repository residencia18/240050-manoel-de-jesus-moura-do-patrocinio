#include <iostream>
#include <string>

using namespace std;

class Animal{
    private:
        string nome;
        int idade;
    public:
        void fazerSom();
};

class Cachorro:Animal{
    public:
        void fazerSom(){
            cout <<"Au Au" << endl;
        }
};
int main(){
    Animal anima;
    Cachorro cachorro;

    cachorro.fazerSom();
    return 0 ;
}