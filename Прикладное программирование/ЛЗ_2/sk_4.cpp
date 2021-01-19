//https://stepik.org/lesson/13377/step/11?auth=login&unit=3571
/*�������� ��������� ��� ������� ���������� ��������� ���� a x^2 + bx + c = 0(������������ x). �� ���� ��������� �������� ��� ����� �����: a, b � c, ��������������. ��� ���� �������������, ��� a != 0. �� ����� ��������� ������ ������� ��� ������������ ����� ���������, ���������� ��������. ���� ������������ ������ ���, �� ��������� ������ ������� ������ "No real roots". ���� � ��������� ������� ������ ���� ������ (������� ������), �� ��������� ������ ������� ��� ������. ������� ������ ������ �� �����. ������, ����� �����, �������� �� �����. ��� ���������� � ��������� ������ ����������� ��� double. ��� ���������� ������� ��� ����� ��������� �������� ������� sqrt �� ������������� ����� cmath.

���������: ����� ����, ��� �� ������� ��� �������, ���������� ��������, ��� ���������� �� ���� ���������, ���� �� �� �� �������������, ��� a != 0.*/

#include <iostream>
#include <cmath>
using namespace std;

int main()
{
    int a, b, c;
    cin >> a >> b >> c;
  double x1, x2, d;
  d = (b * b) - (4 * a * c);
  if (d >= 0) {
        x1 = (-b - sqrt(d)) / (2 * a);
        x2 = (-b + sqrt(d)) / (2 * a);
    cout << x1 << " " << x2;
  }
    else 
    {
        cout << "No real roots";
    }
    return 0;
}