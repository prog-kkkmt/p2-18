#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct Library{
char name[30];
char book[30];
int year;
};

void add_author(int h,char m[30], char b[30], char d[30]){
    struct Library *lib,temp;
    int n,i;
    printf("Enter the number of new readers: ");
    scanf("%d",&n);
		lib = (struct Library*)malloc(n*sizeof(struct Library));
    	for(i=0;i<n;i++){
        			scanf("%s",&(lib+i)->name);
        			scanf("%s",&(lib+i)->book);
        			scanf("%d",&(lib+i)->year);
		}

    FILE *library = fopen("library.txt","a+");
    FILE *library1 = fopen("input_data.txt","a+");

   		for (i=0;i<n;i++){
    			fprintf(library,"|%18s|%20s|%20d|\n",(lib+i)->name,(lib+i)->book,(lib+i)->year);
    			fprintf(library1," %s %s %d ",(lib+i)->name,(lib+i)->book,(lib+i)->year);
		}
		fclose(library);
		fclose(library1);
}
