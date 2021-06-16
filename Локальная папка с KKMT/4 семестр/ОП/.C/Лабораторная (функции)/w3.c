float sum(float k, int n)
{
    float s;
    s=pow(-1, n)*pow(k, 2*n-1)/(2*n+1);
    return s;
}

int w3()
{
	system("cls");
    float x, s = 0, eps = 0.001;
    int i = 0;
    printf ("¬ведите x:\n> ");
    scanf ("%f",&x);
    do
    {
        i++;
        s=s+sum(x, i);
 
    }
    while (sum(x, i) < eps);
    printf ("\n s=%.3f ", s);
    return 0;
}

