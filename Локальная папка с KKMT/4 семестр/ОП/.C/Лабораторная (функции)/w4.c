void inMatrix(int p, int o, int c[p][o]);
void outMatrix(int p, int o, int c[p][o]);
void Symmetrical(int n, int m, int c[n][m], int a[n][m]);
void Skew(int n, int m, int c[n][m], int a[n][m]);

int w4()
{
		system("cls");
	int n,m,k;
	int c[n][m];
	 printf ("������� ���-�� ��������� ��� 1 ������� [a][b]: ");
			scanf("%d%d",&k,&n); int a[k][n];
			inMatrix(k,n,a);
		printf("\n��������������� �������:\n"); outMatrix(k,n,a);
		Symmetrical(k,n,c,a);
		printf("\nC����������� �����:\n"); outMatrix(k,n,c);
		Skew(k,n,c,a); 
		printf("\n��������������� �����:\n"); outMatrix(k,n,c);
}


