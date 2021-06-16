#include <iostream>
#include <cstdlib>

using namespace std;

int Filling(int *mass, int Size){

}

int main(){
    int n, num, mass[n], Size;
    while(num != 0){
        cout << "1. Filling\n" << "2. Max\n" << "3. Sum\n" << "4. Printing\n" << "0. Exit\n";
        cin >> num;
        switch(num){
            case 1: cin >> n >> Size; Filling()
            //case 2: Max(mass, Size);
           // case 3: Sum(mass, Size);
            //case 4: Printing(mass, Size);
            //case 0: exit(0); break;
            default:
            cout << "Unknown"; break;
        }
    }
    return 0;
}
