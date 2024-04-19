#include <iostream>

using namespace std;

float calc_serie(int n)
{
    float s;

    for (int i = 1; i <= n; i++)
    {
        if(i == 1){
            s += 1/n;
        }else if(i ==  (n - 2)){
            s += (n -1) / 2;
        }else if(i == n){
            s += n/1;
        }else{
            s += i / (n - (i - 1));
        }
       
    }

    cout << fixed;
    cout.precision(2);
    cout << "Valor de S: " << s << endl;
  
}
int main(void)
{
    calc_serie(3);
    return 0;
}
