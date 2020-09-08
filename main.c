#include <stdio.h>
#include <conio.h>
#include <stdlib.h>

int main() {

    FILE *file;

    file = fopen("D:/file7.txt", "r");

    fprintf(file, "Hello, World!");

    fclose(file);
}
