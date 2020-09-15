/*Замена переменных местами. Слесарев 15.09.2020 */
#include <stdio.h>
void swap (int *pa, int *pb){
	int t=*pa;
	*pa=*pb;
	*pb=t;
}
int main (){
	int a,b;
	printf("Vvedite chislo:");
	scanf ("%d%d",&a,&b);
	printf ("%d %d\n",a,b);
	swap (&a,&b);
	printf ("%d %d\n",a,b);
	return 0;
}