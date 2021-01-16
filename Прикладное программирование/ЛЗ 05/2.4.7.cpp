/*Выполнили: Короленко И.Р., Кузнецов М.С., Слесарев А.М.
  Группа: ККМТ П2-18*/

#include <iostream>	
#include <string>

using namespace std;

void strcat(char *to, const char *from){
    while (*to != '\0')
        *to++;
    while (*from != '\0')
        *to++ = *from++;
    *to++ = '\0';
}

int main(){
	char word[] = "Ivan";
	char buff[30] = "Korolenko";
	strcat(word, buff);
	return 0;
}
