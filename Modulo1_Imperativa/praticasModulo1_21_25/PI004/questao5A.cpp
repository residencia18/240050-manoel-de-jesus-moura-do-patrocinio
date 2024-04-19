#include <iostream>
#include <string>
#include <climits>
using namespace std;

int main(void){

    int inteiro = 3;
    unsigned int unsigned_int = 3;
    unsigned long int unsigned_long_int;
    float flutuante = 3.56;
    long int long_int ;
    double doubleNum = 3.4;

    cout << " int: " << inteiro << " em boolean: "<< (bool)inteiro<< endl;
    cout << " unsigned int: " << unsigned_int << " em boolean: "<< (bool)unsigned_int<< endl;
    cout << " unsigned long int: " << unsigned_long_int << " em boolean: "<< (bool)unsigned_long_int<< endl;
    cout << " float: " << flutuante << " em boolean: "<< (bool)flutuante<< endl;
    cout << " long int: " << long_int << " em boolean: "<< (bool)long_int<< endl;
    cout << " double: " << doubleNum << " em boolean: "<< (bool)doubleNum<< endl;
    
    return 0;
}