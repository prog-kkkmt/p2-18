/*����������� ��������� � ���� ��� ������ � �������� ����� ����� �� 10 ���������.
������ ����: ����������, ���������� �������������, ���������� �����, ������, �����.
��� ������� �������� (����� ������) ����������� �������, ����������� � �������� ����������
����� ������� �������� ������� � ���������� ���������.
������: ����� �.�. ������ �2-18
*/
#include <iostream>
#include <fstream>
#include <stdlib.h>
#include <ctime>


using namespace std;
int maks,summ=0;
void full(int* f, int n)//�������� �������
{
    *(f+n)=-100+rand()%200;
    n--;
    if (n>-1)
    {
        return full(f,n);
    }
}
int max(int* f, int n)//������������ �����
{
    if ((n==10)||(n==9))
    {
        maks=*(f+n);
    }
    else
    {
        if(*(f+n)>maks)
        {
            maks=*(f+n);
        }
    }
    n--;
    if (n>-1)
    {
        return max(f,n);
    }
    return maks;
}
int sum(int* f, int n)//�����
{
    if (n==10)
    {
        n--;
        return sum(f,n);
    }
    summ+=*(f+n);
    n--;
    if (n>-1)
    {
        return sum(f,n);
    }
}
    ofstream mas("mas.txt");
void fil(int* f, int n)//������ (������ � ����)
{
    if (n==10)
    {
        n=0;
        return fil(f,n);
    }
    mas<<*(f+n)<<' ';
    n++;
    if (n!=9)
    {
        return fil(f,n);
    }
    else
    {
        mas<<*(f+n)<<' ';
        mas.close();
    }

}
int main()
{
    setlocale(LC_ALL, "Russian");
    srand (time(NULL));
    int swit,a[10];
    int *f=&a[0];
    cout<<"������ �� ���������"<<endl<<"1)����������"<<endl
    <<"2)�����"<<endl;
    cin>>swit;
    switch (swit)
    {
        case 1:
        {
            full(f,10);
            break;
        }
        case 2:
        {
            return 0;
        }
    }
    system("cls");
    cout<<"1)����������"<<endl
    <<"2)���������� �������������"<<endl
    <<"3)���������� �����"<<endl
    <<"4)������"<<endl
    <<"5)�����"<<endl;
while(swit!=5)
    {
        cout<<"��� ������: "<<endl;
        for(int i=0;i<10;i++)
        {
            cout << a[i]<<' ';
        }
        cout<<endl;
        cin>>swit;
        switch (swit)
        {
            case 1:
            {
                full(f,10);
                break;
            }
            case 2:
            {
                cout<<" ��������: "<<max(f,10)<<endl;
                break;
            }
            case 3:
            {
                cout<<" �����: "<<sum(f,10)<<endl;
                break;
            }
            case 4:
            {
                fil(f,10);
                char kv='"';
                cout<<"������ ������� � "<<kv<<"mas.txt"<<kv<<endl;
                break;
            }
            case 5:
            {
                return 0;
            }
            default:
            {
                return 0;
            }
        }
    }
    return 0;
}
