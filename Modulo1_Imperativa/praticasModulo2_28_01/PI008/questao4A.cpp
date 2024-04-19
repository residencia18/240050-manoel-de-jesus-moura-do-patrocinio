#include <iostream>
#include <string>
#include <cctype>

using namespace std;

int main(void)
{
   int imagem[640][480];

   for (int i = 0; i < 640; i++)
   {
      for (int j = 0; j < 480; j++)
      {
         imagem[i][j] = rand() % 156;
      }
   }

   for (int i = 0; i < 640; i++)
   {
      for (int j = 0; j < 480; j++)
      {
        cout <<  imagem[i][j] << "\t";
      }
      cout << endl;
   }

   return 0;
}