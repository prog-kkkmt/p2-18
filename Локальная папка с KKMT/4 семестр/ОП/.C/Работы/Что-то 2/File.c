#include <stdio.h>
#include <string.h>
#include <locale.h>
#include <time.h>
#include <stdlib.h>

void main()
{
	setlocale(0,"");
	srand(time(NULL));
	FILE *F1;
	FILE *F2;
	F1 = fopen("F1.txt","r");
	  if (F1 == NULL)
	   {
    		printf("Ошибка! Нет подходящего файла.");
          	getch();
       }
    int i,j,n,m,k,temp;
     
         fscanf(F1,"%d%d",&n,&m);
    int a[n][m];
    fclose(F1);
    F2=fopen("F2.txt","w");
         for(i=0;i<n;i++)
         	{
        		for(j=0;j<m;j++)
        			fprintf(F2,"%5d",rand()%100-50);
        					fprintf(F2,"\n");
		 	}
    fclose(F2);
    F2=fopen("F2.txt","r");
         for(i=0;i<n;i++)
        	 {
        		for(j=0;j<m;j++)
        			fscanf(F2,"%d",&a[i][j]);
		 	}
	for(i=0;i<n;i++)	 	
    	for(j=0;j<m-1;j++)
    		for(k=j;k<m;k++)
    			{
    				if(a[i][j]<a[i][k]){temp=a[i][j];a[i][j]=a[i][k];a[i][k]=temp;}
    			}
	F2=fopen("F2.txt","a");
	fprintf(F2,"\n");
         for(i=0;i<n;i++)
         	{
        		for(j=0;j<m;j++)
        			fprintf(F2,"%5d",a[i][j]);
        					fprintf(F2,"\n");
		 	}
    	fclose(F2);		
         	
}
