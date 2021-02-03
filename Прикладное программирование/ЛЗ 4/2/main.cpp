/*Задание 2. (Гусятинер Л.Б., МГОТУ ККМТ, 23.04.2020)*/

/*Разработать программу с меню для работы с массивом целых чисел из 10 элементов.
Пункты меню: Заполнение, Нахождение максимального, Нахождение суммы, Печать, Выход.
Для каждого действия (кроме выхода) разработать функцию, принимающую в качестве параметров
адрес первого элемента массива и количество элементов.
*/

#include <iostream>
using namespace std;


void filling(int *mas, int siz){
    int i;
    for (i=0; i<siz; ++i){
        cin >> mas[i];
    }
}

int findmax(int *mas, int siz){
    int i;
    int maxi;
    maxi = mas[0];
    for(i=0; i<siz; ++i){
        if (mas[i] > maxi){
           maxi = mas[i];
        }
    }
    return maxi;
}

void print(int *mas, int siz){
    int i;
    for (i=0; i<siz; ++i){
        cout << mas[i] << ' ';
    }
}

int sum(int *mas, int siz){
    int i = 0;
    int summ = 0;
    for(i=0; i<siz; ++i){
        summ += mas[i];
    }
    return summ;
}


int main(){
    int s = 10;
    int mas[s];
    int sw;

    cout << "1. Filling" << endl;
    cout << "2. Find max" << endl;
    cout << "3. Find sum" << endl;
    cout << "4. Print" << endl;
    cout << "5. Exit" << endl;
    cout << endl;

    cout << "select option" << endl;

    cin >> sw;
while(sw != 5){

    if (sw == 1){
        cout << "write mas, size = 10" << endl;
        filling(mas, s);
}
    if (sw == 2){
        cout << "max = ";
        cout << findmax(mas, s) << endl;
    }
    if (sw == 3){
        cout << "sum = ";
        cout << sum(mas, s) << endl;
    }

    if (sw == 4){
        cout << "your mas" << endl;
        print(mas, s);
        cout << endl;
    }
    if (sw == 5){
        break;
    }
    cout << "select option" << endl;

    cin >> sw;
}
    return 0;
}
