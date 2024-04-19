#include <iostream>
#include <string>
#include <vector>

using namespace std;

string compara(string word1, string word2)
{
    string  new_word;

    for (int i = 0; i < word1.length(); i++)
    {
      for (int j = 0; j < word2.length(); j++)
      {
        if(word1.at(i) == word2.at(j) ){
           new_word += word1.at(i) ;
        }

      }
     
    }

  return new_word;
}

int main(void)
{
    string newWord;
    newWord = compara("Manoel","Maneiro");
    cout << endl;
    cout << "Nova string: " << newWord << endl;
    return 0;
}
