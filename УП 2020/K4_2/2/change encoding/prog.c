#Выполнил: Безбородов Константин
#Группа: П2-18

//Это программа которая меняет кодировку с Windows на Ubuntu

#include <sys/stat.h>
#include <stdio.h> 

#include "ffile.h"

#define MAXX 1000

char archive_file[MAXX][MAXX];	//Имена всех файлов в катологе
char swap_files[MAXX][MAXX];	//Имена файлов которым нужно сменить кодировку


int main(){
	char path[MAXX];	//путь
	printf("Введите путь к папке:\n");
	scanf("%s", path);
	size_t num__users = show_dir_content(path);	//Получаем все имена файлов и узнаем их кол-во
	
	mkdir("../rus", 0777);	//Создаем папку в которую перекопируем все файлы
	FILE *f_mf = fopen("../rus/makefile", "w");	//Создаем мэйкфайл, который будет выполнять все действия
	
	char exp_file[] = "txt";	//Разрешение файлов, которым будем менять кодировкуchar swap_files[MAXX][MAXX];	//Список хранящий все файлы которым нужно сменить кодировку
	size_t num__swap_files = excessFiles(exp_file, num__users);	//Удаляем не нужные файлы и правильно форматируем для bush
	
	//Вывод имен форматирования
	for (size_t i = 0; i != num__swap_files; ++i)
		printf("%zu| %s\n", i+1, swap_files[i]);
	
	//	{---- Формируем makefile ----}
	
	fprintf(f_mf, "all: swap\n\n");
	fprintf(f_mf, "swap:\n");
	
	char change_encoding[] = "iconv -f WINDOWS-1251 -t UTF-8 -o";	//Код который мы вставим для смены кодировки
	for (size_t i = 0; i != num__swap_files; ++i)
		fprintf(f_mf, "\t%s ../rus/%s ../%s\n", change_encoding, swap_files[i], swap_files[i]);
	
	fclose(f_mf);
	
	return 0;
}

