#include <iostream>
#include <string>
#include <float.h>

using namespace std;

int main(void)
{
    float pi = 3.14159265358979323846;

    cout << fixed;
    cout.precision(2);
    cout << "Valor de PI: " << pi << endl;

    cout.precision(4);
    cout << "Valor de PI: " << pi << endl;

    cout.precision(8);
    cout << "Valor de PI: " << pi << endl;

    cout.precision(16);
    cout << "Valor de PI: " << pi << endl;

    

    return 0;
}