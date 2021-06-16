#include <stdio.h>
#include <conio.h>
#include <time.h>
#include <locale.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>
#include "w1.c"
#include "w2.c"
#include "w3.c"
#include "w4.c"
#include "w6.c"
#include "w7.c"
#include "w8.c"
#include "w9.c"
#include "w11.c"
#include "w12.c"
#include "w9_2.c"
void main()
{ 
	system("title Menu by (ivauuka99)");
 		setlocale(0,"");
 			srand(time(NULL));
 		int key;
 	while(1)
 	{
 		system("cls");
 		printf("|Выберите соответствующий пунк задания:|\n");
 		printf("========================================\n");
  		printf("|1 |            Задание №1             |\n");
  		printf("|2 |            Задание №2             |\n");
  		printf("|3 |            Задание №3             |\n");
		printf("|4 |            Задание №4             |\n");  		
	//	printf("|5 |            Задание №5             |\n");  		
		printf("|6 |            Задание №6             |\n");  		
		printf("|7 |            Задание №7             |\n");  		
		printf("|8 |            Задание №8             |\n");  	
	    printf("|9 |            Задание №9             |\n");
	//	printf("|10|            Задание №10            |\n");
		printf("|11|            Задание №11            |\n");
		printf("|12|            Задание №12            |\n");
		printf("|0 |              Выход                |\n");
		printf("========================================\n");
		printf("|Скрытое задание под 92 номером! 9v2   |\n");
		scanf("%d",&key);
    		switch(key)
    			{ 
					case 1: w1();break;
					case 2: w2();break;
					case 3: w3();break;
					case 4: w4();break;
					case 6: w6();break;
					case 7: w7();break;
					case 8: w8();break;
					case 9: w9();break;
					case 92: w9_2();break;
					case 11: w11();break;
					case 12: w12();break;
      				case 0: exit(0); 
      				default: printf("!ErroR!");
				}
				getch();
	}
}

void in(int n, int *c)
{
	int i;
	for(i=0;i<n;i++)
		c[i]=rand()%100-20;
}

void out(int n, int *c)
{
	int i;
	for(i=0;i<n;i++)
		printf("%d ",c[i]);
		printf("\n");
}

void sort(int n, int *c)
{
	int temp;
	int i,j;
	for(i=0;i<n-1;i++)
		for(j=i;j<n;j++)
			if(c[i]>c[j]){temp=c[i];c[i]=c[j];c[j]=temp;}
}

void inMatrix(int n, int m, int a[n][m])
{
	int i,j;
	for( i=0;i<n;i++)
			for (j=0;j<m;j++)
    				a[i][j] = rand()%100-30;
}

void outMatrix(int n, int m, int c[n][m])
{
	int i,j;
	for(i=0;i<n;i++)
	{
		for (j=0;j<m;j++) 
		{
			printf("%5d",c[i][j]);
			
		}
		printf("\n");
	}
}

void compostion(int p, int o, int l, int a[p][o], int b[o][l], int c[p][l])
{
	int i,j,jj;
	for(i=0;i<p;i++)
		for (j=0;j<o;j++) 
			{
				c[i][j]=0;
				for(jj=0;jj<l;jj++)
				c[i][j]+=a[i][jj]*b[jj][j];
			}
}

void Symmetrical(int n, int m, int c[n][m], int a[n][m])
{
	int i,j;
	for(i=0;i<n;i++)
    	{
        	for(j=0;j<m;j++)
        		{
        			c[i][j]=0;
            		c[i][j] = (a[i][j]+a[j][i])/2;
        		}
    	}
}

void Skew(int n, int m, int c[n][m], int a[n][m])
{
	int i,j;
	for(i=0;i<n;i++)
    	{
        	for( j=0;j<m;j++)
        		{
        			c[i][j]=0;
            		c[i][j] = (a[i][j]-a[j][i])/2;
        		}
    	}
}

int max(int l, int *a)
{
	int i,max;
	max=a[0];
	for (i=1; i<l;i++)
   			 if (a[i]>max) {max=a[i];}
   			 	return max;
}

int min(int k, int *a)
{
	int i,min;
	min=a[0];
	for (i=1; i<k;i++)
   			 if (a[i]<min) {min=a[i];}
   				 return min;
}

void sortT(int n, int *c)
{
	int temp;
	int i,j;
	for(i=0;i<n-1;i++)
		for(j=i;j<n;j++)
			if(c[i]<c[j]){temp=c[i];c[i]=c[j];c[j]=temp;}
}


void outSumMatrix(int n, int m, int *a, int *b)
{
	int c[n][m];
	int i,j,jj;
    for(i=0;i<n;i++)
    	{
        	for(j=0;j<m;j++)
        		{
            		c[i][j] = (a[i]*b[j]);
            		printf("%6d",c[i][j]);
        		}
       		printf("\n");
	    }
}

float Scalc(int s, float eps)
{
	int n=1,m=n;
		float a=0,b=0,c=0;
				c=pow(s,n)/m;
					b+=c;	
	while(fabsf(b-a)>eps) {n+=2;a=b;m=m*(n-1)*m;c=pow(s,n)/m;b+=c;}
		return a;
}

int detect(int a[3][3])
{
    return a[0][0]*a[1][1]*a[2][2]+a[2][0]*a[0][1]*a[1][2]+a[1][0]*a[2][1]*a[0][2]-a[2][0]*a[1][1]*a[0][2]-a[0][0]*a[2][1]*a[1][2]-a[1][0]*a[0][1]*a[2][2];
}

void MatrixC(int n, int m, int a[n][m], int b[n][m], int c[n][m])
{
	int i,j;
	for (i=0; i<n; i++) 
	{
        for (j=0; j<m; j++) 
		{
			if (a[i][j] > b[i][j]) {c[i][j] = a[i][j];}
			else c[i][j] = b[i][j]; 
		}
	}
}

void MatrixD(int n, int m, int a[n][m], int b[n][m], int d[n][m])
{
	int i,j;
	for (i=0; i<n; i++) 
	{
        for (j=0; j<m; j++) 
		{
			if (a[i][j] < b[i][j]) {d[i][j] = a[i][j];}
			else d[i][j] = b[i][j]; 
		}
	}
}







