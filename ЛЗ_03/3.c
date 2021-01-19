#include <iostream>
using namespace std;
void re(int x,int a)
{
    if(x == a)
    {
        return;
    }
    cin>>x;
    re (x,a);
    if (x!=0)
    {
        cout<<x<<' ';
    }
}
int main()
{
    int x;
    cin>>x;
    re(x,0);
    if(x!=0)
    {
        cout<<x;
    }
	return 0;
}
