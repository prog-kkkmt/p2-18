/*Case3. Дан номер месяца — целое число в диапазоне 1–12
(1 — январь, 2 — февраль и т. д.).
Вывести название соответствующего времени года
(«зима», «весна», «лето», «осень»)..*/

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
