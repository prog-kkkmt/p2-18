#include <stdio.h>
#include <locale.h>
#include <time.h>

����� ����� N (�0)
����� ������������ 1,1*1,2*1,3,,,
12

void main(){
    setlocale(0,"");

    float j=1,n,s;
    int i;
    scanf("%f",&n); //���� �����

        for (i=1; i<n; i++){ // ������� ������
            j=j*(1+i*0.1);
        }
        printf("%f",j);// �����
}
