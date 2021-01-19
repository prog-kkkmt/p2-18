//https://stepik.org/lesson/????-??????-538/step/9?unit=861
int gcd (int a, int b)
{
    if(b == 0)
         return a;
    else
         return gcd (b, a % b);
}
