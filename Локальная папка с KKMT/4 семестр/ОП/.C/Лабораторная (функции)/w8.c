void in(int n, int *c);
void out(int n, int *c);
void outSumMatrix(int n, int m, int *a, int *b);
void outMatrix(int p, int o, int c[p][o]);

int w8()
{
	int n,i,j,m,k;
  		system("cls");
  		int c[n][m];
    printf ("������� ���-�� ��������� ��� 1 �������: ");
			scanf("%d",&n); int a[n]; 
	printf ("������� ���-�� ��������� ��� 2 �������: ");
		scanf("%d",&m); int b[m];
			in(n,a); in(m,b);
    printf("1 ������: ");out(n,a);
    printf("2 ������: ");out(m,b);
 	 printf("\n\n����� ��������: \n"); outSumMatrix(n,m,a,b);			
}
