#include <stdio.h>
#include <conio.h>
#include <stdlib.h>
main()
{
// ������ ��������� ���������
char st[100];

//���������� ��������� �� ����
      FILE *fin;
// ���������� ������ � ����������
      setlocale(0, "");
// ��������� ���� �� ������
      fin = fopen("f6.txt", "r");
          if (fin == NULL) {
        printf("Error opening file");
        getch();
                                    }
// ��������� ������ ������ �� �����
while (!feof(fin))
        {if ( NULL != fgets ( st, 100, fin ) )

        // ������� ������ �� �����
        printf("%s \n",st);}

   fclose(fin);
}
