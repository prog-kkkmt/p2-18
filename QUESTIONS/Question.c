//Найти разницу между числом строчных и прописных (заглавных)
//букв в строке(длина не более 100 символов), подаваемой на вход. 
//Библиотеки <stdio.h>, <string.h> подключать не нужно. (На экран выводить ничего не надо)


#include <ctype.h>

int diff_lower_upper(char * str) {
	// put your code
    int zaglav, nezaglav;
    for(int i = 0; i < 100; ++i){
        if(isupper(str)){
            ++zaglav;
        }
        else{
            ++nezaglav;
        }
        ++str;
    }
       printf("%d", nezaglav - zaglav);
}




