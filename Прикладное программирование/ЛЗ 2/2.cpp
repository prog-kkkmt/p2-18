/* https://stepik.org/lesson/13377/step/7?unit=3571
*/

/*�����������, ��� � ��������� �������� ������ sqr.

#define sqr(x) x * x


����� �������� ����� ����� ��������� ���������?

sqr(3 + 0)
*/

//��������� ����� ����� �������� 3, ����� � ��� ��������� ������� ���������

#include <iostream>
using namespace std;

#define sqr(x) x * x
int main(){
    cout << sqr(3 + 0);

    return 0;
}
