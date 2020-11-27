/*Case1. Дано целое число в диапазоне 1–7. Вывести строку — название дня недели,
соответствующее данному числу (1 — «понедельник», 2 — «вторник» и т. д.).*/
#include <locale.h>
#include <stdio.h>
int main(){
    int day;
    scanf ("%d", & day);
    setlocale (LC_ALL, "rus");
    switch (day){
    case 1:
        printf ("Понедельник");
        break;
    case 2:
        printf ("Вторник");
        break;
    case 3:
        printf ("Среда");
        break;
    case 4:
        printf ("Четверг");
        break;
    case 5:
        printf ("Пятница");
        break;
    case 6:
        printf ("Суббота");
        break;
    case 7:
        printf ("Воскресенье");
        break;
    }
    return 0;
}
