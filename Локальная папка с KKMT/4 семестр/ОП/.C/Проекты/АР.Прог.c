#include <stdio.h>
#include <locale.h>

int pr(int q, int w, int e);
main()
{
	 		setlocale(0,"");
	int n,m,l,ar;
	printf ("¬ведите числа [n][m][l]: ");
	scanf ("%d%d", &n,&m,&l);
	pr(n,m,l);
	ar=pr(n,m,l);
	printf ("јр.прогресси€:%d",ar);
}

int pr(int q, int w, int e)
{
	int rez=0;
	if(q==0) return 0;
	else rez=w+pr(q-1,w+e,e); return rez;
}
