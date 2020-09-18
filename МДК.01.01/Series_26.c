/*Даны целые числа K, N и набор из N вещественных чисел: A1, A2, …, AN. Вывести K-e степени чисел из данного набора:

(A1)K, (A2)K, …, (AN)K.*/
#include <math.h>
#include <stdio.h>
int main()
{
	int n,k;
	printf ("Введите N:");
	scanf ("%d",&n);
	int a[n];
	printf ("Введите K:");
	scanf ("%d",&k);
	for (int i = 0;i < n; i++)
	{
		scanf ("%d" ,&a[i]);
	} 
	for (int i = 0; i < n; ++i)
	{
		printf ("%.0f ",pow(a[i],k));
	}
	return 0;
}