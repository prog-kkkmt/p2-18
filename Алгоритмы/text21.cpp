//Text21. Дан текстовый файл, содержащий более трех строк. Удалить из него последние три строки.
//Выполняли Щепкин и Бурлаев
/*

Леопард быстро бегает
У слона есть хобот
Лев больно кусает
Кошки милые
Пчела летает

Вставить в текстовый файл

*/

#include <iostream>
#include <string>
#include <vector>
#include <fstream>
#include <algorithm>
#include <iterator>

using namespace std;


bool remove_line(const char *filename, size_t index)
{
    std::vector<std::string> vec;
    std::ifstream file(filename);
    if (file.is_open())
    {
        std::string str;
        while (std::getline(file, str))
            vec.push_back(str);
        file.close();
        if (vec.size() < index)
            return false;
        vec.erase(vec.begin() + index);
        std::ofstream outfile(filename);
        if (outfile.is_open())
        {
            std::copy(vec.begin(), vec.end(),
                std::ostream_iterator<std::string>(outfile, "\n"));
            outfile.close();
            return true;
        }
        return false;
    }
    return false;
}

int main(void)
{
    const char * filename = "FILENAME.txt";
    setlocale(LC_ALL, "Russian_Russia.1251");
    ifstream file_in;
    file_in.open(filename);

    if (!file_in)
    {
        std::cerr << Ошибка, невозможно открыть файл :" << "FILENAME.txt" << std::endl;
    }
    else
    {
        //---подсчет количества строк в файле-----------------------------------
        string s;
        int i = 0; //---количество строк
        while (file_in.peek() != EOF)
        {
            getline(file_in, s);
            i++;
        }
        //----------------------------------------------------------------------
        file_in.close();
        if (i <= 3)
        {
            cout << "В файле меньше 3 строк!" << endl;
        }
        else
        {
            for (int j = (i-1); (i - j) < 4; j--)
            {
                remove_line(filename, j);
            }
            cout << "Операция успешна!" << endl;
        }
    }
    system("pause");
        return 0;
    }
