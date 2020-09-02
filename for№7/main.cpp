 #include <iostream>         // Джибраилов \/ Завадский

using namespace std;

int main()
{
    int a,b,s,i; // обьявление переменных
    cin>>a>>b; // вводим а,б
    s=0; // при равниваем s к 0 т.к. изначальное значения 1
    for(i=a;i<b+1;i++) 
    {
        s+=i;
    }
    cout<< s; // выводим
    return 0;
}
