int i=0,j=0;
void rotate(int a[], unsigned size, int shift)
{
    if (i!=size-1)
    {
        int sw;
        i++;
        sw=a[size-(1+i)];
        a[size-(1+i)]=a[size-1];
        a[size-1]=sw;
        return rotate (a,size,shift);
    }
    else
    {
        if (j<shift-1)
        {
            j++;
            i=0;
            return rotate(a,size,shift);
        }
    }
}
