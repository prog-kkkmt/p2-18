//���������: ��������� �.�., �������� �.�., �������� �.�.
//������: ���� �2-18
//�������: 1.8 �������� � ��������� C++, ����� 2

#include <iostream>
#include <cmath>

using namespace std;

int main(){
    double a,b,c,d,x1,x2;
    cin >> a >> b >> c;
    d = (b*b) - (4*a*c);
    if(d>=0){
        x1 = (-b+sqrt(d)) / (2*a);
        x2 = (-b-sqrt(d)) / (2*a);
        cout << x1 << " " << x2 << endl;
    }
    else{
        cout<<"No real roots"<<endl;
    }    return 0;
}
