#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct Library{
char name[30];
char book[30];
int year;
};

void reader_list(){
int i,j,n,k,m;
    struct Library *lib,temp;
    FILE *library1 = fopen("input_data.txt","r");

        fscanf(library1,"%d",&n);
		lib = (struct Library*)malloc(n*sizeof(struct Library));
    	for(i=0;i<n;i++){
        			fscanf(library1,"%s",&(lib+i)->name);
        			fscanf(library1,"%s",&(lib+i)->book);
        			fscanf(library1,"%d",&(lib+i)->year);
		}

		fclose(library1);
    FILE *library = fopen("library.txt","a+");

   		for (i=0;i<n;i++){
    			fprintf(library,"|%18s|%20s|%20d|\n",(lib+i)->name,(lib+i)->book,(lib+i)->year);
    			printf("|%18s|%20s|%20d|\n",(lib+i)->name,(lib+i)->book,(lib+i)->year);
		}

		 fclose(library);
		 system("pause");
}
