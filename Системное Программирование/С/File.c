#include <stdlib.h>
#include <stdio.h>
#include <locale.h>
#include <string.h>

void main()
{

    setlocale(0,"");
    system("cls");
    int arr[256];
  FILE *File;
  char name[] = "file.txt";
     File = fopen("file.txt", "r");
    fscanf(File,"%d", &arr[256]);
    printf("%d ", arr[256]);
      fclose(File);
}
