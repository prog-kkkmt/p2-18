#include <iostream>
int i = 0, n = 0, s = 0;
void rotate(int a[], unsigned size, int shift)
{
    if(i!=size-1)
    {
        i++;
        int t = a[size-(1+i)];
        a[size-(1+i)] = a[size-1];
        a[size-1] = t;
        return rotate(a, size, shift);
    }
    else
    {
        if(n<shift-1)
        {
            i = 0;
            n++;
            return rotate(a, size, shift);
        }
    else
    {
        for(s=0;s<size;s++)
        {
            std::cout << a[s];
        }
    }
    }
}
int main()
{
    int sizeee, shiiift, b, l = 0;
    std::cout << "Size: ";
    std::cin >> sizeee;
    std::cout << "\nShift: ";
    std::cin >> shiiift;
    int a[sizeee];
    for(l=0;l<sizeee;l++)
    {
        std::cin >> a[l];
    }
    rotate(a, sizeee, shiiift);
}