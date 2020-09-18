/*Даны целые числа K, N и набор из N вещественных чисел: A1, A2, …, AN. Вывести K-e степени чисел из данного набора:

(A1)K, (A2)K, …, (AN)K.*/
#include <math.h>
#include <stdio.h>
int main()
{
	int n,k;
	printf ("Введите N:\n");
	scanf ("%d\n",&n);
	int a[n];
	printf ("Введите K:\n");
	scanf ("%d\n",&k);
	for (int i = 0;i < n; i++)
	{
		scanf ("%d " ,&a[i]);
	} 
	for (int i = 0; i < n; ++i)
	{
		printf ("%f ",pow(a[i],k));
	}
	return 0;
}