//���� ��� ���������� ������������� ����: A, B, C.
//���� �� �������� ����������� �� �����������, �� ������� ��;
//� ��������� ������ �������� �������� ������ ���������� �� ���������������.
// ������� ����� �������� ���������� A, B, C.
#include <iostream>
using namespace std;
int main(){
    double a=-2.9,b=0,c=1.2;
    if (a < b && b < c){
        a*=2;
        b*=2;
        c*=2;
    }
    else{
        a=-a;
        b=-b;
        c=-c;
    }
    cout<< a << ' ' << b << ' ' << c <<endl;
    return 0;
}
