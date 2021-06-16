#include <stdio.h>
#include<string.h>
#include<locale.h>
#include <stdlib.h>
#include <ctype.h>
main()
{      setlocale(LC_CTYPE, "Rus");
char s1[10],s2[10];
printf("введите 1 строку   ");
scanf("%5s",s1);
printf("cтрока-%s\n",s1);
scanf("%s",s1);
printf("cтрока-%s\n",s1);
/*printf("введите 2 строку   ");
gets(s2);
puts(s2);*/
return 0;
}
