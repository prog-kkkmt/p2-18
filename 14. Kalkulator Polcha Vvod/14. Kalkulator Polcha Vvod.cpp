// 14. Kalkulator Polcha Vvod.cpp : Определяет точку входа для приложения.
//

#include "framework.h"
#include "14. Kalkulator Polcha Vvod.h"
#include <stdio.h>
#include <iostream>
#include <cmath>

    int main()
    {
        int stack[10];
        int sp = 0;
        printf("enter retern Poland expression");
        while (!feof(stdin))
        {
            int c = getchar();
            int x;
            switch(c)
            {
            case ' ':
            case '\n':
                break;
            case '=':
                printf("My Result = %d\n", stack[sp - 1]); sp--;
                break;
            case '+':
                stack[sp - 2] = stack[sp - 2] + stack[sp - 1]; sp--;
                break;
            case '-':
                stack[sp - 2] = stack[sp - 2] - stack[sp - 1]; sp--;
                break;
            case '*':
                stack[sp - 2] = stack[sp - 2] * stack[sp - 1]; sp--;
                break;
            case '/':
                stack[sp - 2] = stack[sp - 2] / stack[sp - 1]; sp--;
                break;
            case '^':
                stack[sp - 1] = pow (2,4); sp--;
                break;
            default:
                ungetc(c, stdin);
                if (scanf("%d", &x) != 1)
                {
                    fprintf(stderr, "Can't read integer\n");
                    return -1;
                }
                else
                {
                    stack[sp] = x; sp++;
                }
            }
        }
        printf("Result = %d\n", stack[sp - 1]);
        return 0;
    return 0;
    }
    