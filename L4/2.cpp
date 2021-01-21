#include <iostream>
#include <stdlib.h>
int maximum, summa = 0;
void zapolnenie(int* x, int s)
{
    for(int i=0;i<s;i++)
    {
        std::cin >> *(x+i);
    }
}
int max(int* x, int s)
{
    if ((s==10)||(s==9))
    {
        maximum=*(x+s);
    }
    else
    {
        if(*(x+s)>maximum)
        {
            maximum=*(x+s);
        }
    }
    s--;
    if (s>-1)
    {
        return max(x, s);
    }
    return maximum;
}
int sum(int* x, int s)
{
    if (s==10)
    {
        s--;
        return sum(x, s);
    }
    summa+=*(x+s);
    s--;
    if (s>-1)
    {
        return sum(x, s);
    }
}
void vivod(int* x, int s)
{
    for(int i=0;i<s;i++)
    {
        std::cout << " " << x[i];
    }
}
int main()
{
    int b, c, s = 10;
    int a[s];
    int *y = &a[0];
    while(c!=5)
    {
        std::cout << "Заполнение - 1\nНахождение максимального - 2\nНахождение суммы - 3\nВывод - 4\nВыход - 5\n";
        std::cin >> c;
        switch(c)
        {
            case 1:
            {
                std::cout << "Ввести 10 элементов: \n";
                zapolnenie(y, s);
                std::cout << "\n";
                break;
            }
            case 2:
            {
                std::cout << "Максимальное число: \n" << max(y, s) << "\n";
                break;
            }
            case 3:
                std::cout << "Сумма: " << sum(y, 10) << std::endl;
                break;
            case 4:
            {
                std::cout << "Вывод: \n";
                vivod(y, s);
                std::cout << "\n";
                break;
            }
            default:
            {
                break;
            }
        }
        c == 0;
    }
    return 0;
}
