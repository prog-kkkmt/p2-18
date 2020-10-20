/*Text22. Дано целое число K (0 < K < 10) и текстовый файл, содержащий более K строк. Удалить из файла последние K строк.*/
#include <stdio.h>
#include <unistd.h>
#define MAXLEN 80

int main() {
	int i=0,K;
	printf ("Vvedite K:");
	scanf ("%d",&K);
    char *fname1 = "0pen.txt";
    char *fname2 = "tmp.txt";
    FILE *f1 = fopen(fname1, "r");
    FILE *f2 = fopen(fname2, "w");
    char s[MAXLEN];
    while (fgets(s, MAXLEN + 1, f1) != NULL) {
        i++;
    }
    i-=K;
    for (int j=0;j<i;j++)
    {
    	fgets(s, MAXLEN + 1, f1);
        fputs(s, f2);
    }
    fclose(f2);
    fclose(f1);
    remove(fname1);
    rename(fname2, fname1);

    getchar();

    return 0;
}
