//Выполнили: Короленко И.Р., Кузнецов М.С., Слесарев А.М.
//Группа: ККМТ П2-18
//Задание: 2.2 Стек вызовов

#include <iostream>

using namespace std;

unsigned gcd(unsigned a, unsigned b){
   if(b==0)
       return a;
   return gcd(b,a%b);
}

int main(){
    int a,b;
    cin >> a >> b;
    cout << gcd(a,b);
}
