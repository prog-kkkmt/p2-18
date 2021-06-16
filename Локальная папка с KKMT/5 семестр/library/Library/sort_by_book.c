#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <locale.h>

struct Library{
	char name[30];
	char book[30];
	int year;
};

void sort_by_book(){
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
fprintf(library,"\n");
    for(i=0;i<n;i++){
       			for(j=0;j<n;j++)
            		if(strcmp((lib+i)->book,lib[j].book)<0){
							temp=lib[i];
							lib[i]=lib[j];
							lib[j]=temp;
                    }
    }
   		    for (i=0;i<n;i++){
    			fprintf(library,"|%18s|%20s|%20d|\n",(lib+i)->name,(lib+i)->book,(lib+i)->year);
    			printf("|%18s|%20s|%20d|\n",(lib+i)->name,(lib+i)->book,(lib+i)->year);
   		    }
   		    fclose(library);
   		    system("pause");
}
