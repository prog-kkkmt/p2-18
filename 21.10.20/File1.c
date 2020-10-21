/*File1. Дана строка S. Если S является допустимым именем файла, то создать пустой файл с этим именем и вывести True.
 Если файл с именем S создать нельзя, то вывести False.*/
#include <stdio.h>
#include <string.h>

void main (){
	char s[],w[]="\/:*\"?<>|";
	gets (s);
	int n=0;

	for (int i = 0;i < strlen(s); i++)
	{
		for (int j = 0;j = strlen(w);j++)
		{
			if (s[i] == w[j])
				n++;
		}
		
	}
	if (n==0)
		printf ("True");
	else
		printf ("False");
	
}