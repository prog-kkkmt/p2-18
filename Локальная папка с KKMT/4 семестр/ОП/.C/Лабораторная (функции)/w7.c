void in(int p, int *c);
void out(int p, int *c);
void sortT(int p, int *c);

int w7()
{  
	    system("cls");
	int n,m;
		printf ("¬ведите кол-во элементов дл€ 1 массива: ");
			scanf("%d",&n); int a[n];
		printf ("¬ведите кол-во элементов дл€ 2 массива: ");
			scanf("%d",&m);	int b[m];
			in(n,a);
		printf ("\n1 массив: \n"); out(n,a);
			sortT(n,a);
		printf ("\n1 отсортированный массив: \n"); out(n,a);
			in(m,b);
		printf ("\n2 массив: \n"); out(m,b);
			sortT(m,b);
		printf ("\n2 отсортированный массив: \n"); out(m,b);
			getch();
}

