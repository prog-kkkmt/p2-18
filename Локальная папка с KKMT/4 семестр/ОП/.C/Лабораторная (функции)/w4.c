void inMatrix(int p, int o, int c[p][o]);
void outMatrix(int p, int o, int c[p][o]);
void Symmetrical(int n, int m, int c[n][m], int a[n][m]);
void Skew(int n, int m, int c[n][m], int a[n][m]);

int w4()
{
		system("cls");
	int n,m,k;
	int c[n][m];
	 printf ("Введите кол-во элементов для 1 массива [a][b]: ");
			scanf("%d%d",&k,&n); int a[k][n];
			inMatrix(k,n,a);
		printf("\nСгенерированная матрица:\n"); outMatrix(k,n,a);
		Symmetrical(k,n,c,a);
		printf("\nCимметричная часть:\n"); outMatrix(k,n,c);
		Skew(k,n,c,a); 
		printf("\nКососиметричная часть:\n"); outMatrix(k,n,c);
}


