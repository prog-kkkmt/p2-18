#include <stdio.h>
#include <string.h>

struct Library{
char name[30];
char book[30];
int year;
};

int reader_list(){
        int i,j,n,k,m;
   struct Library *lib,temp;
    FILE *library1 = fopen("library1.txt","r");
        fscanf(library1,"%d",&n);
		lib = (struct Library*)malloc(n*sizeof(struct Library));
    	for(i=0;i<n;i++){
        			fscanf(library1,"%s",&(lib+i)->name);
        			fscanf(library1,"%s",&(lib+i)->book);
        			fscanf(library1,"%d",&(lib+i)->year);
			}
			fclose(library1);
    FILE *library=fopen("library.txt","w");

   						fprintf(library,"                         __________\n");
     					fprintf(library,"                        |Библиотека|\n");
     					fprintf(library," ____________________________________________________________\n");
    					fprintf(library,"|       Автор      |   Название книги   |     Год издания    |\n");
    					fprintf(library,"|__________________|____________________|____________________|\n");

   		for (i=0;i<n;i++)
    		{
    			fprintf(library,"|%18s|%20s|%20d|\n",(lib+i)->name,(lib+i)->book,(lib+i)->year);
       			fprintf(library,"|__________________|____________________|____________________|\n");
			}
						printf("                         __________\n");
     					printf("                        |Библиотека|\n");
     					printf(" ____________________________________________________________\n");
    					printf("|       Автор      |   Название книги   |     Год издания    |\n");
    					printf("|__________________|____________________|____________________|\n");

   		for (i=0;i<n;i++)
    		{
    			printf("|%18s|%20s|%20d|\n",(lib+i)->name,(lib+i)->book,(lib+i)->year);
       			printf("|__________________|____________________|____________________|\n");
			}
    return 0;
}
