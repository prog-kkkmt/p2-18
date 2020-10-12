/*Описать функцию Power1(A, B) вещественного типа, находящую величину AB по формуле AB = exp(B·ln(A)) (параметры A и B — вещественные). В случае нулевого или отрицательного параметра A функция возвращает 0. С помощью этой функции найти степени AP, BP, CP, если даны числа P, A, B, C.
Слесарев А.М.*/

#include <stdio.h>
#include <math.h>
 
float Power1 (float a, float b)
{
	if (a>0)
		{
			a = pow(a,b);
			return (a);
		}
	else 
		return 0;	  
}

int main ()
{
	float P,A,B,C;
	printf ("Введите P, A, B, C:\n");
	scanf ("%f %f %f %f", &P, &A, &B, &C);
	printf ("A^p = %.2f; B^p = %.2f; C^p = %.2f;", Power1(A,P),Power1(B,P),Power1(C,P));

}
/*Функция работает опять на Repl.it*/