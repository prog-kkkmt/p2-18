/*���������: ��������� �.�., �������� �.�., �������� �.�.
  ������: ���� �2-18

���������� ������� getline, ������� ��������� ����� ����� �����������,
  ���� �� ��������� ����� ������ ��� �� �������� ������ �������� ������ ('\n'),
  � ���������� C-style ������ � ������������ ���������.
�������� ��������, ��� ��� ��� ������ ����� ������� ����������,
  �� ��� ����� ����� ������������ ������ � �������� ������, ���� � ������ ����� ��������� ������ ��������,
  ��� �� �������.
������, ������������ �� ������� ����� ����������� ���������� delete[].
  ������ �������� ������ ('\n') ��������� � ������ �� �����, �� �� ��������, ��� � ����� C-style
  ������ ������ ���� ����������� ������� ������.
*/

#include <iostream>

using namespace std;

char *resize(const char *str, unsigned size, unsigned new_size){
    char * new_str = new char[new_size];
    for(int i = 0; i < size && i < new_size; ++i)
        new_str[i] = str[i];
    delete[] str;
    return new_str;
}

char *getline(){
    int i = 0, buf = 40;
    char c, *str = new char [buf];
    while (std::cin.get(c) && c != '\n'){
        if (i == buf)
            str = resize(str, i, buf += buf);
        str[i] = c;
        i++;
    }
    str[i] = '\0';
    return str;
}

int main(){
    const char *str = {"Hello. word!"};
    int size = 5;
    int new_size = 15;
    cout << getline();

}
