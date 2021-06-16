File1. Дана строка S. Если S является допустимым именем файла, то создать пустой файл с этим именем и вывести True. Если файл с именем S создать нельзя, то вывести False.
	

#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#define N 30

int main(){
    char *a, word[N], symb[] = "/\\*:?>\"<|";
    	gets(word);
    	a = strpbrk(symb, word);
		if(a == NULL){
                    printf("True");
	    	    strcat(word, ".txt");
	     	    FILE *file1 = fopen(word, "wb+");
		    fclose(file1);
	    	}
    	else printf("False");
    return 0;
}




