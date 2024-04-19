#include <iostream>
#include <math.h>

using namespace std;


// int main(void){
//     float nota,soma = 0;
//     int count = 0;

//     while (count < 3){
//         cout << "informe uma nota: ";
//         cin >> nota;

//         count++;
//         soma += nota;
//     };
//     cout << "A média do aluno foi :" <<  soma / count << endl ;

//     return 0 ;
// }


// int main(void){
//     float temperatura = 0, maior = 0;
    
//     for ( int count = 0; count < 3; count ++){
//         cout << "informe uma temperatura: ";
//         cin >> temperatura;

//         if(maior < temperatura){
//             maior = temperatura;
//         }
       
//     };
//     cout << "A maior temperatura informada foi: " << maior << endl;

//     return 0 ;
// }

// int main(void){
//     int numero, soma;
    
//     cout << "informe um numero inteiro: ";
//     cin >> numero;

//     for ( int count = 0; count < numero; count ++){
//         soma += count;      
//     };
//     cout << "A soma é: " << soma << endl;

//     return 0 ;
// }

// int main(void){
//     int numero, fatorial = 1;
    
//     cout << "informe um numero inteiro: ";
//     cin >> numero;

//     for ( int count = 1; count <= numero; count ++){
//         fatorial *= count;      
//     };
//     cout << "O fatorial é: " << fatorial << endl;

//     return 0 ;
// }

// int main(void){
//     int numero, divisores = 0;
    
//     cout << "informe um numero inteiro: ";
//     cin >> numero;

//     cout << "Os divisores desse número são: " << endl;

//     for ( int count = 1; count <= numero; count ++){
//        if( numero % count == 0) {
//         divisores ++;
//          cout  << count << endl;

//        }
//     };
//     cout << "O total de divisores é: " << divisores << endl;

//     return 0 ;
// }

// int main(void){
//     int numero, divisores = 0;
    
//     cout << "informe um numero inteiro: ";
//     cin >> numero;

//     cout << "Os divisores desse número são: " << endl;

//     for ( int count = 1; count <= numero; count ++){
//        if( numero % count == 0) {
//         divisores ++;
//          cout  << count << endl;

//        }
//     };
//     cout << "O total de divisores é: " << divisores << endl;
//     if(divisores == 2){
//         cout << "Este número é primo " << endl;

//     }else{
//         cout << "Este número não é primo " << endl;

//     }
//     return 0 ;
// }


int main(void){
    int numero, divisores = 0;
    
    cout << "informe a quantidade de números para verificar: ";
    cin >> numero;

    cout << "Os divisores desse número são: " << endl;

    for ( int count = 1; count <= numero; count ++){
       if( numero % count == 0) {
        divisores ++;
         cout  << count << endl;

       }
    };
    cout << "O total de divisores é: " << divisores << endl;
    if(divisores == 2){
        cout << "Este número é primo " << endl;

    }else{
        cout << "Este número não é primo " << endl;

    }
    return 0 ;
}