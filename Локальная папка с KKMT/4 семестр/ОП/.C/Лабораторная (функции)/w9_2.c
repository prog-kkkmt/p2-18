int det(int a[3][3]);

int w9_2()
{
	system("cls");
    int a[3][3],j,q;
    printf ("������� ������� �� �������:\n");
    printf ("[][][]\n");
    printf ("[][][]\n");
    printf ("[][][]\n");
    	for ( j=0; j<3; j++ )
     		for ( q=0; q<3; q++ )
			  scanf("%d",&(a[j][q]));
     printf("������������ ������� A:%d\n",detect(a));
}
