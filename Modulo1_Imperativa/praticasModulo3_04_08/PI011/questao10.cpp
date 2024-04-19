#include <iostream>
#include <string>
#include <vector>

using namespace std;

void acha_letra(string word, char letra)
{
    int tamanho;
    vector <int> vec;

    for (int i = 0; i < word.length(); i++)
    {
       if(word.at(i) == letra){
      
        vec.push_back(i);
       }
       
    }
    tamanho = vec.size();
   
    cout << "Posicoes onde a letra foi encontrada:" << endl;
    for (auto it = vec.begin(); it != vec.end(); it++){
        cout << *it << "\t";
    }
    cout <<endl;
    cout << "tamanho do vetor: " << tamanho << endl;
}
int main(void)
{
    acha_letra("manoel", 'a');
    return 0;
}
