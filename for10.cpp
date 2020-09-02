#include <iostream>
using namespace std;
int main()
{
int n;
cin >> n;//ввод
    int i;
    float sum = 0;//переменная типа флоат
    for  (i=1; i<=n; i++)
      sum += 1/(float)i; //делаем I переменной типа float(складываем дробные числа
    cout<<sum; //вывод
    return 0;
}
