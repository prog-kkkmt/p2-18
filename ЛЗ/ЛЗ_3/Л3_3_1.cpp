unsigned gcd(unsigned a, unsigned b)
{
    if(a == 0)
        return b;
    else if(b == 0)
        return a;
    else if(a > b)
        return gcd(b, a % b);
    else
        return gcd(a, b % a);
}
