void in(int p, int *c);
void out(int p, int *c);
void sort(int p, int *c);

int w1()
{  
	    system("cls");
	int n,m;
		printf ("������� ���-�� ��������� ��� 1 �������: ");
			scanf("%d",&n); int a[n];
		printf ("������� ���-�� ��������� ��� 2 �������: ");
			scanf("%d",&m);	int b[m];
			in(n,a);
		printf ("\n1 ������: \n"); out(n,a);
			sort(n,a);
		printf ("\n1 ��������������� ������: \n"); out(n,a);
			in(m,b);
		printf ("\n2 ������: \n"); out(m,b);
			sort(m,b);
		printf ("\n2 ��������������� ������: \n"); out(m,b);
			getch();
}
