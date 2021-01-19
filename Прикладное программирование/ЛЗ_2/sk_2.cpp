//https://stepik.org/lesson/13377/step/8?auth=login&unit=3571
/*Реализуйте макрос MAX от трёх параметров, который присваивает
целочисленной (int) переменной, переданной в качестве третьего аргумента,
наибольшее из значений, переданных в первых двух аргументах.*/
#define MAX(x, y, r)
#define MAX(x, y, r) (r = std::max (x, y)) /* присваивает r максимум из x и y */
#include <iostream>
int main ()
{
    int x, y, r;
    std::cin >> x >> y;
    MAX (x, y, r);
    MAX (x += y, y, r);
    std::cout << r;
    return 0;
}