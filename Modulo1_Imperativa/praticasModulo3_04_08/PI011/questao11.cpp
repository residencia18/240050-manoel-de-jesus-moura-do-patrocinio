#include <iostream>
#include <string>
#include <vector>

using namespace std;

string codifica(string word)
{
    string  word_codificada;

    for (int i = 0; i < word.length(); i++)
    {
       if(word.at(i) == 'z'){
         word_codificada += 'a';

       }else if(word.at(i) == 'Z'){
         word_codificada += 'A';
       }else{
         word_codificada += ++word.at(i);
       }
    }
    
    cout << "string codificada: " << word_codificada << endl;
   return word_codificada;
}

string decodifica(string word)
{
    string  word_codificada;

    for (int i = 0; i < word.length(); i++)
    {
       if(word.at(i) == 'a'){
         word_codificada += 'z';

       }else if(word.at(i) == 'Z'){
         word_codificada += 'A';
       }else{
         word_codificada += --word.at(i);
       }
    }
    
    cout << "string decodificada: " << word_codificada << endl;
   return word_codificada;
}
int main(void)
{
    string word_codificada, word_descodificada;
    word_codificada = codifica("Estruturas de Dados");
    cout << endl;
    word_descodificada = decodifica(word_codificada);
    return 0;
}
