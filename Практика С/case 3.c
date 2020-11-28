/*Case3. ƒан номер мес€ца Ч целое число в диапазоне 1Ц12
(1 Ч €нварь, 2 Ч февраль и т. д.).
¬ывести название соответствующего времени года
(Ђзимаї, Ђвеснаї, Ђлетої, Ђосеньї)..*/

#include <stdio.h>

int main()
{
   int a;
   scanf("%d", &a);
   switch(a){
    case 12:
    case 1:
    case 2:
        printf("Zima");
        break;
    case 3:
    case 4:
    case 5:
        printf("Vesna");
        break;
    case 6:
    case 7:
    case 8:
        printf("Leto");
        break;
    case 9:
    case 10:
    case 11:
        printf("Osen");
        break;
    default:
        break;
   }
   return 0;
}
