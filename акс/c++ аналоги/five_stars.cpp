#include <iostream>

int main()
{
int x=0;
flag:
        std::cout << "*";
        x++;
            if(x<5){
                goto flag;
            }
            else{
                return 0;
            }
}
