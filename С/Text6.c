//Text6. Даны два текстовых файла. Добавить в конец первого файла содержимое второго файла.

#include <stdio.h>
#include <stdlib.h>
#define N 256

int main(){
        FILE *six2 = fopen("Text2.txt", "r");
        FILE *six1 = fopen("Text1.txt", "a");

        char buff[N];

              while (fgets(buff, N , six2) != NULL) {
                fputs(buff, six1);
            }

    fclose(six1);
    fclose(six2);


return 0;
}
