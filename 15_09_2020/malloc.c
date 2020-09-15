/*Ввод и вывод массива через маллок.  Слесарев 15.09.2020 */
#include <stdio.h>
#include <stdlib.h>
int main()
{
	int n;
	printf ("Vvedite col-vo elementov: ");
	scanf ("%d",&n);
	int *pa=(int *)malloc(sizeof (int)*n);
	for (int i=0;i<n;i++){
		printf ("Vvedite %d elemnt:\t",i+1);
		scanf("%d",pa+i);
	}
	for (int i=0;i<n;i++)
		printf ("%d\t",*(pa+i));
	free (pa);
	return 0;
}