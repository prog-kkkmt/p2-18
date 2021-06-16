//Выполнили: Короленко И.Р., Кузнецов М.С., Слесарев А.М.
//Группа: ККМТ П2-18
//Задание: 1.8 Введение в синтаксис C++, часть 2

#include <iostream>

using namespace std;

int main(){
    int T,a,b;
    cin >> T;
    for (int i=0; i<T; i++){
        cin >> a >> b;
        cout<< a+b << endl;
    }
   return 0;
}
