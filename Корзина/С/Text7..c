#include <stdio.h>
#include <locale.h>
#include <stdlib.h>
//Text7. ���� ������ S � ��������� ����. �������� ������ S � ������ �����.

int main(){
    setlocale(0,"");
        FILE *seven;

        char buff[300];
        char word[25];
          char name[] = "seven.txt";

              if ((seven = fopen(name, "a+")) == NULL){
                printf("�� ������� ������� ����");
                return 0;
              }

              while (!feof(seven)){
                    fgets(buff, 300, seven);
              }

                fclose(seven);
                seven = fopen(name, "w");

            printf("������� �����: ");
            gets(word);

            fputs(word,seven);
            fputs(buff ,seven);


  fclose(seven);
    return 0;
}
