//Выполнили: Короленко И.Р., Кузнецов М.С., Слесарев А.М.
//Группа: ККМТ П2-18
//Задание: 1.8 Введение в синтаксис C++, часть 2

#include <iostream>

using namespace std;

int main(){
    char c = '\0';
    bool a = true;
    while (cin.get(c)){
        if (c!=' '){
            cout << c;
            a = true;
        }
        else if(a){
            cout << c;
            a = false;
        }
    }
	return 0;
}
