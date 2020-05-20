#include <iostream>

int main()
{
int x=0;
flag:
        std::cout << "0";
        std::cout << "1";
        x++;
            if(x<5){
                goto flag;
            }
            else{
                return 0;
            }
}
