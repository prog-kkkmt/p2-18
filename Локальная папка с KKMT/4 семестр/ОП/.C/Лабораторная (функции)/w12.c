void inMatrix(int n, int m, int a[n][m]);
void outMatrix(int n, int m, int a[n][m]);
void MatrixC(int n, int m, int a[n][m], int b[n][m], int c[n][m]);
void MatrixD(int n, int m, int a[n][m], int b[n][m], int s[n][m]);

int w12()
{
		system("cls");
	int n,m,o,s;
	int c[n][m];
		int d[n][m];
	 printf ("������� ���-�� ��������� ��� ������� 1 [a][b]: ");
		scanf("%d%d",&n,&m);int a[n][m]; inMatrix(n,m,a);
	printf("\n��������������� ������� A:\n");outMatrix(n,m,a);
    	 printf ("������� ���-�� ��������� ��� ������� 2 [a][b]: ");
		scanf("%d%d",&o,&s);int b[o][s]; inMatrix(o,s,b);
	printf("\n��������������� ������� B:\n"); outMatrix(o,s,b);
    MatrixC(n,m,a,b,c);
    	printf("\n������� C=max(a(i,j),b(i,j)):\n");outMatrix(n,m,c);
    MatrixD(o,s,a,b,d);
    	printf("\n������� D=min(a(i,j),b(i,j)):\n");outMatrix(o,s,d);
}
