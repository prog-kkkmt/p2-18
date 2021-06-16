int **array(int ROW, int COL)
{
	int i,**p= NULL;
		p = (int**) malloc(ROW * sizeof(int*));
			for (i = 0; i < ROW; i++)
		p[i] = (int*) malloc(COL * sizeof(int));
	return p;
}

void inMatrix(int n, int m, int a[n][m])
{
	int i,j;
	for( i=0;i<n;i++)
			for (j=0;j<m;j++)
    				a[i][j] = rand()%10;
}

void outMatrix(int n, int m, int c[n][m])
{
	extern FILE *tr;
	int i,j;
	for(i=0;i<n;i++)
	{
		for (j=0;j<m;j++) 
		{
			fprintf(tr,"%5d",c[i][j]);
			
		}
		fprintf(tr,"\n");
	}
}
	    
	/*void array_destroyer(int **p,  int ROW)
		{
		    int i;
		    for ( i = 0; i < ROW ; i++)
		              free(p[i]);
		    free(p);
		}*/

