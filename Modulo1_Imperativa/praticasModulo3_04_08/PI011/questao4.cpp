#include <iostream>


using namespace std;

std::pair<int,int>calcula(int x, int y){
    x += y;
    y = x - y;

    return std::make_pair( x,y);
}
int main(void){
    int x = 10,y = 5;
    pair<int,int> p = calcula(x,y);

    cout << "valor de X: " << p.first << " ,valor de Y: " << p.second << endl;
    return 0 ;
}
