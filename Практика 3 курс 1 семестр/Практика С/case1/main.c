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
        printf("Ponedelnik");
        break;
    case 2:
        printf("Vtornik");
        break;
    case 3:
        printf("Sreda");
        break;
    case 4:
        printf("Cgetverg");
        break;
    case 5:
        printf("Pyatnica");
        break;
    case 6:
        printf("Subbota");
        break;
    case 7:
        printf("Voskresenie");
        break;
    default:
        printf("Nepravilno ukazan den");
        break;
}
return 0;
}
