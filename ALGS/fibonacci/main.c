#include <stdio.h>
#include <stdlib.h>


int counter = 0;

int fib(int n){
    ++counter;

    if (n == 0)
        return 0;
    if(n == 1)
        return 1;

    return fib(n - 1) + fib(n - 2);
}

int main()
{
    int n;
    scanf("%d", &n);
    printf("fib number: %d", fib(n));
    printf("\n fun fib called: %d times", counter);

    return 0;
}
