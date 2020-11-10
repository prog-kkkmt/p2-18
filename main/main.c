#include "pch.h"

int main(){
    setlocale(0,"");
		while(1){
 		system("cls");
 		printf("|        Menu      |\n");
 		printf("====================\n");
  		printf("|1| find_in_list   |\n");
  		printf("|2| find_in_list2  |\n");
  		printf("|3| sort_bubble    |\n");
  		printf("|4| sort_input     |\n");
  		printf("|5| sort_viborom   |\n");
  		printf("|6| Fibonacci      |\n");
  		printf("|7| NOD and NOK    |\n");
		printf("====================\n");
		printf("|0|      Exit      |\n");
		int key = 0;
		scanf("%d",&key);
        switch(key){
            case 1: find_in_list();break;
            case 2: find_in_list2();break;
            case 3: sort_bubble();break;
            case 4: sort_input();break;
            case 5: sort_viborom();break;
            case 6: n_fib();break;
            case 7: nod_nok();break;
    //        case 8: Rev_str();
     //       case 9: opr_str_kol();
            case 0: return EXIT_SUCCESS;
        }
	}
	return 0;
}


