void in(int n, int *c);
void out(int n, int *c);
int max(int l, int *a);
int min(int k, int *a);

int w6()
{
  		system("cls");
  	int n,m,c;
		printf ("������� ���-�� ��������� ��� 1 �������: ");
			scanf("%d",&n); int a[n];
		printf ("������� ���-�� ��������� ��� 2 �������: ");
			scanf("%d",&m);	int b[m];
			in(n,a);
		printf ("\n1 ������: "); out(n,a);
		printf("\n������������: %d\n",max(n,a));
		printf("�����������: %d\n",min(n,a));
			in(m,b);
		printf ("\n2 ������: "); out(m,b);
		printf("\n������������: %d\n", max(m,b)); 
		printf("�����������: %d\n",min(m,b));
			getch();
}
	
