/*Даны два текстовых файла. Добавить в конец первого файла содержимое второго файла.*/
#include <stdio.h>
int main() {
  FILE *file2 = fopen ("Read.txt","r");
  int a ;
  fread(a,sizeof(int),50,file2);
  FILE *file1 = fopen ("Open.txt","a");
  fprintf (file1,"\n%d",a);
  fclose(file1);
  fclose(file2);
  return 0;
}
