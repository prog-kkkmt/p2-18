/*Разработать программу с меню для работы с массивом целых чисел из 10 элементов.
Пункты меню: Заполнение, Нахождение максимального, Нахождение суммы, Печать, Выход.
Для каждого действия (кроме выхода) разработать функцию, принимающую в качестве параметров
адрес первого элемента массива и количество элементов.
Сделал: Сумин К.Е. группа П2-18
*/
#include <iostream>
#include <fstream>
#include <stdlib.h>
#include <ctime>


using namespace std;
int maks,summ=0;
void full(int* f, int n)//создание массива
{
    *(f+n)=-100+rand()%200;
    n--;
    if (n>-1)
    {
        return full(f,n);
    }
}
int max(int* f, int n)//максимальное число
{
    if ((n==10)||(n==9))
    {
        maks=*(f+n);
    }
    else
    {
        if(*(f+n)>maks)
        {
            maks=*(f+n);
        }
    }
    n--;
    if (n>-1)
    {
        return max(f,n);
    }
    return maks;
}
int sum(int* f, int n)//сумма
{
    if (n==10)
    {
        n--;
        return sum(f,n);
    }
    summ+=*(f+n);
    n--;
    if (n>-1)
    {
        return sum(f,n);
    }
}
    ofstream mas("mas.txt");
void fil(int* f, int n)//печать (запись в файл)
{
    if (n==10)
    {
        n=0;
        return fil(f,n);
    }
    mas<<*(f+n)<<' ';
    n++;
    if (n!=9)
    {
        return fil(f,n);
    }
    else
    {
        mas<<*(f+n)<<' ';
        mas.close();
    }

}
int main()
{
    setlocale(LC_ALL, "Russian");
    srand (time(NULL));
    int swit,a[10];
    int *f=&a[0];
    cout<<"Массив не составлен"<<endl<<"1)Заполнение"<<endl
    <<"2)Выход"<<endl;
    cin>>swit;
    switch (swit)
    {
        case 1:
        {
            full(f,10);
            break;
        }
        case 2:
        {
            return 0;
        }
    }
    system("cls");
    cout<<"1)Заполнение"<<endl
    <<"2)Нахождение максимального"<<endl
    <<"3)Нахождение суммы"<<endl
    <<"4)Печать"<<endl
    <<"5)Выход"<<endl;
while(swit!=5)
    {
        cout<<"Ваш массив: "<<endl;
        for(int i=0;i<10;i++)
        {
            cout << a[i]<<' ';
        }
        cout<<endl;
        cin>>swit;
        switch (swit)
        {
            case 1:
            {
                full(f,10);
                break;
            }
            case 2:
            {
                cout<<" Максимум: "<<max(f,10)<<endl;
                break;
            }
            case 3:
            {
                cout<<" Сумма: "<<sum(f,10)<<endl;
                break;
            }
            case 4:
            {
                fil(f,10);
                char kv='"';
                cout<<"Массив записан в "<<kv<<"mas.txt"<<kv<<endl;
                break;
            }
            case 5:
            {
                return 0;
            }
            default:
            {
                return 0;
            }
        }
    }
    return 0;
}
