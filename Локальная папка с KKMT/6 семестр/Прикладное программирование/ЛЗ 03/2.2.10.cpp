//���������: ��������� �.�., �������� �.�., �������� �.�.
//������: ���� �2-18
//�������: 2.2 ���� �������

#include <iostream>

using namespace std;

void rev()
{
    int a = 0;
    cin >> a;
    if(a == 0) return;
        rev();
    cout << a << " ";
}
int main()
{
    rev();
    return 0;
}
