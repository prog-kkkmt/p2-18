#include <dirent.h>
#include <sys/stat.h>
#include <stdio.h>

#define MAXX 1000

extern char archive_file[MAXX][MAXX];
extern char swap_files[MAXX][MAXX];	//Список хранящий все файлы которым нужно сменить кодировку

//Находит все файлы в катологе и возвращает их кол-во
size_t show_dir_content(char *path){
	DIR *d = opendir(path); // open the path
	size_t len = 0;
	
	// Если не смогли открыть папку
	if(d == NULL)
		return 0;

	struct dirent *dir;
	for (len = 0; (dir = readdir(d)); ++len)
		sprintf(archive_file[len], "%s", dir->d_name);
	
	closedir(d); // close the directory
	
	return len;
}

//Формирует список только из тех, кому нужна перекодировка
size_t excessFiles(char *exp_file, size_t num__users){
	size_t num__swap_files = 0;
	for (size_t i = 0; i != num__users; ++i){
		char str[MAXX] = "";	//Правильное формирование строки
		size_t len__str = 0;	//Длина этой (^) строки
		
		char ch;	//Текущий символ (используется в цикле)
		//Цикл формирующий правельное имя
		for (size_t j = 0; (ch = archive_file[i][j]) != '\0'; ++j){
			//Так как в bush "пробел - разделитель", надо поставить перед ним '\'
			if (ch == ' ' || ch =='(' || ch == ')')
				str[len__str++] = '\\';
			str[len__str++] = ch;
		}
		int count = 0;	//Счетчик совпадений (для отсичения ненужных файлов)
		//Цикл узнающий, подходит ли имя или нет
		for (size_t j = len__str - 4; j != len__str; ++j)
			if (exp_file[count] == str[j])
				count++;
		
		//Добавляем ли файл
		if (count == 3){
			for (size_t k = 0; k != len__str; ++k)
				swap_files[num__swap_files][k] = str[k];
				
			++num__swap_files;
		}

	}
	
	return num__swap_files;
}
