/*� ���� ������ ��� ����� ����������� �������, ������� �������� ���������� ������� �����
�� �������� ����� ������� (����������� �����).

�� ���� ������� ��������� ������, ��� ������ � �������� ������.
��������, ���� �� ���� ������� ����� ������: int a[] = { 1, 2, 3, 4, 5 };
� ��������� ���������� �������� ��� ����� �� 2 �������, �� �� ������ �� �������
����� � ����� �������: 3, 4, 5, 1, 2.

�������� ��������, ��� �������� ������ ����� ���� �������,
� ����� ���� � ������ ������� �������, ��� ��� ������ ����� ������.

���������� � ����������: ��� ����� ����������� ������ ������� ������������ ������.
��� ���� ��� �� ������ ������� ��� �������� ���-����. ��� ������� ���� ������ �� ������
���������� ����� ��������������� �������, ���� ��� ��� �����. ������������� ������� main �� �����.
��������������, ��� ��� �� ����������� �������������� ������, � ������: ������� �
����������� ����������. ������������ ������������ ����������� � ������������
�� �����������, ���� ���� �� � ���� �������.

������������: ����� ���, ��� ������ ���������� ������� ���� ������,
���������� ��������, ������� �� ������ ������������. � ������ ������
�� ����������� ������������� ����� ��������� (� �������� ��������).

���������: ��� ����� ������������� �������� % ��� ���������� �������.
�������� ������� ���������� ���� ������� �������� ������ �� ���� ������� �� ������.
�������� ������� ���������� ��������� ��� ���������� �������, ������� ������������
�������� ������� � �������� �������.
������: ����� �.�. ������ �2-18*/
#include <iostream>
using namespace std;
int i=0,j=0;
void rotate(int a[], unsigned size, int shift)
{
    if (i!=size-1)
    {
        int sw;
        i++;
        sw=a[size-(1+i)];
        a[size-(1+i)]=a[size-1];
        a[size-1]=sw;
        return rotate (a,size,shift);
    }
    else
    {
        if (j<shift-1)
        {
            j++;
            i=0;
            return rotate(a,size,shift);
        }
        else
        {
            for(int k=0;k<size;k++)
            {
                cout<<a[k];
            }
        }
    }
}
int main()
{
    int n,x;
    cout<<"Size: ";
    cin>>n;
    cout<<"Shift: ";
    cin>>x;
    cout<<"a[]"<<endl;
    int a[n];
    for(int k=0;k<n;k++)
    {
        cin>>a[k];
    }
    rotate(a,n,x);
}
