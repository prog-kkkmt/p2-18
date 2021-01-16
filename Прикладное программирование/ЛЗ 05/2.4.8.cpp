/*Выполнили: Короленко И.Р., Кузнецов М.С., Слесарев А.М.
  Группа: ККМТ П2-18*/

#include <iostream>	

using namespace std;

int strstr(const char *text, const char *pattern){
	if (*pattern == '\0') return 0;
        int l_t = strlen(text);
        int l_p = strlen(pattern);
        int count = -1;
        for (int i = 0; i < l_t; i++) {
                int count_p = 0;
                for (int j = 0; j < l_p; j++) {
                        if (text[i + j] == pattern[j]) {
                                ++count_p;
                        } else break;
                }
                if (count_p == l_p) return i;  
        }
        return count;
}

int main(){
	
	return 0;
}
