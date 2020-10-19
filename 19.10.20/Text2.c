#include <stdio.h>

int main ()
{
	FILE *f1 = fopen ("Out2.txt","w");
	int N;
	char a='a',b;
	printf ("¬ведите N (1<N<27): ");
	scanf ("%d", &N);
	for (int i=1; i<N+1;i++){
		b=a;
		for (int j=0;j<i;j++)
		{
			fprintf(f1,"%c",b);
			b++;
		}
		fprintf (f1,"\n");
	}
	fclose (f1);
	return 0;
}
