#include <stdio.h>
#include <iostream>
#include <cmath>

using namespace std;

int main() {
    int aux, coun, Max=100, div;

    for(aux = 2 ;aux <= Max; aux++){
        div = 0;

        for(coun = 2 ; coun <= sqrt(aux) ; coun++)
            if(aux%coun==0)
                div++;

        if(!div)
            cout << aux << " ";
    }

    cout << endl;

    return 0;
}

//fonte: stackoverflow, faltou massa cinzenta pra resolver de cabeça kk