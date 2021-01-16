/*Выполнили: Короленко И.Р., Кузнецов М.С., Слесарев А.М.
  Группа: ККМТ П2-18*/

#include <iostream>	
#include <string>

using namespace std;

unsigned strlen(const char *str){
    if(*str)
      return 1 + strlen(++str);
    else 
      return 0;
}

int main(){
	const char *str = "Hello, word!";
	cout << strlen(str);
	return 0;
}

/*Выполнили: Короленко И.Р., Кузнецов М.С., Слесарев А.М.
  Группа: ККМТ П2-18*/

#include <iostream>	
#include <string>

using namespace std;

unsigned strlen(const char *str){
    return *str ? 1 + strlen(++str) : 0;
}

int main(){
	const char *str = "Hello, word!";
	cout << strlen(str);
	return 0;
}

/*Выполнили: Короленко И.Р., Кузнецов М.С., Слесарев А.М.
  Группа: ККМТ П2-18*/

#include <iostream>	
#include <string>

using namespace std;

unsigned strlen(const char *str){
    unsigned len = 0;
    while(*str++) len++;
    return len;
}

int main(){
	const char *str = "Hello, word!";
	cout << strlen(str);
	return 0;
}

