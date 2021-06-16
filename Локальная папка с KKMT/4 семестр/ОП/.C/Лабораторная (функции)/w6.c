void in(int n, int *c);
void out(int n, int *c);
int max(int l, int *a);
int min(int k, int *a);

int w6()
{
  		system("cls");
  	int n,m,c;
		printf ("Введите кол-во элементов для 1 массива: ");
			scanf("%d",&n); int a[n];
		printf ("Введите кол-во элементов для 2 массива: ");
			scanf("%d",&m);	int b[m];
			in(n,a);
		printf ("\n1 массив: "); out(n,a);
		printf("\nМаксимальное: %d\n",max(n,a));
		printf("Минимальное: %d\n",min(n,a));
			in(m,b);
		printf ("\n2 массив: "); out(m,b);
		printf("\nМаксимальное: %d\n", max(m,b)); 
		printf("Минимальное: %d\n",min(m,b));
			getch();
}
	
