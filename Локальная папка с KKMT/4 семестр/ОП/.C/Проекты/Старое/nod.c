#include <stdio.h>
#include<string.h>
#include<locale.h>
#include <stdlib.h>
#include <ctype.h>
main()
{      setlocale(LC_CTYPE, "Rus");
char s1[10],s2[10];
printf("������� 1 ������   ");
scanf("%5s",s1);
printf("c�����-%s\n",s1);
scanf("%s",s1);
printf("c�����-%s\n",s1);
/*printf("������� 2 ������   ");
gets(s2);
puts(s2);*/
return 0;
}
