#include <iostream>
using namespace std;
int main()
{
int n;
cin >> n;//����
    int i;
    float sum = 0;//���������� ���� �����
    for  (i=1; i<=n; i++)
      sum += 1/(float)i; //������ I ���������� ���� float(���������� ������� �����
    cout<<sum; //�����
    return 0;
}
