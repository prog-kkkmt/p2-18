#include <iostream>

using namespace std;

int main()
{
int N, K, a=0;
cin >> N;
cin >> K;
if (N>0)
    while (a<N)
    {
    a++;
    cout << K;
    }
else
    cout <<"число меньше или равно 0";
}

/*int main()
{
int N, K, a=0;
cin >> N;
cin >> K;
if (N>0)
    do {
    a++;
    cout << K;
    } while (a<N);
else
    cout <<"число меньше или равно 0";
}
