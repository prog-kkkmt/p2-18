#include <stdio.h>
#include <conio.h>
#include <locale.h>
main()
{
    setlocale(0,"");
     int a[5];
      int b[5];
      int c[5];
      int i;
// ���������� ��������� �� ����
     FILE *fout;
// ��������� ���� �� ������
      //fou = fopen("C:\\Users\\user\\Desktop\\data.txt", "w");
        fout = fopen("f2.txt", "w");
// ���������� ����������� � ����
     printf("������� �������\n");
     for (i=0;i<5;i++)
     {
// ���� �������� ��������� �������� , ���������� ����� �� ������ � ����

         scanf("%d%d",&a[i],&b[i]);
         c[i]=a[i]+b[i];
         fprintf(fout,"%d %d %d\n",a[i],b[i],c[i]);
     }
// ����� �������� �� �����
fclose(fout);
// ��������� ���� �� ������
fout = fopen("f2.txt", "r");
 for (i=0;i<5;i++)
     {fscanf(fout,"%d%d%d",&a[i],&b[i],&c[i]);
         printf("%d %d %d \n",a[i],b[i],c[i]);
     }
     getch();
// �������� �����
     fclose(fout);
}
