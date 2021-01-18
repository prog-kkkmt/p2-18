//Выполнил задание: Пилипушко Андрей П2-18
//Задание: 1.8 Введение в синтаксис C++, часть 2

#include <iostream>

using namespace std;

int main(){
    int n, p;
    cin >> n;
    for(int i = 0; i < n; i++){
        cin >> p;
        int j = 0;
        int a = 2;
        while (a<=p)
        {
            a *= 2;
            j++;
        }
        cout << j << endl;
    }
return 0;
}
