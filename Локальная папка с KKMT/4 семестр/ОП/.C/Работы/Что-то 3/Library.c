#include <stdlib.h>
#include <stdio.h>
#include <locale.h>
#include <string.h>

struct Library{
char name[30]; // ��� ������	
char book[30]; // �������� �����
int year; // ��� �������
};

void main()
{
	setlocale(0,""); 										 
	FILE *library1=fopen("library1.txt","r"); 				
	FILE *library; 											
		if(fopen==NULL)										
			{
				printf("!Error opening!");
				getchar();	
			}
    int i,j,n,k,m;											
    int min;
   printf("������� ���-�� ����: ");
    	fscanf(library1,"%d",&n);							
    struct Library lib[n],temp; 						
    	for(i=0;i<n;i++)
			{
				//printf("������� ������: ");
        			fscanf(library1,"%s",lib[i].name);		// ����� � ��������� ��������� ������
       			//printf("������� �������� �����: ");
        			fscanf(library1,"%s",lib[i].book);		// ����� � ��������� ��������� �������� �����
        		//printf("������� ��� �������: ");
        			fscanf(library1,"%d",&lib[i].year);     // ����� � ��������� ��������� ����
			}			
			fclose(library1);
			library=fopen("library.txt","w"); 				//�������� ����� liberary
	
   						fprintf(library,"                         __________\n");
     					fprintf(library,"                        |����������|\n");
     					fprintf(library," ____________________________________________________________\n");
    					fprintf(library,"|       �����      |   �������� �����   |     ��� �������    |\n");
    					fprintf(library,"|__________________|____________________|____________________|\n");
//����� �������
   		for (i=0;i<n;i++)
    		{
    			fprintf(library,"|%18s|%20s|%20d|\n",lib[i].name,lib[i].book,lib[i].year);				// ����� ������� � ��������� ��������
       			fprintf(library,"|__________________|____________________|____________________|\n");
			}
						printf("                         __________\n");
     					printf("                        |����������|\n");
     					printf(" ____________________________________________________________\n");
    					printf("|       �����      |   �������� �����   |     ��� �������    |\n");
    					printf("|__________________|____________________|____________________|\n");
//����� �������
   		for (i=0;i<n;i++)
    		{
    			printf("|%18s|%20s|%20d|\n",lib[i].name,lib[i].book,lib[i].year);						// ����� ������� � ������� 
       			printf("|__________________|____________________|____________________|\n");
			}
	fprintf(library,"\n");																				
    	for (i=0; i<n-1;i++)
    		for (j=i+1;j<n;j++)
	// ���������� �� �����, �� ����������� � ������ 3 ������ 
					if(lib[i].year>lib[j].year)
						{
							temp=lib[i];
					 		lib[i]=lib[j];
							lib[j]=temp;
						}			
		   		fprintf(library,"                    ____________________\n");
     			fprintf(library,"                   | ����� ������ ����� |\n");
     			fprintf(library," ____________________________________________________________\n");
    			fprintf(library,"|       �����      |   �������� �����   |     ��� �������    |\n");
    			fprintf(library,"|__________________|____________________|____________________|\n");
    		
   		for (i=0;i<n-7;i++)//-7 ��� ������ 3 ������, �� �������� ������ ������((( 
    		{
    			fprintf(library,"|%18s|%20s|%20d|\n",lib[i].name,lib[i].book,lib[i].year);
       			fprintf(library,"|__________________|____________________|____________________|\n");
			}
			
			   	fprintf(library,"\n");

//����������� �� ������			
    	for(i=0;i<n;i++)
			{
       			for(j=0;j<n;j++)
            		if(strcmp(lib[i].name,lib[j].name)<0)  						// ��������� ���� � ���������� ����
						{
							temp=lib[i]; 
							lib[i]=lib[j]; 
							lib[j]=temp;
						}
   		    }
   		    
		   		fprintf(library,"                    ____________________\n");
     			fprintf(library,"                   |���������� �� ������|\n");
     			fprintf(library," ____________________________________________________________\n");
    			fprintf(library,"|       �����      |   �������� �����   |     ��� �������    |\n");
    			fprintf(library,"|__________________|____________________|____________________|\n");
    		
   		for (i=0;i<n;i++)
    		{
    			fprintf(library,"|%18s|%20s|%20d|\n",lib[i].name,lib[i].book,lib[i].year);
       			fprintf(library,"|__________________|____________________|____________________|\n");
			}
			fclose(library);// �������� liberary
			int key;
			printf("\n");
			printf("�������� ���� �� �������:\n");
			printf("|1. ����� �� ������.  |\n");
			printf("|2. ����� �� ��������.|\n");
			scanf("%d",&key);
	switch(key)     // ������ ���� ����...
		{
			
			case 1: // ���� 1 
				{
				
				library=fopen("library.txt","a"); // �������� ����� liberary
				fprintf(library,"\n");
				char name[30];
 					printf("������� ������ (�������� ���������� �����): ");
					 	scanf("%s",name);
	 						fprintf(library,"                    ____________________\n");
     						fprintf(library,"                   |   ����� �� ������  |\n");
     						fprintf(library," ____________________________________________________________\n");
    						fprintf(library,"|       �����      |   �������� �����   |     ��� �������    |\n");
    						fprintf(library,"|__________________|____________________|____________________|\n");
		
        			for (i=0; i<n;i++)
        				 {
         					if (strcmp(lib[i].name,name)==0) // �������� ���� � ����� 
		 						{
    								fprintf(library,"|%18s|%20s|%20d|\n",lib[i].name,lib[i].book,lib[i].year);
       								fprintf(library,"|__________________|____________________|____________________|\n");
								}
							//else if (i==n-1) // ������ �� ��� �� �������� � ���� ��� ������ �� ��������
							//printf("������� ������ ���, ���������� ��� ���...\n");
						}
				fclose(library);
				break;
				}
			case 2:
				{
					library=fopen("library.txt","a");
					fprintf(library,"\n");
						char name[30];
 					printf("������� �������� (������� ���������� �����): ");
	 					scanf("%s",name);
	 						fprintf(library,"                   ______________________\n");
     						fprintf(library,"                  |   ����� �� ��������  |\n");
     						fprintf(library," ____________________________________________________________\n");
    						fprintf(library,"|       �����      |   �������� �����   |     ��� �������    |\n");
    						fprintf(library,"|__________________|____________________|____________________|\n");
		
         			for (i=0; i<n;i++)
         				{
         					if (strcmp(lib[i].book,name)==0) // �������� ���� � ����� 
		 						{
    								fprintf(library,"|%18s|%20s|%20d|\n",lib[i].name,lib[i].book,lib[i].year);
       								fprintf(library,"|__________________|____________________|____________________|\n");
								}
							//else if (i==n-1)// ������ �� ��� �� �������� � ���� ��� ������ �� ��������
							//printf("������� �������� ���, ���������� ��� ���...\n");
						}
		 			fclose(library); // ��������� �������� 
		 			break;
				}
			default: puts("����� ������ ���, ���������� ��� ���...\n"); // ����� ������ ���� ����� � ����� ������ �������)
		}
}

