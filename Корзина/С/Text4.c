//��� ��������� ����. ������� ���������� ������������ � ��� �������� � ����� (������� ������ ����� EOLN � ����� ����� EOF ��� �������� ���������� �������� �� ���������).
// ��������� ���� ���������� ����������

#include <stdio.h>
#include <locale.h>
#include <stdlib.h>
#include <string.h>
#define N 255

int main(){
    setlocale(0,"");
        FILE *f;
    char s[N];
    unsigned line, word= 0, flag, i;
    line = 0;
    f = fopen("four.txt","r");
    while (fgets(s, N, f) != NULL) {
        line++;
        flag = 0;
        for (i=0; i < strlen(s); ++i)
            if (s[i] != ' ' && flag == 0) {
                word++;
                flag = 1;
            } else
                if (s[i] == ' ') flag = 0;

    }
    printf("%ld ������(a/��)\n",word);
    printf("%d �����\n", line);
    fclose(f);
}  /* int word=0,symb=0,size;
    FILE *four;
        char name[] = "four.txt";
        if ((four = fopen(name, "rb")) == NULL){
            printf("�� ������� ������� ����");
            return 0;
        }
            while (!feof(four)){            //������ ����� �� �����
                fscanf(four, "%*[^\n]%*c");
                word += 1;                // �������
            }

    {
    fseek (four, 0, SEEK_END);
    size = ftell(four);
    fclose(four);
    printf("%ld\n", size);
  }*/


/*    fclose(four);
    printf("����� � �����: %d\n",word);
    printf("�������� � �����: %d\n",symb);

}*/

  /*while ((ch = getchar()) != EOF) {
        if (ch == '\n')
            word++; // ������
        else
            simb++; // �������

        if (ch == ' ' || ch == '\n')
            flag = -1; // �����
        else if (flag == -1) {
            flag = 1;
        }
    }

*/
