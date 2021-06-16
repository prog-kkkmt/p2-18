#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <locale.h>

#include "add_reader.h"
#include "find_reader.h"
#include "reader_list.h"
#include "sort_by_author.h"
#include "sort_by_book.h"
#include "sort_by_year.h"

int main(){
    	setlocale(0,"");
    	int a,n,h;
    	char s;
    	char m;
    	 char b;
    	char d;

	m1:	while(1){
 		system("cls");
 		printf("|        Menu      |\n");
 		printf("====================\n");
  		printf("|1| Reader list    |\n");
  		printf("|2| Edit list      |\n");
  		printf("|3| Actions list   |\n");
		printf("====================\n");
		printf("|0|      Exit      |\n");
		int key = 0;
		scanf("%d",&key);
        switch(key){
            case 1: reader_list(a); break;
            case 2:
                while(1){
                    system("cls");
                    printf("|     Edit List    |\n");
                    printf("====================\n");
                    printf("|1| Add author     |\n");
                   // printf("|2| Edit author    |\n");
                    printf("|3| Find author    |\n");
                    //printf("|4| Remove author  |\n");
                    printf("====================\n");
                    printf("|0|      Back      |\n");
                        scanf("%d",&key);
                            switch(key){
                                case 1: add_author(h,m,b,d);break;
                                //case 2: edit_reader();break;
                                case 3: find_reader(s);break;
                                //case 4: remove_reader();break;
                                case 0: goto m1;
                                default: printf("!Error!");
                            }
                    }break;
            case 3:
                while(1){
                    system("cls");
                    printf("|   Actions List   |\n");
                    printf("====================\n");
                    printf("|1| Sort by author |\n");
                    printf("|2| Sort by book   |\n");
                    printf("|3| Sort by year   |\n");
                    printf("====================\n");
                    printf("|0|      Back      |\n");
                        int key3 = 0;
                        scanf("%d",&key);
                           switch(key){
                                case 1: sort_by_author();break;
                                case 2: sort_by_book();break;
                                case 3: sort_by_year();break;
                                case 0: goto m1;
                                default: printf("!Error!");
                          }
                }break;
            case 0: return EXIT_SUCCESS;
				getchar();
        }
	}
	return 0;
}
