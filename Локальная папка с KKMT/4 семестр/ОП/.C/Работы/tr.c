#include <stdio.h>
#include <conio.h>
#include <time.h>
#include <locale.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>
#include "trfunc.c"
FILE *tr;
int **array(int ROW, int COL);
void inMatrix(int p, int o, int c[p][o]);
void outMatrix(int p, int o, int c[p][o]);

void main()
{
	int **matrix,i,j,m,n;
	setlocale(0,""); 										 
	//FILE *tr;														
		if(fopen==NULL){printf("!Error opening!");getchar();}	
		tr=fopen("tr.txt","w"); 
			printf("¬ведите кол-во [n][m]="); scanf("%d%d",&n,&m);int a[n][m]; inMatrix(n,m,a);
    matrix = array(n,m);
	outMatrix(n,m,a);
	fclose(tr);
		tr=fopen("tr.txt","w"); 
}
 



