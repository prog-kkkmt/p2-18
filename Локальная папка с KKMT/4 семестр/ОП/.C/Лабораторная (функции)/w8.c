void in(int n, int *c);
void out(int n, int *c);
void outSumMatrix(int n, int m, int *a, int *b);
void outMatrix(int p, int o, int c[p][o]);

int w8()
{
	int n,i,j,m,k;
  		system("cls");
  		int c[n][m];
    printf ("¬ведите кол-во элементов дл€ 1 массива: ");
			scanf("%d",&n); int a[n]; 
	printf ("¬ведите кол-во элементов дл€ 2 массива: ");
		scanf("%d",&m); int b[m];
			in(n,a); in(m,b);
    printf("1 массив: ");out(n,a);
    printf("2 массив: ");out(m,b);
 	 printf("\n\n—умма массивов: \n"); outSumMatrix(n,m,a,b);			
}
