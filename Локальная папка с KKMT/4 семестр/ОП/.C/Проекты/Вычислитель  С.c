#include <stdio.h>
#include <locale.h>

int fact(int n);
main()
{
	 		setlocale(0,"");
	int n,m,f;
	printf ("¬ведите числа [n][m]: ");
	scanf ("%d%d", &n,&m);
	f=(fact(n))/(fact(m)*fact(n-m));
	printf ("C=%d", f);
}

int fact(int k)
{
	if (k==1)
	return 1;
	else return k*fact(k-1);
}
