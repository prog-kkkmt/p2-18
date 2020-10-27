#include <stdio.h>

int menu(){
 	while(1){
 		system("cls");
 		printf("|       Menu:      |\n");
 		printf("====================\n");
  		printf("|1| Reader list    |\n");
  		printf("|2| Edit list      |\n");
  		printf("|3| Actions list   |\n");
		printf("====================\n");
		printf("|0       Exit      |\n");
		int key = 0;
		scanf("%d",&key);
        switch(key){
            case 1: reader_list();break;
            case 2:
                while(1){
                    system("cls");
                    printf("|     Edit List:   |\n");
                    printf("====================\n");
                    printf("|1| Add reader     |\n");
                    printf("|2| Edit reader    |\n");
                    printf("|3| Remove reader  |\n");
                    printf("====================\n");
                    printf("|0       Back      |\n");
                        int key2 = 0;
                        scanf("%d",&key2);
                            switch(key2){
                                //case 1: add_reader();break;
                                //case 2: edit_reader();break;
                                //case 3: remove_reader();break;
                                case 0: menu();break;
                                default: printf("!Error!");
                            }
                    }break;
            case 3:
                while(1){
                    system("cls");
                    printf("|   Actions List:  |\n");
                    printf("====================\n");
                    printf("|1| Sort by reader |\n");
                    printf("|2| Sort by author |\n");
                    printf("|3| Sort by year   |\n");
                    printf("====================\n");
                    printf("|0       Back      |\n");
                        int key3 = 0;
                        scanf("%d",&key3);
                           switch(key3){
                                //case 1: sort_by_reader();break;
                                //case 2: sort_by_author();break;
                                //case 3: sort_by_year();break;
                                case 0: menu(); break;
                                default: printf("!Error!");
                            }
                    }break;
				getch();
                }
	return 0;
    }
}
