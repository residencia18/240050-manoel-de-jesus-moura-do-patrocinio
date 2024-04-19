#include <iostream>

using namespace std;

float conversao_teperatura(float celsius){
    float fahrenheit = (1.8 * celsius) + 32;
    return fahrenheit;
}

void entrada_dados() {

    float temp_celsius;

    cout << "Informe uma emperatura em Celsius: ";
    cin >> temp_celsius;

    float temp_fahrenheit = conversao_teperatura(temp_celsius);

    cout << endl;
    cout << "A temperatura " << temp_celsius << "°C Celsius convertida em Fahrenheit é: " << temp_fahrenheit << "°F" << endl; 
}

int main(){

    entrada_dados();

    return 0;
}