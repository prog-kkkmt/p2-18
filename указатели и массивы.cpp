#include <iostream>
using namespace std;
void shiftLeft(int ar[], int n) {
    int tmp = ar[0];
    for (int i = 0; i < n-1; ++i)
        ar[i] = ar[i+1];
    ar[n-1] = tmp;
}
int main(){
    const int MAXN = 100;
    int ar[MAXN];
    int n, b;
    cin >> n;
    cin >> b;

    for (int i=0; i<n; i++){
        cin >> ar[i];
    }

    for (int i=0; i<b; i++){
        shiftLeft(ar, n);
    }

    for (int i=0; i<n; i++){
        cout<<ar[i]<<" ";
    }
    return 0;
}
