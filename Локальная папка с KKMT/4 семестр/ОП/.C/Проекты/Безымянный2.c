#include <stdio.h>
int NOD(int a, int b);
main()
{
	int x1,x2,f;
	printf("Vvedite 2 chisla: ");
	scanf ("%d%d",&x1,&x2);
	f=NOD(x1,x2);
	printf ("NOD (%d,%d)= %d", x1,x2,f);
}
int NOD (int a, int b)
{
	if (a==b)
	return a;
	else if (a>b) return NOD (a-b,b);
	else return NOD (a,b-a);
}
