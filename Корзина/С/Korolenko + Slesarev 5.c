#include <stdio.h>
#include <locale.h>
#include <time.h>

���� ����� ����� N � ����� �� N �����
����� ����������� ��������� ����� �� ������� ������
���� ������������� �����    � ������ ���������� �� ������� 0


void main(){
    setlocale(0,"");
    int i,n,m;
        scanf("%d",&n);
            int mas[n];
        for ( i = 0; i < n; i ++){
            mas[i] = rand ()%10-10; //��������� �����
                printf("%d ",mas[i]);
        }
        m=mas[0];
        for ( i = 0; i < n; i ++){
            if(mas[i]>m)
                m=mas[i];
        }
            if(m>0){
                printf("\n%d",m);
            }
            else printf("\n0,00");
    }
