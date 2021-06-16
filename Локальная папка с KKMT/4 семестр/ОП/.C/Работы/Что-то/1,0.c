#include <stdio.h> 
#include <string.h>
#include <locale.h>

void main() 
{ 
	setlocale(0,"");
			char strl[255],sep[3]="/,";
				char *pstr;
			printf("¬ведите текст: ");
				gets(strl);
			printf("\n");
				pstr=strtok(strl,sep);
			printf("\n");
				printf("%s\n",pstr);
			}
		
