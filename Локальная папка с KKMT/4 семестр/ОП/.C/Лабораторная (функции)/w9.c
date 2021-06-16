void inMatrix(int n, int m, int a[n][m]);
void outMatrix(int n, int m, int a[n][m]);
int detect(int a[3][3]);

int w9()
{
	system("cls");
    int mas[3][3];
    int n,m;
    	printf ("Введите кол-во элементов для матрицы [3][3]: ");
			scanf("%d%d",&n,&m);
				inMatrix(n,m,mas);
		printf ("Матрица А:\n");outMatrix(n,m,mas);
     printf("Определитель матрицы A:%d\n",detect(mas));
}

