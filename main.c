#include <stdio.h>  //Джабраилов и Толоконников
#include <stdlib.h>
int main()
{
int n, i;
 scanf("%d",&n);
  int*pa=(int*)malloc(sizeof (int)*n);
   for (int i=0; i<n;++i)
   {
     scanf("%d",pa+i);
   }
     printf("min: %d", *pa);
      free(pa);
       return 0;
}
