#include <stdio.h>
#include <conio.h>
main()
{     int a[10];
      int b[10];
      int c[10];
      int i;
// ���������� ��������� �� ����
     FILE *fin;
// ��������� ���� �� ������
      //fin = fopen("C:\\Users\\user\\Desktop\\data.txt", "r");
        fin = fopen("f1.txt", "r");
// ���������� ���������� �� �����
     for (i=0;i<10;i++)
     {
// ���������� ������ ��  ���� �������� ����� � ������ � �������
         fscanf(fin,"%d%d%d",&a[i],&b[i],&c[i]);
     }
// ����� �������� �� �����
 for (i=0;i<10;i++)
     {
         printf("%d %d %d \n",a[i],b[i],c[i]);
     }
     getch();
// �������� �����
     fclose(fin);
}
