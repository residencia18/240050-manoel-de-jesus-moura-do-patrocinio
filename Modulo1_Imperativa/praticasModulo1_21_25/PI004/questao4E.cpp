#include <iostream>
#include <string>
#include <float.h>

using namespace std;

int main(void)
{
    float pi = 3.14159265358979323846;
    double pid = pi;

    cout << fixed;
    cout.precision(2);
    cout << "Valor de PI: " << pi << endl;
    cout << "Valor de PID: " << pid << endl;

    cout << endl;

    cout.precision(4);
    cout << "Valor de PI: " << pi << endl;
    cout << "Valor de PID: " << pid << endl;

    cout << endl;

    cout.precision(8);
    cout << "Valor de PI: " << pi << endl;
    cout << "Valor de PID: " << pid << endl;

    cout << endl;

    cout.precision(16);
    cout << "Valor de PI: " << pi << endl;
    cout << "Valor de PID: " << pid << endl;

    
    // Aparentimente nenhuma diferença
    return 0;
}