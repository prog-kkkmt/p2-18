#include <stdio.h>
#include <locale.h>
#include <time.h>

���� ����� ����� N (>1) ������� ���������� �� ����� ����� �
��� ������� ������ 1+2+,,,+� ����� ������ ��� ����� N � ���� ��� �����

void main(){
    setlocale(0,"");

    int k=0,n,sum=0,i;
    scanf("%d",&n);
        while(sum <= n){
            k++;
            sum+=k;
        }
        printf("K=%d Summ=%d",k-1,sum-k);
    }
