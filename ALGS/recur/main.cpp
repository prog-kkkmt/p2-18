//ќписать рекурсивную функцию Fact(N) вещественного типа, вычисл€ющую значение факториала

#include <iostream>


using namespace std;

float Fact(float n){
if(n == 1 || n == 0){ // 1! = 1,  0! = 1//а также дл€ выхода из рекурсивной функции;
    return 1;
}
float answer; //переменна€ с ответом
answer = n * Fact(n - 1); // рекурси€, входное число умножаетс€ на результат выполнени€ себ€ пока не будет 1;
return answer;//возвращает ответ
}

int main()
{
    int a;//ввод числа
    cout << "enter n! ";
    cin >> a;
    //вывод резалта
    cout << "asnwer = " << Fact(a);
return 0;
}
