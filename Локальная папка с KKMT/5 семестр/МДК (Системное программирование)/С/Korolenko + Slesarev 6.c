#include <stdio.h>
#include <locale.h>
#include <time.h>
��� ������ A ������ N
������� ��� �������� � ������� �������� � ������� ����������� �������
�2 �4 �6
�������� ��������


void main(){
    setlocale(0,"");
        int i,n;
        scanf("%d",&n);
        int mas[n];
            for ( i = 0; i < n; i ++){
                mas[i] = rand ()%10; //��������� �����
                printf("%d ",mas[i]);
            }
                printf("\n");
            i=1;
            while(i<=n){
                printf("%d ",mas[i]);
                i=i+2;
            }
    }
