#include <stdio.h>
#include <string.h>
#include <locale.h>
#include <stdlib.h>



void main()

{
FILE *inputfile;
FILE *outputfile;

int m,n,i,j,k,a,temp,

inputfile = fopen("matrica1.txt", "r");
if (inputfile==NULL)
printf("ERROR");

     fscanf(inputfile, "%d%d",&m,&n);
     printf("%d %d",m,n);

     int mas[m][n];

     fclose(inputfile);
outputfile=fopen("matrica2.txt","w");
srand(time(NULL));
for(i=0; i<m; i++)
{
for(j=0; j<n; j++)
{fprintf(outputfile, "%4d", rand()%10-5);
fprintf(outputfile,"\n");
}
fclose(outputfile);
outputfile=fopen("matrica1.txt","r");
for(i=0;i<n;i++)
        	 {
        		for(j=0;j<m;j++)
        			fscanf(outputfile,"%d",&a[i][j]);
		 	}
	for(i=0;i<n;i++)
    	for(j=0;j<m-1;j++)
    		for(k=j;k<m;k++)
    			{
    				if(a[i][j]<a[i][k]){temp=a[i][j];a[i][j]=a[i][k];a[i][k]=temp;}
    			}
	outputfile=fopen("matrica2","a");
	fprintf(outputfile,"\n");
         for(i=0;i<n;i++)
         	{
        		for(j=0;j<m;j++)
        			fprintf(outputfile,"%5d",a[i][j]);
        					fprintf(outputfile,"\n");
		 	}
    	fclose(outputfile);

}
