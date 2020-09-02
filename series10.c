#include <stdio.h>

int main(void)
{
    int i,n,r,b=0;
    printf("kolichestvo:");
    scanf("%i", &n); // ввод колчества чисел
    for (i=1; i<=n; ++i){ // цикл
    printf("%i=",i); // ввод самих чисел
    scanf("%i", &r);
    if (r>0) b=1; // если числа больше 0, то писать True
    }
    printf("%s\n",b?"True":"False");
    return 0;
}
