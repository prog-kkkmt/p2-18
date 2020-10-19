#include <stdio.h>

int main ()
{
	FILE *f1 = fopen ("Out.txt","w");
	int N,K;
	printf ("Vvedite N i K: ");
	scanf ("%d %d", &N, &K);
	for (int i=0; i<N;i++){
		for (int j=0;j<K;j++)
		{
			fprintf(f1,"*");
		}
		fprintf (f1,"\n");
	}
	fclose (f1);
	return 0;
}

