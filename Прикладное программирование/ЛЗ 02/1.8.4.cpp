//Выполнили: Короленко И.Р., Кузнецов М.С., Слесарев А.М.
//Группа: ККМТ П2-18
//Задание: 1.8 Введение в синтаксис C++, часть 2

#include <iostream>

using namespace std;

int power(int x, unsigned p){
    int answer = 1;
    for(int i=1; i <= p; i++){
        answer *= x;
    }
  return answer;
}

int main(){
    int a,b;
    cin >> a >> b;
    cout << power(a,b);
}
