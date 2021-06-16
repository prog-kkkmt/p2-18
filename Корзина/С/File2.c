File2°. Дано имя файла и целое число N (> 1). Создать файл целых чисел с данным именем и записать в него N первых положительных четных чисел (2, 4, …).


#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#define N 30

int main(){
        int num;
        char word[N];
        gets(word);
        scanf("%d", &num);
            strcat(word, ".txt");
            FILE *file2 = fopen(word, "wb+");
        for (int i = 2; i < num; i += 2)
            if ((i % 2) == 0){
                fprintf(file2,"%d ", i);
        }
        fclose(file2);
    return 0;
}
