unsigned gcd(unsigned a, unsigned b)
{
    if (b!=0)
    {
        return gcd(b,(a%b));
    }
    return a;
}




