/*Вводим число от 1 до 7, программа выдаст день недели. Слесарев А.М. 18.09.20*/
#include <stdio.h>
 
int main()
{
   int a;
   printf("Введите число от 1 до 7: ") ;
   scanf ("%d", &a); 
   switch (a) 
   {
   case 1:
       printf("Понедельник") ;
       break;
   case 2:
       printf("Вторник") ;
       break;
   case 3:
       printf("Среда") ;
       break;
   case 4:
       printf("Четверг") ;
       break;
   case 5:
       printf("Пятница") ;
       break;
   case 6:
       printf("Суббота") ;
       break;
   case 7:
       printf("Воскресенье") ;
       break;
   }
   return 0;
}