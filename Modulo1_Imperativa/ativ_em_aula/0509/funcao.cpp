#include <iostream>

using namespace std;


int fat (int n) {
        int fatorial = 1;
        for(int i = 1; i <= n; i++){
            fatorial *= i;
        }
        return fatorial;
}

void arrajos (int n, int p){
    
    cout << "O valor arranjo: " << fat(n) / fat(n - p) << endl;

}

void combinacao (int n, int p){
     
    cout << "a combinação  tem " << fat(n) / (fat(p) * fat(n - p)) << " maneiras" << endl;

}
int main(void){
    int n, p, escolha;
   
    cout << "Digite o total de itens: ";
    cin >> n;
    cout << "Digite quantos serao tomados: ";
    cin >> p;

    do{
        cout << "Digite 1 para calcular o arrajo ou 2 para calcular a combinacao ";
        cin >> escolha;

        if(escolha == 1){
            arrajos(n,p);
            
        }else if( escolha == 2){
            combinacao(n,p);
        }else{
            cout << "ai nao sujeito, me ajuda a te ajudar" << endl;
        }

    }while (escolha != 1 && escolha != 2);
   
    

    return 0;
}