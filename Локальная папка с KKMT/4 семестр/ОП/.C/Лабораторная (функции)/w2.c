void inMatrix(int p, int o, int c[p][o]);
void outMatrix(int p, int o, int c[p][o]);
void compostion(int p, int o, int l, int c[p][o], int y[p][o], int z[p][o]);

int w2()
{
	system("cls");
		int n,m,h;
		int a[h][n];
		int b[m][n];
		int d[h][n];
	printf ("������� ���-�� ��������� ��� 1 ������� [a][b]: ");
			scanf("%d%d",&h,&n);
			inMatrix(h,n,a);
		printf ("������� ���-�� ��������� ��� ������������ 1 � 2 ������� [M]: ");
			scanf("%d",&m);	
			inMatrix(h,m,b);
		printf ("\n1 ������:\n"); outMatrix(h,n,a);	
		printf ("\n2 ������:\n"); outMatrix(h,n,b);
		compostion(h,n,m,a,b,d);
		printf("\n������������ 1 ������� �� 2:\n"); outMatrix(h,m,d);	
			getch();
}

