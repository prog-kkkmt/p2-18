/*
� ���� ��������� ���������� ��������� �������:
int foo(int n) {
    if (n <= 0)
        return 1;
    return foo((n * 2) / 3) + foo(n - 2);
}
����� ���������, ������� ����� ��� ����� ������� ������� foo,
���� �� ������� � ���������� 3 (�.�. foo(3)). ����� ������ ����� ���� ����� ���������.

���������: ��� ������� ���� ������ ����� ������� ���������� ������ ����������� �������.
*/
#include <iostream>
using namespace std;
int i = 0;
int foo(int n)
{
    i ++;
    if (n <= 0)
        return 1;
    foo((n * 2) / 3) + foo(n - 2);
        return i;
}
int main()
{
    int n;
    cin >> n;
    cout << foo(n);
    return 0;
}
