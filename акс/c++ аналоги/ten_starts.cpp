#include <iostream>

int main()
{
int x=0;
flag:
        std::cout << "*";
        x++;
            if(x<10){
                goto flag;
            }
}
