#include <stdio.h>
#include <conio.h>
#include <stdlib.h>
main()
{
// ������ ��������� ���������
char st1[100];
char st2[100];
//���������� ��������� �� ����
      FILE *fin;
// ���������� ������ � ����������
      setlocale(0, "");
// ��������� ���� �� ������
      fin = fopen("f5.txt", "r");
          if (fin == NULL) {
        printf("Error opening file");
        getch();
                                    }
// ��������� ������ ������ �� �����
if ( NULL != fgets ( st1, 100, fin ) )
{
// ������� ������ �� �����
printf("%s \n",st1);}
// ��������� ������ ������ �� �����
if ( NULL != fgets ( st2, 100, fin ) )
{
// ������� ������ �� �����
printf("%s \n",st2);}
// ��������� ���� �� ������
   fclose(fin);
}
