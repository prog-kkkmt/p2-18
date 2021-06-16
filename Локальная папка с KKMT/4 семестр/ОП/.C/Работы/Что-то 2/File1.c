#include <stdio.h>
#include <string.h>
#include <locale.h>
#include <stdlib.h>

void main()
{
	setlocale(0,"");
	srand(time(NULL));
	FILE *file;
	FILE *F1;
	char str[20];
	file = fopen("file.txt","r");
	  if (file == NULL)
	   {
    		printf("Ошибка! Нет подходящего файла.");
          	getch();
       }
       fclose(file);
    int i,j,n,m,k,temp;
F1 = fopen("file.txt", "r");
if ( NULL != fgets ( str, 100, file ) )
	{
 		fprintf("%s \n",str);}
   fclose(F1);
}
