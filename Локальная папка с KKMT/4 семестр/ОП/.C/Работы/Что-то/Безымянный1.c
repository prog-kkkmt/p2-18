#include <stdio.h>
#include <string.h>


int main(void)
{
	setlocale(0,"");
	char n[10];
	int p;
	char BMW[3]="BMW";
		char Audi[4]="Audi";
	scanf("%s%d", &n, &p);
	if (strcmp(BMW,n)==1)
		{
			if(p>=1500)
		 	printf("%s %d",n,p);
			 else printf("ХУЙ, гуляй дядя")	;
		}
	else if(strcmp(Audi,n)==1)
		{
			if(p>=15000)
		 	printf("%s %d",n,p);	
		}
	else 
	printf("ХУЙ, гуляй дядя");
}
