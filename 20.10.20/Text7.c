/*Дана строка S и текстовый файл. Добавить строку S в начало файла.*/
#include <stdio.h>
#define MAXLEN 80

int main ()
{
	char *fname1 = "Open.txt";
    char *fname2 = "OUT.txt";
	FILE *f1 = fopen ("Open.txt","a+");
	FILE *f2 = fopen ("OUT.txt","w");
	char q[MAXLEN+1];
	int s;
	scanf ("%d",&s);
	fprintf (f2,"%d\n",s);
	while (fgets(q, MAXLEN , f1) != NULL) {
        fputs(q, f2);
    }
	fclose (f1);
	fclose (f2);
	remove(fname1);
    rename(fname2, fname1);
	getchar ();
	return 0;
}
