#include <stdio.h>
#include <locale.h>
#include <time.h>

//���� ��� ����� ����� ���������� 12

void main(){
    setlocale(0,"");
    int i,j,min_value,n;
        printf("������� ���-��:\n");
        scanf ("%d", &n);
        int mas[n];
        printf("������� 3 �����:\n");
            for (i = 0; i < n; i++) {
                scanf ("%d", &mas[i]); }
            for(i = 0; i < n; i++)
                if(mas[i] < min_value) min_value = mas[i];
                printf("%i", min_value);
}
