#include <iostream>
using namespace std;
void recur()
{
    int a;
    a=0;
    cin>>a;
    if(a==0){
    return;
    }
    recur();
    cout<<a<<" ";
}
int main()
{
recur();
}
