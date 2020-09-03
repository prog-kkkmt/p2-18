//Дано имя файла и целые положительные числа N и K. Создать текстовый файл
// с указанным именем и записать в него N строк, каждая из которых состоит из K символов «*» (звездочка).


#include <iostream>
#include <fstream>
#include <string>

using namespace std;


int main()
{
    int n, k; // n кол-во строк, k кол во звезд в строке

    //ввод данных
    cout << "enter numbers of strings\n";
    cin >> n;
    cout << "enter number of symbols \" * \" \n";
    cin >> k;

    //переменная для имени файла
    string filename;
    //ввод имени файла
    cout << "enter file name ";
    cin >> filename;
    //создания объекта из библиотеки fstream для работы с файлами
    ofstream fileOBJ;
    fileOBJ.open(filename + ".txt"); //создание файла с вводимым значением + разширением файла txt
    //вложенный цикл для заполнения файла звездами
    for(int i = 0; i < n; ++i){
        for(int j = 0; j < k; ++j){
            fileOBJ << '*';
        }
        fileOBJ << "\n";
    }

    //закрытие файла для освобождения памяти
    fileOBJ.close();
return 0;
}
