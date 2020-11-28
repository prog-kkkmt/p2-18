/*Case2°. Дано целое число K. Вывести строку-описание оценки, соответствующей числу K
(1 — «плохо», 2 — «неудовлетворительно», 3 — «удовлетворительно», 4 — «хорошо», 5 — «отлично»).
 Если K не лежит в диапазоне 1–5, то вывести строку «ошибка».*/

#include <stdio.h>

int main()
{
   int a;
   scanf("%d", &a);
   switch(a){
   case 1:
        printf("Ploho");
        break;
    case 2:
        printf("Neudovletvoritelno");
        break;
    case 3:
        printf("Udovletvoritelno");
        break;
    case 4:
        printf("Horosho");
        break;
    case 5:
        printf("Otlichno");
        break;
    default:
        printf("Oshibka");
        break;

   }
   return 0;
}
