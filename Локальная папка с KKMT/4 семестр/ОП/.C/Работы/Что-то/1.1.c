#include <stdio.h> 
#include <string.h>
#include <locale.h>

void main() 
{ 
	 	setlocale(0,""); 
			char strl[255],sep[6]=",.!?",strn[255]="";
			char mas[20][20],temp[20];
			char *pstr;
					printf("Введите текст: ");
				gets(strl);
					printf("\n");
				pstr=strtok(strl,sep);
				int i=0,j=0;
					printf("\n");
						while(pstr!=NULL)
						{
							strcpy(mas[i],pstr);
							printf("%s\n",mas[i]);
							i++;
							pstr=strtok(NULL,sep);
						};
		int count=i;
		 	printf("count=%d\n",count);
				for (i=0;i<count-1;i++)
					for (j=i;j<count;j++)
						if (strcmp(mas[i],mas[j])>=0)
					 	{
					 		strcpy(temp,mas[i]);
					 		strcpy(mas[i],mas[j]);
					 		strcpy(mas[j],temp);
					 	}
				printf("Новый массив: ");
					for(i=0;i<count;i++)
						printf("%s\n",mas[i]);
						printf("Новая строка: ");
			for (i=0;i<count;i++)
				(strcat(strn,mas[i]));strcat(strn," ");
				puts(strn);										
}
