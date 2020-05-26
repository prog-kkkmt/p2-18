#include <iostream>
#include <string>
#include <fstream>
#include <locale.h>
#include <Windows.h>
using namespace std;

int main()
{
//locale
    setlocale(LC_ALL, "Russian");
    SetConsoleCP(1251);
    SetConsoleOutputCP(1251);

//Developer
cout << "-------------------------------------------------------------------------------------------";
cout << endl<< "Программу тест по языку ассемблер разработал Безбородов Константин" << endl;
cout << "-------------------------------------------------------------------------------------------" << endl;

//vars
int answer[3];
int trueAnswer[3] = {2, 1, 1};

string name = "guest", lastName = "guest";
//name input
cout << " Введите ваше имя: ";
    cin >> name;
cout << "\n";
//Last name input
cout << " Введите вашу фамилию: ";
    cin >> lastName;
cout << endl<< "-----------------------------------#1------------------------------------------------------" << endl;
//#1
//Перечислите команды, корректно записанные с синтаксисом AT&T
//pop eax FALSE / sub $3,%eaxpop TRUE / %eax, %ebxpop FALSE / $3push 3 FALSE/
cout << "Выбрать команду котороая корректно записанна с синтаксисом AT&T" << endl;
cout << "Варианты ответов:" << endl << "<1> pop eax \t<2> sub $3, %eaxpop \t<3> %eax, %ebxpop \t<4> $3push" << endl << endl;
cin >> answer[0];
cout << endl<< "-----------------------------------#2------------------------------------------------------" << endl;
//#2
//Шестнадцатеричное 96h в двоичной системе исчисления равно
//10010110 TRUE / 01101001 FALSE /  0000011000001001 FALSE /  150 FALSE/
cout << "Шестнадцатеричное 96h в двоичной системе исчисления равно" << endl;
cout << "Варианты ответов:" << endl << "<1> 10010110 \t<2> 01101001 \t<3> 0000011000001001 \t<4> 150" << endl << endl;
cin >> answer[1];
cout << endl<< "-----------------------------------#3------------------------------------------------------" << endl ;
//#3
//К регистрам общего назначения относят регистры
//EAX; EBX; ECX; EDX; TRUE / EES; EDS; ESS; ECS; FALSE /
cout << "К регистрам общего назначения относят регистры" << endl;
cout << "Варианты ответов:" << endl << "<1> EAX; EBX; ECX; EDX; \t<2> EES; EDS; ESS; ECS;" << endl << endl;
cin >> answer[2];
cout << endl<< "------------------------------------YOUR ANSWERS------------------------------------------" << endl;
for(int i = 0; i<3; i++){
    cout << "#" << i+1 << ends << "your answer:" << ends <<answer[i] << ends;
    if (answer[i]!= trueAnswer[i]){
        cout << "false" << ends;
        if(answer[i]>4 || answer[i] < 1)
        {
            cout << "Такого ответа нет!" << endl;
        }
        else{
            cout << endl;
        }
        continue;
    }
    else if((answer[i]== trueAnswer[i]))
    {
        cout << "true" << endl;
        continue;
    }
}
cout << endl<< "------------------------------------TRUE ANSWERS------------------------------------------" << endl;
for(int i = 0; i<3; i++){
    cout << "#" << i+1 << ends << "true answer:" << ends <<trueAnswer[i] << endl;
}
//РАБОТА С ФАЙЛОМ
ofstream myFile;
myFile.open("data.txt");
myFile <<"Тест выполнил: "<< ends << name << ends << lastName<<endl;
for(int i = 0; i < 3;i++){
    myFile << "#" << i+1 << ends << "your answer:" << ends <<answer[i] << ends;
    if (answer[i]!= trueAnswer[i]){
        myFile << "false" << ends;
            if(answer[i]>4 || answer[i] < 1){
                myFile << "Такого ответа нет!" << endl;
            }
            else{
                myFile << endl;
            }
        continue;
    }
    else if((answer[i]== trueAnswer[i]))
    {
        myFile << "true" << endl;
        continue;
    }
}
myFile.close();
}
