#include <iostream>
#include <string>
#include <cctype>


using namespace std;



int main(void){
   string word1, word2;

   for(int i = 0; i < 10; i++){
      word1 += 'a' + rand()%('z' - 'a');
      word2 += 'a' + rand()%('z' - 'a');
   }
   word1[0] = toupper(word1.at(0));
   word2[0] = toupper(word2.at(0));


   if(word1.at(0) > word2.at(0)){
      cout << word2 << " " << word1 << endl;
   }else{
      cout << word1 << " " << word2 << endl; 
   }
  
   return 0;
}