#include <stdio.h>

int main ()
{
	FILE *f1 = fopen ("Out2.txt","w");
	int N;
	char a='a';
	printf ("Vvedite N (1<N<27): ");
	scanf ("%d", &N);
	for (int i=1; i<N+1;i++){
		for (int j=0;j<i;j++)
		{
			fprintf(f1,"%c",a);
			a++;
		}
		fprintf (f1,"\n");
	}
	fclose (f1);
	return 0;
}
