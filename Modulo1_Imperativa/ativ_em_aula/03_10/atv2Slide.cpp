#include <iostream>
#include <string>
#include <math.h>

using namespace std;

class Forma{
    
    public:
        void calcularArea();
};

class Retanguro:Forma{
   public:
        void calcularArea(float base, float altura){
            cout<<"Area do Retangulo: " << base * altura << endl;
        }
};
class Circulo:Forma{
   float pi = 3.14;
   
   public: 
   void calcularArea(float raio){
        cout<<"Area do Circulo: " << pi * (pow(raio,2)) << endl;
   }
};
int main(){
   Retanguro retangulo;
   Circulo circulo;

   retangulo.calcularArea(3.5,2.5);
   circulo.calcularArea(2);
    return 0 ;
}