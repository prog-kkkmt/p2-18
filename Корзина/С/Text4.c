//Дан текстовый файл. Вывести количество содержащихся в нем символов и строк (маркеры концов строк EOLN и конца файла EOF при подсчете количества символов не учитывать).
// Короленко Иван Безбородов Константин

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
    printf("%ld символ(a/ов)\n",word);
    printf("%d строк\n", line);
    fclose(f);
}  /* int word=0,symb=0,size;
    FILE *four;
        char name[] = "four.txt";
        if ((four = fopen(name, "rb")) == NULL){
            printf("Не удалось открыть файл");
            return 0;
        }
            while (!feof(four)){            //Считка файла до конца
                fscanf(four, "%*[^\n]%*c");
                word += 1;                // счётяик
            }

    {
    fseek (four, 0, SEEK_END);
    size = ftell(four);
    fclose(four);
    printf("%ld\n", size);
  }*/


/*    fclose(four);
    printf("Строк в файле: %d\n",word);
    printf("Символов в файле: %d\n",symb);

}*/

  /*while ((ch = getchar()) != EOF) {
        if (ch == '\n')
            word++; // строки
        else
            simb++; // символы

        if (ch == ' ' || ch == '\n')
            flag = -1; // слова
        else if (flag == -1) {
            flag = 1;
        }
    }

*/
