/*https://stepik.org/lesson/538/step/9?unit=861*/

/*� ���� ��������� ���������� ��������� �������:

int foo(int n) {
    if (n <= 0)
        return 1;
    return foo((n * 2) / 3) + foo(n - 2);
}
����� ���������, ������� ����� ��� ����� ������� ������� foo, ���� �� ������� � ���������� 3 (�.�. foo(3)).
 ����� ������ ����� ���� ����� ���������.

*/

#include <iostream>

using namespace std;

// ������� foo ����� ���������� 9 ���, ����� � ���� ��������� ������� ����������� ���������� cnt �� ��������� � ��������� � ���������:

extern int cnt = 0;

int foo(int n) {
    cnt ++;
    if (n <= 0)
        return 1;
    return foo((n * 2) / 3) + foo(n - 2);

}
int main()
{
    int n = 3;
    cout << foo(n) << endl;
    cout << cnt << endl;

    return 0;
}
