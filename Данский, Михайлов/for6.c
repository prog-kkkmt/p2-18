#include <stdio.h>


int main(void)
{   
    
float a, b; //объ€вл€ем переменные
     
scanf("%f", &b); //указываем цену
        
for(a=1.0; a<2.2; a+=0.2)//создаем цикл
        
printf("%.2f\n", a*b);//высчитываем результат
                
    
return 0;
}