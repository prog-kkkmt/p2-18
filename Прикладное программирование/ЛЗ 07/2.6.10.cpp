/*Выполнили: Короленко И.Р., Кузнецов М.С., Слесарев А.М.
  Группа: ККМТ П2-18

Реализуйте функцию getline, которая считывает поток ввода посимвольно,
  пока не достигнет конца потока или не встретит символ переноса строки ('\n'),
  и возвращает C-style строку с прочитанными символами.
Обратите внимание, что так как размер ввода заранее неизвестен,
  то вам нужно будет перевыделять память в процессе чтения, если в потоке ввода оказалось больше символов,
  чем вы ожидали.
Память, возвращенная из функции будет освобождена оператором delete[].
  Символ переноса строки ('\n') добавлять в строку не нужно, но не забудьте, что в конце C-style
  строки должен быть завершающий нулевой символ.
*/

#include <iostream>

using namespace std;

char *resize(const char *str, unsigned size, unsigned new_size){
    char * new_str = new char[new_size];
    for(int i = 0; i < size && i < new_size; ++i)
        new_str[i] = str[i];
    delete[] str;
    return new_str;
}

char *getline(){
    int i = 0, buf = 40;
    char c, *str = new char [buf];
    while (cin.get(c) && c != '\n'){
        if (i == buf)
            str = resize(str, i, buf += buf);
        str[i] = c;
        i++;
    }
    str[i] = '\0';
    return str;
}

int main(){
    const char *str = {"Hello. word!"};
    int size = 5;
    int new_size = 15;
    cout << getline();

}
