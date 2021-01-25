/*
https://stepik.org/lesson/����-�������-538/step/8?unit=861
�������� ����������� ������� ���������� ����������� ������ �������� ����
������������� ����� ����� (Greatest Common Divisor, GCD).
��� ����� �������������� ���������� ����������:

GCD(a, b) = GCD(b, a mod b)
GCD(0, a) = a
GCD(a, b) = GCD(b, a)
*/
#include <iostream>
using namespace std;
unsigned gcd(unsigned a, unsigned b)
{
    if (b!= 0)
    {
        return gcd (b, (a % b));
    }
    return a;
}
int main()
{
    int a, b;
    cin >> a >> b;
    cout << gcd(a, b);
    return 0;
}
