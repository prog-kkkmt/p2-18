/*Case2∞. ƒано целое число K. ¬ывести строку-описание оценки, соответствующей числу K
(1 Ч Ђплохої, 2 Ч Ђнеудовлетворительної, 3 Ч Ђудовлетворительної, 4 Ч Ђхорошої, 5 Ч Ђотличної).
 ≈сли K не лежит в диапазоне 1Ц5, то вывести строку Ђошибкаї.*/

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
