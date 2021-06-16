#include <stdlib.h>
#include <stdio.h>
#include <locale.h>
#include <string.h>

struct Library{
char name[30]; // имя автора	
char book[30]; // название книги
int year; // год издания
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
   printf("Введите кол-во книг: ");
    	fscanf(library1,"%d",&n);							
    struct Library lib[n],temp; 						
    	for(i=0;i<n;i++)
			{
				//printf("Введите автора: ");
        			fscanf(library1,"%s",lib[i].name);		// Поиск в текстовом документе автора
       			//printf("Введите название книги: ");
        			fscanf(library1,"%s",lib[i].book);		// Поиск в текстовом документе названия книги
        		//printf("Введите год издания: ");
        			fscanf(library1,"%d",&lib[i].year);     // Поиск в текстовом документе года
			}			
			fclose(library1);
			library=fopen("library.txt","w"); 				//открытие фойла liberary
	
   						fprintf(library,"                         __________\n");
     					fprintf(library,"                        |Библиотека|\n");
     					fprintf(library," ____________________________________________________________\n");
    					fprintf(library,"|       Автор      |   Название книги   |     Год издания    |\n");
    					fprintf(library,"|__________________|____________________|____________________|\n");
//Вывод массива
   		for (i=0;i<n;i++)
    		{
    			fprintf(library,"|%18s|%20s|%20d|\n",lib[i].name,lib[i].book,lib[i].year);				// вывод массива в текстовый документ
       			fprintf(library,"|__________________|____________________|____________________|\n");
			}
						printf("                         __________\n");
     					printf("                        |Библиотека|\n");
     					printf(" ____________________________________________________________\n");
    					printf("|       Автор      |   Название книги   |     Год издания    |\n");
    					printf("|__________________|____________________|____________________|\n");
//Вывод массива
   		for (i=0;i<n;i++)
    		{
    			printf("|%18s|%20s|%20d|\n",lib[i].name,lib[i].book,lib[i].year);						// вывод массива в консоль 
       			printf("|__________________|____________________|____________________|\n");
			}
	fprintf(library,"\n");																				
    	for (i=0; i<n-1;i++)
    		for (j=i+1;j<n;j++)
	// Сортировка по датам, по возрастанию и вывода 3 данных 
					if(lib[i].year>lib[j].year)
						{
							temp=lib[i];
					 		lib[i]=lib[j];
							lib[j]=temp;
						}			
		   		fprintf(library,"                    ____________________\n");
     			fprintf(library,"                   | Самые старые книги |\n");
     			fprintf(library," ____________________________________________________________\n");
    			fprintf(library,"|       Автор      |   Название книги   |     Год издания    |\n");
    			fprintf(library,"|__________________|____________________|____________________|\n");
    		
   		for (i=0;i<n-7;i++)//-7 для вывода 3 данных, не придумал другой способ((( 
    		{
    			fprintf(library,"|%18s|%20s|%20d|\n",lib[i].name,lib[i].book,lib[i].year);
       			fprintf(library,"|__________________|____________________|____________________|\n");
			}
			
			   	fprintf(library,"\n");

//Сортировака по Автору			
    	for(i=0;i<n;i++)
			{
       			for(j=0;j<n;j++)
            		if(strcmp(lib[i].name,lib[j].name)<0)  						// Сравнение слов и сортировка слов
						{
							temp=lib[i]; 
							lib[i]=lib[j]; 
							lib[j]=temp;
						}
   		    }
   		    
		   		fprintf(library,"                    ____________________\n");
     			fprintf(library,"                   |Сортировка по Автору|\n");
     			fprintf(library," ____________________________________________________________\n");
    			fprintf(library,"|       Автор      |   Название книги   |     Год издания    |\n");
    			fprintf(library,"|__________________|____________________|____________________|\n");
    		
   		for (i=0;i<n;i++)
    		{
    			fprintf(library,"|%18s|%20s|%20d|\n",lib[i].name,lib[i].book,lib[i].year);
       			fprintf(library,"|__________________|____________________|____________________|\n");
			}
			fclose(library);// закрытие liberary
			int key;
			printf("\n");
			printf("Выберете один из пунктов:\n");
			printf("|1. Поиск по Автору.  |\n");
			printf("|2. Поиск по Названию.|\n");
			scanf("%d",&key);
	switch(key)     // своего рода меню...
		{
			
			case 1: // кейс 1 
				{
				
				library=fopen("library.txt","a"); // открытин файла liberary
				fprintf(library,"\n");
				char name[30];
 					printf("Введите Автора (которого необходимо найти): ");
					 	scanf("%s",name);
	 						fprintf(library,"                    ____________________\n");
     						fprintf(library,"                   |   Выбор по Автору  |\n");
     						fprintf(library," ____________________________________________________________\n");
    						fprintf(library,"|       Автор      |   Название книги   |     Год издания    |\n");
    						fprintf(library,"|__________________|____________________|____________________|\n");
		
        			for (i=0; i<n;i++)
        				 {
         					if (strcmp(lib[i].name,name)==0) // Проверка слов и вывод 
		 						{
    								fprintf(library,"|%18s|%20s|%20d|\n",lib[i].name,lib[i].book,lib[i].year);
       								fprintf(library,"|__________________|____________________|____________________|\n");
								}
							//else if (i==n-1) // Почему то как не пробовал с если оно вообще не работает
							//printf("Данного автора нет, попробуйте ешё раз...\n");
						}
				fclose(library);
				break;
				}
			case 2:
				{
					library=fopen("library.txt","a");
					fprintf(library,"\n");
						char name[30];
 					printf("Введите Название (которое необходимо найти): ");
	 					scanf("%s",name);
	 						fprintf(library,"                   ______________________\n");
     						fprintf(library,"                  |   Выбор по Названию  |\n");
     						fprintf(library," ____________________________________________________________\n");
    						fprintf(library,"|       Автор      |   Название книги   |     Год издания    |\n");
    						fprintf(library,"|__________________|____________________|____________________|\n");
		
         			for (i=0; i<n;i++)
         				{
         					if (strcmp(lib[i].book,name)==0) // Проверка слов и вывод 
		 						{
    								fprintf(library,"|%18s|%20s|%20d|\n",lib[i].name,lib[i].book,lib[i].year);
       								fprintf(library,"|__________________|____________________|____________________|\n");
								}
							//else if (i==n-1)// Почему то как не пробовал с если оно вообще не работает
							//printf("Данного названия нет, попробуйте ешё раз...\n");
						}
		 			fclose(library); // Финальное закрытие 
		 			break;
				}
			default: puts("Таких данных нет, попробуйте ешё раз...\n"); // вывод ошибки если номер в кейсе указан неверно)
		}
}

