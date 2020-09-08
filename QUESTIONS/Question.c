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




