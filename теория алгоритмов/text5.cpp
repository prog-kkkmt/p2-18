// Дана строка S и текстовый файл. Добавить строку S в конец файла
#include <iostream>
#include <fstream>

using namespace std;

int main()
{
string S = "string"; // создаём строку S
ofstream file("werty.txt"); // открывает текстовый документ
file << S; // записываем строку в файл
file.close(); // закрываем файл
return 0; // возвращаем 0
}
