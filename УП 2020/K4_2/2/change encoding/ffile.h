#ifndef FFILE_H
#define FFILE_H

	#ifdef __cplusplus
	extern "C"
	#endif

size_t show_dir_content(char *path);	//Находит все файлы в катологе и возвращает их кол-во

size_t excessFiles(char *exp_file, size_t num__users);	

#endif
