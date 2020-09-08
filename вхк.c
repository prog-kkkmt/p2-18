#include <stdio.h>
#include <conio.h>
#include<string.h>
main()
{     char a[100];
      char b[100];
      char c[100];
      int i;

     FILE *f;

      f = fopen("D:\\tesrt\\data.txt", "r");

     for (i=0;i<3;i++)
     {

         fscanf(f,"%d%d%d",&a[i],&b[i],&c[i]);
     }

 for (i=0;i<3;i++)
     {
         printf("%s%s%s\n",a[i],b[i],c[i]);
     }
     getch();

     fclose(f);
}
