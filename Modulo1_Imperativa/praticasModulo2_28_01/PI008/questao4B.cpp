#include <iostream>
#include <string>
#include <cctype>

using namespace std;

int main(void)
{
   string wordlist[1][10];

   for (int j = 0; j < 10; j++)
   {

      for (int k = 0; k < 10; k++)
      {
         wordlist[0][k] += 'a' + rand() % ('z' - 'a');
      }
   }

   for (int k = 0; k < 10; k++)
   {
      wordlist[0][k].at(0) = toupper(wordlist[0][k].at(0));
      cout << wordlist[0][k] << "\t";
   }
   cout << endl;

   return 0;
}