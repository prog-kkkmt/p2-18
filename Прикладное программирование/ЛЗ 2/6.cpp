/* https://stepik.org/lesson/13377/step/12?unit=3571
*/

/*
�������� ���������, ������� ����������� ������ �� std::cin, ���� �� ��������� ����� ������ �����,
 � �������� ��������� ������ ������ �������� ����� � ������� ���������� ��������� � std::cout.
 ������� ������ ��������, ����� �������� ������� �� �����.
 ��� ���������� ������� ��� �� ����������� ������������ �������������� �������, � ������: ���������, ������������ ������������ � ��������, ���� ���� �� ��� � ���� �������.
 �� ������ ���������� ����� ��������������� �������, ���� ��� ��� �����.

���������: �������� ����������� ���� ��� ������������ ����. ������� ������ ('\0'), ������ ����� ������ ('\n')
� ����� ������ � ��� ��� ������ ����. ��� ��, ��� �������� ����� ������ �  �������� � ����� ��� ������������ ����.
*/

#include <iostream>
using namespace std;

int main()
{
    char c = '\0';
    while (cin.get(c)) {
        while (c == ' ' && cin.peek() == ' '){
            cin.get(c);
        }
        cout << c;
    }
    return 0;
}
