#include <stdio.h>
#include <stdlib.h>
#include<locale.h>
struct book
{
  char title[15];
  char author[15];
  int value;
};
int main()
{
  struct book *lib;
  int i,n;
  setlocale(0,"");
  printf("n=?"); scanf("%d",&n);

    lib = (struct book*)malloc(n * sizeof(struct book));
  for (i = 0; i<n; i++)
  { getchar();
    printf("¬ведите название %d книги : ", i + 1);

   gets((lib + i)->title);

    printf("¬ведите автора %d книги : ", i + 1);
    gets((lib + i)->author);
    printf("¬ведите цену %d книги : ", i + 1);
    scanf("%d", &(lib + i)->value);
     getchar();

  }
  for (i = 0; i<n; i++)
  {
    printf("\n %d. %s ", i + 1, (lib + i)->author);
    printf("%s %d", (lib + i)->title, (lib + i)->value);
  }
  getchar();
  return 0;
}
