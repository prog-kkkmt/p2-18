/*Даны целые числа K и N (N > 0). Вывести N раз число K.*/
#include <stdio.h>
int main ()
{
	int n,k;
	scanf ("%d%d",&n,&k);
	for (int i = 0; i<k;i++)
	{
		printf("%d ",n );
	}
}