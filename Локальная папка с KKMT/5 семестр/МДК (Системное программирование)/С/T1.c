#include <stdio.h>
#include <conio.h>
#include <time.h>
#include <locale.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>
//#include "w1.c"

int main()
{ 
	system("title Menu by (ivauuka99)");
 		setlocale(0,"");
 		int key;
 	while(1)
 	{
 		system("cls");
 		printf("|  Выберите соответствующий пунк меню: |\n");
 		printf("========================================\n");
  		printf("|1 |            Задание №1             |\n");
		printf("|0 |              Выход                |\n");
		printf("========================================\n");
		printf("|                                      |\n");
		scanf("%d",&key);
    		switch(key)
    			{ 
					//case 1: w1();break;

      				case 0: exit(0); 
      				default: printf("!ErroR!");
				}
				getch();
	}
	return 0; 
}
